"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""


from .scan_statistics import get_scan_statistics
from .issues import *
from .assets import *
from .breaches import get_breaches, get_breaches_by_id, get_leaked_credentials, update_leaked_credential_status
from .reports import generate_report, get_report

operations = {
    "get_leaked_credentials": get_leaked_credentials,
    "get_archived_issues": get_archived_issues,
    "get_issue_summary": get_issue_summary,
    "get_scan_statistics": get_scan_statistics,
    "get_issue_by_id": get_issue_by_id,
    "get_issues_discovered": get_issues_discovered,
    "get_asset_asns": get_asset_asns,
    "get_asns_by_asset_id": get_asns_by_asset_id,
    "get_domains": get_domains,
    "get_domain_by_asset_id": get_domains_by_asset_id,
    "get_ips": get_ips,
    "get_ips_by_asset_id": get_ips_by_asset_id,
    "get_prefixes": get_prefixes,
    "get_prefixes_by_asset_id": get_prefixes_by_asset_id,
    "get_subdomains": get_subdomains,
    "get_subdomain_by_asset_id": get_subdomains_by_asset_id,
    "get_asset_statistics": get_asset_statistics,
    "get_breaches": get_breaches,
    "get_breaches_by_id": get_breaches_by_id,
    "generate_report": generate_report,
    "get_report": get_report,
    "get_archived_assets": get_archived_assets,
    "get_exposed_services": get_exposed_services,
    "get_cloud_integrations": get_cloud_integrations,
    "get_fgt_integrations": get_fgt_integrations,
    "get_security_insights": get_security_insights,
    "get_archived_issue_comments": get_archived_issue_comments,
    "get_issue_comments": get_issue_comments,
    "get_tags": get_tags,
    "get_tag_by_id": get_tags,
    "get_groups": get_groups,
    "get_group_by_id": get_groups,
    "update_archived_issue": update_archived_issue,
    "update_issue_status": update_issue_status,
    "update_archived_asset": update_archived_asset,
    "update_asn_asset_status_to_false_positive": update_asn_asset_status_to_false_positive,
    "update_prefix_asset_status_to_false_positive": update_prefix_asset_status_to_false_positive,
    "update_ip_asset_status_to_false_positive": update_ip_asset_status_to_false_positive,
    "update_domain_asset_status_to_false_positive": update_domain_asset_status_to_false_positive,
    "update_subdomain_asset_status_to_false_positive": update_subdomain_asset_status_to_false_positive,
    "update_leaked_credential_status": update_leaked_credential_status
}
