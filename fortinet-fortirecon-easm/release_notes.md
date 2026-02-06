#### The following enhancements have been made to the Fortinet FortiRecon EASM Connector in version 1.2.1:

- Added a new query parameter `Show Plaintext Password` in the action `Get Leaked Credentials` 
- Added new query parameters `Recon Severity` and `NVD Severity` in the action `Get Issues Discovered`
- Updated the output schemas of following actions. Also added `Created Time` and `Modified Time` date-range filters to these actions:
    - Get Issues Discovered
    - Get Archived Issues
    - Get IPs
    - Get Domains
    - Get Subdomains
    - Get Prefixes
    - Get Asset ASNs
    - Get Exposed Services
    - Get Archived Assets
    - Get Cloud Integrations
    - Get FortiGate Integrations
    - Get Archived Issue Comments
    - Get Issue Comments
    - Get Tags
    - Get Groups
