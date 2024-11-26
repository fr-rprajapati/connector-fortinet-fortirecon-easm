"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""

from .assets import get_multiple_records
from .make_rest_api_call import MakeRestApiCall
from datetime import datetime


def get_breaches(config, params):
    endpoint = "/easm/{org_id}/breaches"
    has_password = params.get("has_password")
    if has_password:
        params["has_password"] = has_password
    return get_multiple_records(config=config, endpoint=endpoint, params=params)


def get_breaches_by_id(config, params):
    endpoint = "/easm/{org_id}"+"/breaches/{0}".format(params.get("breach_id"))
    return get_multiple_records(config=config, endpoint=endpoint)


def get_leaked_credentials(config, params):
    MK = MakeRestApiCall(config=config)
    endpoint = "/easm/{org_id}/leaked_creds"
    start = params.get("start_date")
    if start:
        params["start_date"] = datetime.strptime(start.strip('Z'), "%Y-%m-%dT%H:%M:%S.%f").strftime("%Y-%m-%d")
    end = params.get("end_date")
    if end:
        params["end_date"] = datetime.strptime(end.strip('Z'), "%Y-%m-%dT%H:%M:%S.%f").strftime("%Y-%m-%d")
    has_password = params.get("has_password")
    if isinstance(has_password, bool):
        params["has_password"] = "true" if has_password else "false"
    payload = MK.build_payload(params)
    response = MK.make_request(endpoint=endpoint, method="GET", params=payload)
    return response


def update_leaked_credential_status(config, params):
    status = params.pop("status")
    payload = {"status": status}
    MK = MakeRestApiCall(config=config)
    endpoint = "/easm/{org_id}"+"/leaked_creds/{0}".format(params.pop("leaked_cred_id"))
    print(endpoint)
    response = MK.make_request(endpoint=endpoint, method="PATCH", params=params, data=payload)
    return response
