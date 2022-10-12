import json
import logging
import re
import uuid

import dateutil
import pytz
from jsonpath_ng.ext import parser
from pytz import timezone

from logic.normalizer.config import common_observation_config, observations_config, crop_mapping_config
from logic.shared import Shared


class Normalizer:
    def __init__(self, **kwargs):
        self.__shared = Shared()

    def normalize(self, schema, account_id, asset_id, raw_object):
        obs_collection_id = str(uuid.uuid1())
        raw_object['integration_account'] = account_id
        raw_object['asset_id'] = asset_id
        observations, obs_collection = self.normalize_raw_obj(
            raw_object,
            schema,
            obs_collection_id
        )
        return obs_collection, obs_collection_id, observations

    def normalize_raw_obj(self, raw_object, schema, observation_collection_id):
        obs_common_data_string = self.replace_config_tokens(raw_object, common_observation_config.get())
        obs_coll_common_data_string = self.replace_config_tokens(raw_object, common_observation_config.get())

        obs_common_data = json.loads(obs_common_data_string)
        obs_coll_common_data = json.loads(obs_coll_common_data_string)

        obs_ids, observations = self.normalize_observations(obs_common_data, schema, raw_object,
                                                            observation_collection_id)

        observation_collection = self.normalize_observation_collection(
            obs_coll_common_data=obs_coll_common_data,
            schema=schema,
            raw_data=raw_object,
            obs_ids=obs_ids,
            observation_collection_id=observation_collection_id
        )

        return observations, observation_collection

    def normalize_observations(self, obs_common_data, schema, raw_data, observation_collection_id):
        observations = observations_config.get(schema, 'obs')
        self.handle_empty_lat_long(obs_common_data)

        obs_ids = []
        observations_list = []
        for observation in observations:
            conditions = observation['conditions']
            for condition in conditions:
                raw_object_exp = parser.parse(condition)
                raw_objects_matched = [match.value for match in raw_object_exp.find(raw_data)]
                if len(raw_objects_matched) <= 0 or raw_objects_matched[0] is None:
                    continue

                observation_string = self.replace_config_tokens(
                    raw_data,
                    observation['observation']
                )
                observation_dict = json.loads(observation_string)
                observation_dict['id'] = str(uuid.uuid4())
                observation_dict['parentCollectionRef'] = observation_collection_id
                observation_dict.update(obs_common_data)

                if not self.location_is_available(observation_dict):
                    observation_dict['spatialExtent'] = None

                observations_list.append(observation_dict)

                obs_ids.append(observation_dict['id'])
                break

        observations = {'Obs': observations_list}

        return obs_ids, observations

    def location_is_available(self, observation):
        return observation['xMin'] is not None and \
               observation['xMax'] is not None and \
               observation['yMin'] is not None and \
               observation['xMax'] is not None

    def normalize_observation_collection(self, **kwargs):
        observation_coll_config = observations_config.get(kwargs.get('schema'), 'obscoll')
        observation_collection_string = self.replace_config_tokens(
            kwargs.get('raw_data'),
            observation_coll_config
        )
        common_data = kwargs.get('obs_coll_common_data')

        self.handle_empty_lat_long(common_data)

        observation_collection = json.loads(observation_collection_string)
        observation_collection['ObsCollection'][0]['id'] = kwargs.get('observation_collection_id')
        observation_collection['ObsCollection'][0]['obsRefs'] = kwargs.get('obs_ids')
        observation_collection['ObsCollection'][0].update(common_data)

        if not self.location_is_available(observation_collection['ObsCollection'][0]):
            observation_collection['ObsCollection'][0]['spatialExtent'] = None

        return observation_collection

    def handle_empty_lat_long(self, common_data):
        if common_data['xMin'] == '' or common_data['xMin'] == 'None' or common_data['xMin'] is None:
            common_data['xMin'] = None
        else:
            common_data['xMin'] = float(common_data['xMin'])
        if common_data['yMin'] == '' or common_data['yMin'] == 'None' or common_data['yMin'] is None:
            common_data['yMin'] = None
        else:
            common_data['yMin'] = float(common_data['yMin'])
        if common_data['xMax'] == '' or common_data['xMax'] == 'None' or common_data['xMax'] is None:
            common_data['xMax'] = None
        else:
            common_data['xMax'] = float(common_data['xMax'])
        if common_data['yMax'] == '' or common_data['yMax'] == 'None' or common_data['yMax'] is None:
            common_data['yMax'] = None
        else:
            common_data['yMax'] = float(common_data['yMax'])

        if common_data['xMin'] is None and common_data['yMin'] is None:
            common_data['spatialExtent'] = '{"type": "Point", "coordinates":  [null, null]}'

    def find_all_function_tokens(self, string):
        return self.unique(re.findall('&.' + '*' + '?&', string))

    def find_all_tokens(self, string):
        return self.unique(re.findall('#.' + '*' + '?#', string))

    def unique(self, ls):
        list_set = set(ls)
        return list(list_set)

    def replace_tokens(self, config_file_string, raw):
        all_tokens = self.find_all_tokens(config_file_string)
        for token in all_tokens:
            config_file_string = self.replace_token(config_file_string, raw, token)

        return config_file_string

    def replace_token(self, config_file_string, raw, token):
        expression = token.replace('#', '')
        try:
            results = [match.value for match in parser.parse(expression).find(raw)]
            if len(results) > 0 and results[0] is not None:
                expression_translated = results[0]
            else:
                logging.warning(f'failed to find mapping for {expression}')
                expression_translated = ''

            config_file_string = config_file_string.replace(token, str(expression_translated))
        except Exception as e:
            logging.warning(e)
            pass

        return config_file_string

    def replace_function_tokens(self, config_file_string, raw):
        all_tokens = self.find_all_function_tokens(config_file_string)
        for token in all_tokens:
            expression = token.replace('&', '')
            try:
                function, params_list = self.extract_function_info(expression)
                expression_translated = function(params_list)
            except Exception as e:
                logging.warning(e)
                expression_translated = ''

            config_file_string = config_file_string.replace(token, str(expression_translated))

        return config_file_string

    def extract_function_info(self, expression):
        index = expression.index('(')
        index2 = expression.index(')')
        function_name = expression[:index]
        function = getattr(self, function_name)
        params = expression[index + 1: index2]
        return function, params.split(',')

    def replace_config_tokens(self, raw, config_dict):
        config_json = json.dumps(config_dict)
        config_json = self.replace_tokens(config_json, raw)
        config_json = self.replace_function_tokens(config_json, raw)

        return config_json

    def map_crop(self, params):
        crop_mapping = crop_mapping_config.get()

        for crop_mapping_obj in crop_mapping:
            if crop_mapping_obj['name'] == params[0]:
                return crop_mapping_obj['databusId']

        logging.warning('failed to find crop mapping')
        return ''

    def convert_to_utc(self, params):
        try:
            date_time = dateutil.parser.parse(params[0].strip().replace('Z', ''))
            tz_info = timezone(params[1].strip())
            date_time_localized = self.__shared.set_timezone(date_time, tz_info)
            date_time_utc = self.__shared.convert_to_timezone(date_time_localized, pytz.utc)

            return date_time_utc.isoformat().replace('+00:00', 'Z')
        except Exception as e:
            logging.warning(e)
            return params[0].strip()

    def generate_asset_id_from_alias(self, **kwargs):
        token_str = f'{kwargs["id"]}#{kwargs["model_scope"]}#{kwargs["system_type"]}#{kwargs["instance_system_id"]}'
        return str(uuid.uuid5(uuid.NAMESPACE_DNS, token_str))

    def handle_lfw(self, params):
        lfw = params[0]

        if lfw == '' or lfw == 'null' or lfw is None:
            return ''

        lfw = float(params[0])
        if lfw == 1:
            return 'true'
        elif lfw == 0:
            return 'false'

        return ''
