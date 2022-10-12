def get():
    return {

        'ObsCollection': [{
            'codeComponents': [],
            'phenTime': '&convert_to_utc(#$.time#, #$.device.time_zone#)&'
        }]
    }
