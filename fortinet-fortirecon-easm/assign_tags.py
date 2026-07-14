"""
Copyright start
MIT License
Copyright (c) 2026 Fortinet Inc
Copyright end
"""
from .make_rest_api_call import MakeRestApiCall


def assign_tag(config, payload):
    MK = MakeRestApiCall(config=config)
    endpoint = "/easm/{org_id}/assign_tag"
    response = MK.make_request(endpoint=endpoint, method="POST", data=payload)
    return response

def unassign_tag(config, payload):
    MK = MakeRestApiCall(config=config)
    endpoint = "/easm/{org_id}/unassign_tag"
    response = MK.make_request(endpoint=endpoint, method="POST", data=payload)
    return response


