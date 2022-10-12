import os

import epsagon


def init_epsagon():
    epsagon.init(
        token=os.getenv('EPSAGON_TOKEN'),
        app_name=os.getenv('EPSAGON_APP_NAME'),
        metadata_only=False
    )
