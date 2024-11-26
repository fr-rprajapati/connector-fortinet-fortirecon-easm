"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""

STATUS_MAPPING = {
    "Active": "active",
    "False Positive": "false_positive",
    "Resolved": "resolved",
    "Risk Accepted": "risk_accepted",
    "Deleted": "deleted"
}

SEVERITY_MAPPING = {
    "Low": "low",
    "High": "high",
    "Medium": "medium",
    "Critical": "critical"
}

BUCKET_ID_MAPPING = {
    "Exposed Remote Service": "exposed_remote_service",
    "Vulnerable Software": "vulnerable_software",
    "Exposed Management Service": "exposed_management_service",
    "Certificate Issues": "certificate_issues",
    "DNS Health Email": "dns_health_(email)",
    "DNS Health": "dns_health",
    "Exposed Database Service": "exposed_database_service",
    "Reputation": "reputation",
    "MisConfiguration": "mis_configuration",
    "Missing Encryption": "missing_encryption",
    "Exposed Insecure Service": "exposed_insecure_service"
}

COMMA_SEPARATED_INPUT_PARAM = [
    'tags_in',
    'tags_match_all',
    'groups_in',
    'groups_match_all',
    'technologies',
    'countries',
    'services',
    'products',
    'issue_name_identifier'
]

ASSET_TYPE_MAPPING = {
    "IP Address": 'ip_address',
    "ASN Number": 'asn_number',
    "IP Prefix": 'ip_prefix',
    "Domain Name": 'domain_name',
    "Sub Domain": 'sub_domain'
}
SEARCH_TYPE_MAPPING = {
    "Exact": 'exact',
    "Begins with": 'begins_with',
    "Ends with": 'ends_with',
    "Wildcard": 'wildcard'
}


ISSUE_STATUS_MAPPING = {
       "ACTIVE": "active",
        "RESOLVED": "resolved",
        "FALSE_POSITIVE": "false_positive",
        "RISK_ACCEPTED": "risk_accepted"
}