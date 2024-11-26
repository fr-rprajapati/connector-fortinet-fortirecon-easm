"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""

from .make_rest_api_call import MakeRestApiCall


def get_scan_statistics(config, params):
    endpoint = "/easm/{org_id}/scan_statistics"
    MK = MakeRestApiCall(config=config)
    payload = MK.build_payload(params)
    response = MK.make_request(endpoint=endpoint, method="GET", params=payload)
    return response
