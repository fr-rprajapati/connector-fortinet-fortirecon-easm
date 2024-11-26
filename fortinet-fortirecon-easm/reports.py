"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""

from .make_rest_api_call import MakeRestApiCall
from connectors.core.connector import get_logger

logger = get_logger("fortinet-fortirecon-easm")


def generate_report(config, params):
    MK = MakeRestApiCall(config=config)
    endpoint = "/easm/{org_id}/reports"
    payload = MK.build_payload(params)
    response = MK.make_request(endpoint=endpoint, method="POST", params=payload)
    return response


def get_report(config, params):
    MK = MakeRestApiCall(config=config)
    endpoint = "/easm/{org_id}"+"/reports/{report_id}".format(report_id=params.get("report_id"))
    response = MK.make_request(endpoint=endpoint, method="GET", params=params)
    if response.get('report_url') and not params.get('get_link'):
        return MK.make_request(url=response.get('report_url'), flag=False)
    return response

