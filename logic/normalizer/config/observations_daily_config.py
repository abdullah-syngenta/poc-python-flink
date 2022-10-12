from logic.normalizer.config import cc_agg_time_daily


def get():
    phen_time_config = '&convert_to_utc(#$.time#,#$.device.time_zone#)&'
    CC_AGG_TIME_DAILY = cc_agg_time_daily.get()
    mint_time = '&convert_to_utc(#$.mint_time#,#$.device.time_zone#)&'
    maxt_time = '&convert_to_utc(#$.maxt_time#,#$.device.time_zone#)&'
    map_crop = '&map_crop(#$.growing_season.crop_varietal.crop_category.name#)&'
    return [
        {
            'conditions': ['$.cl'],
            'observation': {

                'obsCode': 'E_CHLOROPHYLL_INDX',
                'codeComponents': [CC_AGG_TIME_DAILY],
                'phenTime': phen_time_config,
                'valueUoM': '',
                'value': '#$.cl#'
            }
        },
        {
            'conditions': ['$.crop_water_demand'],
            'observation': {
                'obsCode': 'E_CRP_H2O_DMD_PER_DAY',
                'codeComponents': [
                    CC_AGG_TIME_DAILY,
                    {
                        'componentCode': 'CC_FOI_CROP',
                        'componentType': 'FEATURE_OF_INTEREST',
                        'selector': 'CROP',
                        'value': map_crop
                    }],
                'phenTime': phen_time_config,
                'valueUoM': 'mm1day-1',
                'value': '#$.crop_water_demand#'
            }
        },
        {
            'conditions': ['$.dli'],
            'observation': {
                'obsCode': 'E_DLY_LIGHT_INTG',
                'codeComponents': [CC_AGG_TIME_DAILY],
                'phenTime': phen_time_config,
                'valueUoM': 'mol1[m2]-1day-1',
                'value': '#$.dli#'
            }
        },
        {
            'conditions': ['$.gdd'],
            'observation': {
                'obsCode': 'E_GDD',
                'codeComponents': [
                    CC_AGG_TIME_DAILY,
                    {
                        'componentCode': 'CC_PARAM_GDD_TEMP_BASE',
                        'componentType': 'PARAMETER',
                        'selector': 'A_GDD_TEMP_BASE',
                        'value': '#$.growing_season.crop_varietal.gdd_temp_base#',
                        'valueUoM': 'C'
                    },
                    {
                        'componentCode': 'CC_FOI_CROP',
                        'componentType': 'FEATURE_OF_INTEREST',
                        'selector': 'CROP',
                        'value': map_crop
                    },
                    {
                        'componentCode': 'CC_PARAM_GDD_SOURCE',
                        'componentType': 'PARAMETER',
                        'selector': 'A_GDD_SOURCE',
                        'value': '#gdd_source#'
                    }],
                'phenTime': phen_time_config,
                'valueUoM': '',
                'value': '#$.gdd#'
            }
        },
        {
            'conditions': ['$.gdd_cumulative'],
            'observation': {
                'obsCode': 'E_GDD_CUMULATIVE',
                'codeComponents': [
                    CC_AGG_TIME_DAILY,
                    {
                        'componentCode': 'CC_PARAM_GDD_TEMP_BASE',
                        'componentType': 'PARAMETER',
                        'selector': 'A_GDD_TEMP_BASE',
                        'value': '#$.growing_season.crop_varietal.gdd_temp_base#',
                        'valueUoM': 'C'
                    },
                    {
                        'componentCode': 'CC_FOI_CROP',
                        'componentType': 'FEATURE_OF_INTEREST',
                        'selector': 'CROP',
                        'value': map_crop
                    },
                    {
                        'componentCode': 'CC_PARAM_GDD_SOURCE',
                        'componentType': 'PARAMETER',
                        'selector': 'A_GDD_SOURCE',
                        'value': '#$.gdd_cumulative_source#'
                    }
                ],
                'phenTime': phen_time_config,
                'valueUoM': '',
                'value': '#$.gdd_cumulative#'
            }
        },
        {
            'conditions': ['$.tdew_at_mint'],
            'observation': {
                'obsCode': 'E_DEWPOINT',
                'codeComponents': [{

                }],
                'phenTime': '&convert_to_utc(#$.mint_time#, #$.device.time_zone#)&',
                'valueUoM': 'C',
                'value': '#$.tdew_at_mint#'
            }
        },
        {
            'observation': {
                'obsCode': 'E_SHRT_WAVE_RAD_DN',
                'codeComponents': [
                    CC_AGG_TIME_DAILY,
                    {
                        'componentCode': 'CC_AGG_METHOD_SUM',
                        'componentType': 'AGG_METHOD',
                        'selector': 'SUM'
                    }
                ],
                'phenTime': '&convert_to_utc(#$.time#, #$.device.time_zone#)&',
                'valueUoM': 'MJ1[m2]-1',
                'value': '#$.swdw#'
            },
            'conditions': ['$.swdw'],
        },
        {
            'conditions': ['$.sunshine_duration'],
            'observation': {
                'obsCode': 'E_SHRT_WAVE_RAD_DN_HOUR_COUNT',
                'codeComponents': [
                    CC_AGG_TIME_DAILY,
                    {
                        'componentCode': 'CC_AGG_METHOD_SUM',
                        'componentType': 'AGG_METHOD',
                        'selector': 'SUM'
                    },
                    {
                        'componentCode': 'CC_PARAM_GREATER_THAN',
                        'componentType': 'PARAMETER',
                        'selector': 'GREATER_THAN',
                        'value': '120.0',
                        'valueUoM': 'W1[m2]-1'
                    }
                ],
                'phenTime': '&convert_to_utc(#$.time#,#$.device.time_zone#)&',
                'valueUoM': 'count',
                'value': '#$.sunshine_duration#'
            }
        },
        {
            'conditions': ['$.rh_at_mint'],
            'observation': {
                'obsCode': 'E_RELATIVE_HUMIDITY',
                'codeComponents': [{

                }],
                'phenTime': mint_time,
                'valueUoM': 'prcnt',
                'value': '#$.rh_at_mint#'
            }
        },
        {
            'conditions': ['$.rh_at_maxt'],
            'observation': {
                'obsCode': 'E_RELATIVE_HUMIDITY',
                'codeComponents': [{

                }],
                'phenTime': maxt_time,
                'valueUoM': 'prcnt',
                'value': '#$.rh_at_maxt#'
            }
        },
        {
            'conditions': ['$.precip_hours'],
            'observation': {
                'obsCode': 'E_RAINFALL_HOUR_COUNT',
                'codeComponents': [
                    CC_AGG_TIME_DAILY,
                    {
                        'componentCode': 'CC_AGG_METHOD_SUM',
                        'componentType': 'AGG_METHOD',
                        'selector': 'SUM'
                    },
                    {
                        'componentCode': 'CC_FOI_RAINFALL',
                        'componentType': 'FEATURE_OF_INTEREST',
                        'selector': 'ENVIRONMENT'
                    },
                    {
                        'componentCode': 'CC_PARAM_GREATER_THAN',
                        'componentType': 'PARAMETER',
                        'selector': 'GREATER_THAN',
                        'value': '0.1',
                        'valueUoM': 'mm1hr-1'
                    }
                ],
                'phenTime': phen_time_config,
                'valueUoM': 'count',
                'value': '#$.precip_hours#'
            }
        },
        {
            'conditions': ['$.ndvi'],
            'observation': {
                'obsCode': 'E_NDVI',
                'codeComponents': [CC_AGG_TIME_DAILY],
                'phenTime': phen_time_config,
                'valueUoM': '',
                'value': '#$.ndvi#'
            }
        },
        {
            'observation': {
                'obsCode': 'E_AIR_TEMPERATURE',
                'codeComponents': [
                    CC_AGG_TIME_DAILY,
                    {
                        'componentCode': 'CC_AGG_METHOD_MAX',
                        'componentType': 'AGG_METHOD',
                        'selector': 'MAX'
                    }
                ],
                'phenTime': maxt_time,
                'valueUoM': 'C',
                'value': '#$.maxt#'
            },
            'conditions': ['$.maxt']
        },
        {
            'observation': {
                'obsCode': 'E_AIR_TEMPERATURE',
                'codeComponents': [
                    CC_AGG_TIME_DAILY,
                    {
                        'componentCode': 'CC_AGG_METHOD_MIN',
                        'componentType': 'AGG_METHOD',
                        'selector': 'MIN'
                    }
                ],
                'phenTime': mint_time,
                'valueUoM': 'C',
                'value': '#$.mint#'
            },
            'conditions': ['$.mint']
        },
        {
            'conditions': ['$.low_quality'],
            'observation': {
                'obsCode': 'AD_QUALITY_LOW_FLAG',
                'codeComponents': [CC_AGG_TIME_DAILY],
                'phenTime': phen_time_config,
                'valueUoM': '',
                'value': '#$.low_quality#'
            }
        },
        {
            'conditions': ['$.lfairdelta'],
            'observation': {
                'obsCode': 'E_LEAF_AIR_TEMP_DIFF',
                'codeComponents': [CC_AGG_TIME_DAILY],
                'phenTime': phen_time_config,
                'valueUoM': 'C',
                'value': '#$.lfairdelta#'
            }
        },
        {
            'conditions': ['$.kc'],
            'observation': {
                'obsCode': 'E_CROP_COEFF',
                'codeComponents': [
                    CC_AGG_TIME_DAILY,
                    {
                        'componentCode': 'CC_FOI_CROP',
                        'componentType': 'FEATURE_OF_INTEREST',
                        'selector': 'CROP',
                        'value': map_crop
                    }
                ],
                'phenTime': phen_time_config,
                'valueUoM': '',
                'value': '#$.kc#'
            }
        }
    ]
