"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""
from .make_rest_api_call import *
from .constants import (STATUS_MAPPING,
                        SEVERITY_MAPPING,
                        BUCKET_ID_MAPPING,
                        ASSET_TYPE_MAPPING,
                        ISSUE_STATUS_MAPPING)


def get_issues_discovered(config, params):
    MK = MakeRestApiCall(config=config)
    endpoint = "/easm/{org_id}/issues"
    status = params.get("status")
    asset_type = params.get("asset_type")
    if status:
        params["status"] = STATUS_MAPPING.get(status)
    severity = params.get("severity")
    if severity:
        params["severity"] = SEVERITY_MAPPING.get(severity)
    if asset_type:
        params["asset_type"] = ASSET_TYPE_MAPPING.get(asset_type)
    bucket_id = params.get("bucket_id")
    if bucket_id:
        mapping = []
        for v in bucket_id:
            mapping.append(BUCKET_ID_MAPPING.get(v))
        params["bucket_id"] = ",".join(mapping)
    payload = MK.build_payload(params)
    response = MK.make_request(endpoint=endpoint, method="GET", params=payload)
    return response


def get_issue_by_id(config, params):
    MK = MakeRestApiCall(config=config)
    endpoint = "/easm/{org_id}"+"/issues/{0}". format(params.get("issue_id"))
    response = MK.make_request(endpoint=endpoint, method="GET")
    return response


def get_issue_summary(config, params):
    MK = MakeRestApiCall(config=config)
    endpoint = "/easm/{org_id}/issues_statistics"
    payload = MK.build_payload(params)
    response = MK.make_request(endpoint=endpoint, method="GET", params=payload)
    return response


def get_archived_issues(config, params):
    MK = MakeRestApiCall(config=config)
    status = params.get("status")
    if status:
        params["status"] = STATUS_MAPPING.get(status)
    asset_type = params.get("asset_type")
    if asset_type:
        params['asset_type'] = ASSET_TYPE_MAPPING.get(asset_type, asset_type)
    endpoint = "/easm/{org_id}/archived_issues"
    payload = MK.build_payload(params)
    response = MK.make_request(endpoint=endpoint, method="GET", params=payload)
    return response


def get_archived_issue_comments(config, params):
    MK = MakeRestApiCall(config=config)
    endpoint = "/easm/{org_id}/archived_issues" + "/{0}/comments".format(params.pop('issue_id'))
    comment_type = params.get('comment_type')
    if comment_type:
        params['comment_type'] = comment_type.lower()
    payload = MK.build_payload(params)
    response = MK.make_request(endpoint=endpoint, method="GET", params=payload)
    return response


def get_issue_comments(config, params):
    MK = MakeRestApiCall(config=config)
    endpoint = "/easm/{org_id}/issues" + "/{0}/comments".format(params.pop('issue_id'))
    comment_type = params.get('comment_type')
    if comment_type:
        params['comment_type'] = comment_type.lower()
    payload = MK.build_payload(params)
    response = MK.make_request(endpoint=endpoint, method="GET", params=payload)
    return response


def get_archived_assets(config, params):
    MK = MakeRestApiCall(config=config)
    asset_type = params.get("asset_type")
    if asset_type:
        params['asset_type'] = ASSET_TYPE_MAPPING.get(asset_type, asset_type)
    user_action = params.get("user_action")
    if user_action:
        params["user_action"] = STATUS_MAPPING.get(user_action)
    endpoint = "/easm/{org_id}/archived_assets"
    payload = MK.build_payload(params)
    response = MK.make_request(endpoint=endpoint, method="GET", params=payload)
    return response


def get_tags(config, params):
    MK = MakeRestApiCall(config=config)
    scope = params.get("scope")
    if scope:
        params['scope'] = scope.lower()
    endpoint = "/easm/{org_id}/tags"
    tag_id = params.pop("tag_id", '')
    if tag_id:
        endpoint += f"/{tag_id}"
    payload = MK.build_payload(params)
    response = MK.make_request(endpoint=endpoint, method="GET", params=payload)
    return response


def get_groups(config, params):
    MK = MakeRestApiCall(config=config)
    scope = params.get("scope")
    if scope:
        params['scope'] = scope.lower()
    endpoint = "/easm/{org_id}/groups"
    group_id = params.pop("group_id", '')
    if group_id:
        endpoint += f"/{group_id}"
    payload = MK.build_payload(params)
    response = MK.make_request(endpoint=endpoint, method="GET", params=payload)
    return response


# Update status actions

def update_archived_issue(config, params):
    MK = MakeRestApiCall(config=config)
    endpoint = "/easm/{org_id}"+"/archived_issues/{0}".format(params.pop("issue_id"))
    response = MK.make_request(endpoint=endpoint, method="PATCH", params=params)
    return response

def update_issue_status(config, params):
    status = params.pop("status")
    payload = {"status": ISSUE_STATUS_MAPPING.get(status)}
    MK = MakeRestApiCall(config=config)
    endpoint = "/easm/{org_id}"+"/issues/{0}".format(params.pop("issue_id"))
    print(endpoint)
    response = MK.make_request(endpoint=endpoint, method="PATCH", params=params, data=payload)
    return response
