import json
import uuid

import epsagon


class AlertRaiser:
    def __init__(self):
        self.__alerts = []

    def raise_alert(self, alert_type, alert_code, details):
        alert = {
            'id': str(uuid.uuid1()),
            'account_id': details.get('account_id', 'Unknown'),
            'alert_type': alert_type,
            'alert_code': alert_code,
            'details': details
        }

        self.__alerts.append(alert)

    def __get_raised_alerts(self):
        return self.__alerts

    def raise_epsagon_error(self):
        alerts = self.__get_raised_alerts()
        if len(alerts) > 0:
            epsagon.label('alert', True)
            epsagon.label('alerts_count', len(alerts))
            epsagon.label('type', json.dumps([alert['alert_type'] for alert in alerts]))
            epsagon.label('alerts', json.dumps([alert['alert_code'] for alert in alerts]))
            epsagon.label('details', json.dumps([alert.get('details') for alert in alerts]))
            epsagon.error(Exception('Arable One or more alerts was raised'))
