from logic.normalizer.config import observations_daily_config, observations_hourly_config, observation_collection_hourly_config
from logic.normalizer.config import observation_collection_daily_config


def get(schema, file_type):
    config = {
        'hourly_obs': observations_hourly_config.get(),
        'daily_obs': observations_daily_config.get(),
        'hourly_obscoll': observation_collection_hourly_config.get(),
        'daily_obscoll': observation_collection_daily_config.get()
    }
    return config[schema + '_' + file_type]
