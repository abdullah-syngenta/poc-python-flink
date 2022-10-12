from logic.normalizer.config import cc_agg_time_hourly


def get():
    phen_time = '#$.time#'
    CC_AGG_TIME_HOUR = cc_agg_time_hourly.get()
    unit_w1_m2_1 = 'W1[m2]-1'

    return [
        {
            'conditions': ['$.b1dw'],
            'observation': {
                'obsCode': 'E_SPEC_BND_1_DN',
                'codeComponents': [CC_AGG_TIME_HOUR],
                'phenTime': phen_time,
                'valueUoM': unit_w1_m2_1,
                'value': '#$.b1dw#'
            }
        },
        {
            'conditions': ['$.b1uw'],
            'observation': {
                'obsCode': 'E_SPEC_BND_1_UP',
                'codeComponents': [CC_AGG_TIME_HOUR],
                'phenTime': phen_time,
                'valueUoM': unit_w1_m2_1,
                'value': '#$.b1uw#'
            }

        },
        {
            'conditions': ['$.b2dw'],
            'observation': {
                'obsCode': 'E_SPEC_BND_2_DN',
                'codeComponents': [CC_AGG_TIME_HOUR],
                'phenTime': phen_time,
                'valueUoM': 'W1[m2]-1',
                'value': '#$.b2dw#'
            }

        },
        {
            'conditions': ['$.b2uw'],
            'observation': {
                'obsCode': 'E_SPEC_BND_2_UP',
                'codeComponents': [CC_AGG_TIME_HOUR],
                'phenTime': phen_time,
                'valueUoM': unit_w1_m2_1,
                'value': '#$.b2uw#'
            }

        },
        {
            'conditions': ['$.b3dw'],
            'observation': {
                'obsCode': 'E_SPEC_BND_3_DN',
                'codeComponents': [CC_AGG_TIME_HOUR],
                'phenTime': phen_time,
                'valueUoM': unit_w1_m2_1,
                'value': '#$.b3dw#'
            }

        },
        {
            'conditions': ['$.b3uw'],
            'observation': {
                'obsCode': 'E_SPEC_BND_3_UP',
                'codeComponents': [CC_AGG_TIME_HOUR],
                'phenTime': phen_time,
                'valueUoM': unit_w1_m2_1,
                'value': '#$.b3uw#'
            }

        },
        {
            'conditions': ['$.b4dw'],
            'observation': {
                'obsCode': 'E_SPEC_BND_4_DN',
                'codeComponents': [CC_AGG_TIME_HOUR],
                'phenTime': phen_time,
                'valueUoM': unit_w1_m2_1,
                'value': '#$.b4dw#'
            }

        },
        {
            'conditions': ['$.b4uw'],
            'observation': {
                'obsCode': 'E_SPEC_BND_4_UP',
                'codeComponents': [CC_AGG_TIME_HOUR],
                'phenTime': phen_time,
                'valueUoM': unit_w1_m2_1,
                'value': '#$.b4uw#'
            }

        },
        {
            'conditions': ['$.b5dw'],
            'observation': {
                'obsCode': 'E_SPEC_BND_5_DN',
                'codeComponents': [CC_AGG_TIME_HOUR],
                'phenTime': phen_time,
                'valueUoM': unit_w1_m2_1,
                'value': '#$.b5dw#'
            }

        },
        {
            'conditions': ['$.b5uw'],
            'observation': {
                'obsCode': 'E_SPEC_BND_5_UP',
                'codeComponents': [CC_AGG_TIME_HOUR],
                'phenTime': phen_time,
                'valueUoM': unit_w1_m2_1,
                'value': '#$.b5uw#'
            }

        },
        {
            'conditions': ['$.b6dw'],
            'observation': {
                'obsCode': 'E_SPEC_BND_6_DN',
                'codeComponents': [CC_AGG_TIME_HOUR],
                'phenTime': phen_time,
                'valueUoM': unit_w1_m2_1,
                'value': '#$.b6dw#'
            }
        },
        {
            'conditions': ['$.b6uw'],
            'observation': {
                'obsCode': 'E_SPEC_BND_6_UP',
                'codeComponents': [CC_AGG_TIME_HOUR],
                'phenTime': phen_time,
                'valueUoM': unit_w1_m2_1,
                'value': '#$.b6uw#'
            }
        },
        {
            'conditions': ['$.b7dw'],
            'observation':
                {
                    'obsCode': 'E_SPEC_BND_7_DN',
                    'codeComponents': [CC_AGG_TIME_HOUR],
                    'phenTime': phen_time,
                    'valueUoM': unit_w1_m2_1,
                    'value': '#$.b7dw#'
                }
        },
        {
            'conditions': ['$.maxt'],
            'observation': {
                'obsCode': 'E_AIR_TEMPERATURE',
                'codeComponents': [
                    CC_AGG_TIME_HOUR,
                    {
                        'componentCode': 'CC_AGG_METHOD_MAX',
                        'componentType': 'AGG_METHOD',
                        'selector': 'MAX'
                    }
                ],
                'phenTime': phen_time,
                'valueUoM': 'C',
                'value': '#$.maxt#'
            }
        },
        {
            'conditions': ['$.lwuw'],
            'observation': {
                'obsCode': 'E_LNG_WAVE_RAD_UP',
                'codeComponents': [
                    CC_AGG_TIME_HOUR,
                    {
                        'componentCode': 'CC_AGG_METHOD_MEAN',
                        'componentType': 'AGG_METHOD',
                        'selector': 'MEAN'
                    }
                ],
                'phenTime': phen_time,
                'valueUoM': unit_w1_m2_1,
                'value': '#$.lwuw#'
            }
        },
        {
            'conditions': ['$.lwdw'],
            'observation': {
                'obsCode': 'E_LNG_WAVE_RAD_DN',
                'codeComponents': [
                    CC_AGG_TIME_HOUR,
                    {
                        'componentCode': 'CC_AGG_METHOD_MEAN',
                        'componentType': 'AGG_METHOD',
                        'selector': 'MEAN'
                    }
                ],
                'phenTime': phen_time,
                'valueUoM': unit_w1_m2_1,
                'value': '#$.lwdw#'
            }
        },
        {
            'conditions': ['$.low_quality'],
            'observation': {
                'obsCode': 'AD_QUALITY_LOW_FLAG',
                'codeComponents': [CC_AGG_TIME_HOUR],
                'phenTime': phen_time,
                'valueUoM': '',
                'value': '#$.low_quality#'
            }
        },
        {
            'conditions': ['$.lfw'],
            'observation': {
                'obsCode': 'E_LEAF_WETNESS_B',
                'codeComponents': [CC_AGG_TIME_HOUR],
                'phenTime': phen_time,
                'valueUoM': '',
                'value': '&handle_lfw(#$.lfw#)&'
            }
        },
        {
            'conditions': ['$.et_version'],
            'observation': {
                'obsCode': 'E_DSG_ET_VER',
                'codeComponents': [CC_AGG_TIME_HOUR],
                'phenTime': phen_time,
                'valueUoM': '',
                'value': '#$.et_version#'
            }
        },
        {
            'conditions': ['$.etc'],
            'observation': {
                'obsCode': 'E_CROP_ET',
                'codeComponents': [
                    CC_AGG_TIME_HOUR,
                    {
                        'componentCode': 'CC_FOI_CROP',
                        'componentType': 'FEATURE_OF_INTEREST',
                        'selector': 'CROP',
                        'value': '&map_crop(#$.growing_season.crop_varietal.crop_category.name#)&'
                    }
                ],
                'phenTime': phen_time,
                'valueUoM': 'mm',
                'value': '#$.etc#'
            }
        },
        {
            'conditions': ['$.et'],
            'observation': {
                'obsCode': 'E_REF_ET',
                'codeComponents': [CC_AGG_TIME_HOUR],
                'phenTime': phen_time,
                'valueUoM': 'mm',
                'value': '#$.et#'
            }
        },
        {
            'conditions': ['$.ea'],
            'observation': {
                'obsCode': 'E_ACT_H2O_V_PRESS',
                'codeComponents': [CC_AGG_TIME_HOUR],
                'phenTime': phen_time,
                'valueUoM': 'hPa',
                'value': '#$.ea * 10#'
            }
        },
        {
            'conditions': ['$.b7uw'],
            'observation': {
                'obsCode': 'E_SPEC_BND_7_UP',
                'codeComponents': [CC_AGG_TIME_HOUR],
                'phenTime': phen_time,
                'valueUoM': unit_w1_m2_1,
                'value': '#$.b7uw#'
            }
        },
        {
            'conditions': ['$.max_tdew'],
            'observation': {
                'obsCode': 'E_DEWPOINT',
                'codeComponents': [
                    CC_AGG_TIME_HOUR,
                    {
                        'componentCode': 'CC_AGG_METHOD_MAX',
                        'componentType': 'AGG_METHOD',
                        'selector': 'MAX'
                    }
                ],
                'phenTime': phen_time,
                'valueUoM': 'C',
                'value': '#$.max_tdew#'
            }
        },
        {
            'conditions': ['$.min_rh'],
            'observation': {
                'obsCode': 'E_RELATIVE_HUMIDITY',
                'codeComponents': [
                    CC_AGG_TIME_HOUR,
                    {
                        'componentCode': 'CC_AGG_METHOD_MIN',
                        'componentType': 'AGG_METHOD',
                        'selector': 'MIN'
                    }
                ],
                'phenTime': phen_time,
                'valueUoM': 'prcnt',
                'value': '#$.min_rh#'
            }
        },
        {
            'conditions': ['$.mint'],
            'observation': {
                'obsCode': 'E_AIR_TEMPERATURE',
                'codeComponents': [
                    CC_AGG_TIME_HOUR,
                    {
                        'componentCode': 'CC_AGG_METHOD_MIN',
                        'componentType': 'AGG_METHOD',
                        'selector': 'MIN'
                    }
                ],
                'phenTime': phen_time,
                'valueUoM': 'C',
                'value': '#$.mint#'
            }
        },
        {
            'conditions': ['$.p'],
            'observation': {
                'obsCode': 'E_ATM_PRESSURE',
                'codeComponents': [CC_AGG_TIME_HOUR],
                'phenTime': phen_time,
                'valueUoM': 'hPa',
                'value': '#$.p * 10#'
            }
        },
        {
            'conditions': ['$.pardw'],
            'observation': {
                'obsCode': 'E_PAR_DN',
                'codeComponents': [CC_AGG_TIME_HOUR],
                'phenTime': phen_time,
                'valueUoM': 'mol1[m2]-1s-1',
                'value': '#$.pardw#'
            }
        },
        {
            'conditions': ['$.paruw'],
            'observation': {
                'obsCode': 'E_PAR_UP',
                'codeComponents': [CC_AGG_TIME_HOUR],
                'phenTime': phen_time,
                'valueUoM': 'mol1[m2]-1s-1',
                'value': '#$.paruw#'
            }
        },
        {
            'conditions': ['$.prate'],
            'observation': {
                'obsCode': 'E_RAINFALL_PER_TIME',
                'codeComponents': [CC_AGG_TIME_HOUR],
                'phenTime': phen_time,
                'valueUoM': 'mm1hr-1',
                'value': '#$.prate#'
            }
        },
        {
            'conditions': ['$.precip'],
            'observation': {
                'obsCode': 'E_RAINFALL',
                'codeComponents': [
                    CC_AGG_TIME_HOUR,
                    {
                        'componentCode': 'CC_AGG_METHOD_SUM',
                        'componentType': 'AGG_METHOD',
                        'selector': 'SUM'
                    }
                ],
                'phenTime': phen_time,
                'valueUoM': 'mm',
                'value': '#$.precip#'
            }
        },
        {
            'conditions': ['$.rh'],
            'observation': {
                'obsCode': 'E_RELATIVE_HUMIDITY',
                'codeComponents': [CC_AGG_TIME_HOUR],
                'phenTime': phen_time,
                'valueUoM': 'prcnt',
                'value': '#$.rh#'
            }
        },
        {
            'conditions': ['$.sample_pct'],
            'observation': {
                'obsCode': 'E_AGG_SAMPLE_PCNT',
                'codeComponents': [CC_AGG_TIME_HOUR],
                'phenTime': phen_time,
                'valueUoM': 'prcnt',
                'value': '#$.sample_pct#'
            }
        },
        {
            'conditions': ['$.slp'],
            'observation': {
                'obsCode': 'E_SEA_LVL_PRESSURE',
                'codeComponents': [CC_AGG_TIME_HOUR],
                'phenTime': phen_time,
                'valueUoM': 'hPa',
                'value': '#$.slp * 10#'
            }
        },
        {
            'conditions': ['$.swdw'],
            'observation': {
                'obsCode': 'E_SHRT_WAVE_RAD_DN',
                'codeComponents': [
                    CC_AGG_TIME_HOUR,
                    {
                        'componentCode': 'CC_AGG_METHOD_MEAN',
                        'componentType': 'AGG_METHOD',
                        'selector': 'MEAN'
                    }
                ],
                'phenTime': phen_time,
                'valueUoM': unit_w1_m2_1,
                'value': '#$.swdw#'
            }
        },
        {
            'conditions': ['$.swuw'],
            'observation': {
                'obsCode': 'E_SHRT_WAVE_RAD_UP',
                'codeComponents': [
                    CC_AGG_TIME_HOUR,
                    {
                        'componentCode': 'CC_AGG_METHOD_MEAN',
                        'componentType': 'AGG_METHOD',
                        'selector': 'MEAN'
                    }
                ],
                'phenTime': phen_time,
                'valueUoM': unit_w1_m2_1,
                'value': '#$.swuw#'
            }
        },
        {
            'conditions': ['$.tabove'],
            'observation': {
                'obsCode': 'E_SKY_TEMPERATURE',
                'codeComponents': [CC_AGG_TIME_HOUR],
                'phenTime': phen_time,
                'valueUoM': 'C',
                'value': '#$.tabove#'
            }
        },
        {
            'conditions': ['$.tair'],
            'observation': {
                'obsCode': 'E_AIR_TEMPERATURE',
                'codeComponents': [CC_AGG_TIME_HOUR],
                'phenTime': phen_time,
                'valueUoM': 'C',
                'value': '#$.tair#'
            }
        },
        {
            'conditions': ['$.tbelow'],
            'observation': {
                'obsCode': 'E_LEAF_TEMPERATURE',
                'codeComponents': [CC_AGG_TIME_HOUR],
                'phenTime': phen_time,
                'valueUoM': 'C',
                'value': '#$.tbelow#'
            }
        },
        {
            'conditions': ['$.tdew'],
            'observation': {
                'obsCode': 'E_DEWPOINT',
                'codeComponents': [CC_AGG_TIME_HOUR],
                'phenTime': phen_time,
                'valueUoM': 'C',
                'value': '#$.tdew#'
            }
        },
        {
            'conditions': ['$.vpd'],
            'observation': {
                'obsCode': 'E_VPD',
                'codeComponents': [CC_AGG_TIME_HOUR],
                'phenTime': phen_time,
                'valueUoM': 'hPa',
                'value': '#$.vpd * 10#'
            }
        },
        {
            'conditions': ['$.wind_direction'],
            'observation': {
                'obsCode': 'E_WIND_DIRECTION',
                'codeComponents': [CC_AGG_TIME_HOUR],
                'phenTime': phen_time,
                'valueUoM': '',
                'value': '#$.wind_direction#'
            }
        },
        {
            'conditions': ['$.wind_heading'],
            'observation': {
                'obsCode': 'E_WIND_HEADING',
                'codeComponents': [CC_AGG_TIME_HOUR],
                'phenTime': phen_time,
                'valueUoM': 'arcdeg',
                'value': '#$.wind_heading#'
            }
        },
        {
            'conditions': ['$.wind_speed'],
            'observation': {
                'obsCode': 'E_WIND_SPEED',
                'codeComponents': [CC_AGG_TIME_HOUR],
                'phenTime': phen_time,
                'valueUoM': 'km1hr-1',
                'value': '#$.wind_speed#'
            }
        },
        {
            'conditions': ['$.wind_speed_max'],
            'observation': {
                'obsCode': 'E_WIND_SPEED',
                'codeComponents': [
                    CC_AGG_TIME_HOUR,
                    {
                        'componentCode': 'CC_AGG_METHOD_MAX',
                        'componentType': 'AGG_METHOD',
                        'selector': 'MAX'
                    }
                ],
                'phenTime': phen_time,
                'valueUoM': 'km1hr-1',
                'value': '#$.wind_speed_max#'
            }
        },
        {
            'conditions': ['$.wind_speed_min'],
            'observation': {
                'obsCode': 'E_WIND_SPEED',
                'codeComponents': [
                    CC_AGG_TIME_HOUR,
                    {
                        'componentCode': 'CC_AGG_METHOD_MIN',
                        'componentType': 'AGG_METHOD',
                        'selector': 'MIN'
                    }
                ],
                'phenTime': phen_time,
                'valueUoM': 'km1hr-1',
                'value': '#$.wind_speed_min#'
            }
        }
    ]
