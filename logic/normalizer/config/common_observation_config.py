def get():
    return {
        'integrationAccountRef': '#$.integration_account#',
        'assetRef': '#$.asset_id#',
        'xMin': '#$.long#',
        'xMax': '#$.long#',
        'yMin': '#$.lat#',
        'yMax': '#$.lat#',
        'spatialExtent': '{"type": "Point", "coordinates":  [#$.long#, #$.lat#]}',
        'contextItems': [
            {
                'code': 'SYN_SYSTEM',
                'value': 'ARABLE'
            }
        ]
    }
