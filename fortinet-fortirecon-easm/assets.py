"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""

from .make_rest_api_call import MakeRestApiCall
from .constants import SEARCH_TYPE_MAPPING


def get_asset_asns(config, params):
    search_type = params.get('search_type')
    if search_type:
        params['search_type'] = SEARCH_TYPE_MAPPING.get(search_type, search_type)
    endpoint = "/easm/{org_id}/assets/asns"
    return get_multiple_records(config=config, endpoint=endpoint, params=params)


def get_asns_by_asset_id(config, params):
    asset_id = params.pop("asset_id")
    endpoint = "/easm/{org_id}/"+"assets/asns/{0}".format(asset_id)
    return get_multiple_records(config=config, endpoint=endpoint, params=params)


def get_domains(config, params):
    endpoint = "/easm/{org_id}/assets/domains"
    return get_multiple_records(config=config, endpoint=endpoint, params=params)


def get_domains_by_asset_id(config, params):
    endpoint = "/easm/{org_id}"+"/assets/domains/{0}".format(params.pop("asset_id"))
    return get_multiple_records(config=config, endpoint=endpoint, params=params)


def get_ips(config, params):
    endpoint = "/easm/{org_id}/assets/ips"
    ports = params.get('ports')
    if ports:
        params['ports'] = str(ports).strip('[]()')
    return get_multiple_records(config=config, endpoint=endpoint, params=params)


def get_ips_by_asset_id(config, params):
    endpoint = "/easm/{org_id}"+"/assets/ips/{0}".format(params.pop("asset_id"))
    return get_multiple_records(config=config, endpoint=endpoint, params=params)


def get_prefixes(config, params):
    endpoint = "/easm/{org_id}/assets/prefixes"
    return get_multiple_records(config=config, endpoint=endpoint, params=params)


def get_prefixes_by_asset_id(config, params):
    endpoint = "/easm/{org_id}"+"/assets/prefixes/{0}".format(params.pop("asset_id"))
    return get_multiple_records(config=config, endpoint=endpoint, params=params)


def get_subdomains(config, params):
    endpoint = "/easm/{org_id}/assets/subdomains"
    ports = params.get('ports')
    if ports:
        params['ports'] = str(ports).strip('[]()')
    return get_multiple_records(config=config, endpoint=endpoint, params=params)


def get_subdomains_by_asset_id(config, params):
    endpoint = "/easm/{org_id}"+"/assets/subdomains/{0}".format(params.get("asset_id"))
    return get_multiple_records(config=config, endpoint=endpoint)


def get_asset_statistics(config, params):
    endpoint = "/easm/{org_id}/assets_statistics"
    return get_multiple_records(config=config, endpoint=endpoint, params=params)


def get_exposed_services(config, params):
    endpoint = "/easm/{org_id}/exposed_services"
    asset = params.pop('asset', '')
    if asset:
        endpoint += '/{0}'.format(asset)
    return get_multiple_records(config=config, endpoint=endpoint, params=params)


def get_cloud_integrations(config, params):
    endpoint = "/easm/{org_id}/cloud_integrations"
    for k in ['provider', 'connection_status']:
        if params.get(k):
            params[k] = params[k].lower()
    return get_multiple_records(config=config, endpoint=endpoint, params=params)


def get_fgt_integrations(config, params):
    endpoint = "/easm/{org_id}/fgt_integrations"
    if params.get('connection_status'):
        params['connection_status'] = params['connection_status'].lower()
    return get_multiple_records(config=config, endpoint=endpoint, params=params)


def get_security_insights(config, params):
    endpoint = "/easm/{org_id}/security_insights" + "/{0}/dns".format(params.get('domain'))
    return get_multiple_records(config=config, endpoint=endpoint)


def get_multiple_records(config, endpoint, params=None):
    MK = MakeRestApiCall(config=config)
    payload = MK.build_payload(params) if params else None
    response = MK.make_request(endpoint=endpoint, method="GET", params=payload)
    return response

# Update status actions

def update_archived_asset(config, params):
    MK = MakeRestApiCall(config=config)
    endpoint = "/easm/{org_id}"+"/archived_assets/{0}".format(params.pop("asset_id"))
    response = MK.make_request(endpoint=endpoint, method="PATCH", params=params)
    return response

def update_asn_asset_status_to_false_positive(config, params):
    MK = MakeRestApiCall(config=config)
    endpoint = "/easm/{org_id}"+"/assets/asns/{0}".format(params.pop("asset_id"))
    response = MK.make_request(endpoint=endpoint, method="PATCH", params=params)
    return response

def update_domain_asset_status_to_false_positive(config, params):
    MK = MakeRestApiCall(config=config)
    endpoint = "/easm/{org_id}"+"/assets/domains/{0}".format(params.pop("asset_id"))
    response = MK.make_request(endpoint=endpoint, method="PATCH", params=params)
    return response

def update_ip_asset_status_to_false_positive(config, params):
    MK = MakeRestApiCall(config=config)
    endpoint = "/easm/{org_id}"+"/assets/ips/{0}".format(params.pop("asset_id"))
    response = MK.make_request(endpoint=endpoint, method="PATCH", params=params)
    return response

def update_prefix_asset_status_to_false_positive(config, params):
    MK = MakeRestApiCall(config=config)
    endpoint = "/easm/{org_id}"+"/assets/prefixes/{0}".format(params.pop("asset_id"))
    response = MK.make_request(endpoint=endpoint, method="PATCH", params=params)
    return response

def update_subdomain_asset_status_to_false_positive(config, params):
    MK = MakeRestApiCall(config=config)
    endpoint = "/easm/{org_id}"+"/assets/subdomains/{0}".format(params.pop("asset_id"))
    response = MK.make_request(endpoint=endpoint, method="PATCH", params=params)
    return response
