"""
Copyright start
MIT License
Copyright (c) 2025 Fortinet Inc
Copyright end
"""

from .make_rest_api_call import MakeRestApiCall
from connectors.core.connector import get_logger

logger = get_logger("fortinet-fortirecon-easm")


def create_task(config, params):
    MK = MakeRestApiCall(config=config)
    endpoint = "/security-orchestration/{org_id}/tasks"
    payload = MK.build_payload(params)
    response = MK.make_request(endpoint=endpoint, method="POST", data=payload)
    return response


def update_task(config, params):
    MK = MakeRestApiCall(config=config)
    endpoint = "/security-orchestration/{org_id}"+"/tasks/{0}".format(params.pop("task_id"))
    response = MK.make_request(endpoint=endpoint, method="PATCH", data=params)
    return response
