# Edit the config_and_params.json file and add the necessary parameter values.
# Ensure that the provided input_params yield the correct output schema.
# Add logic for validating conditional_output_schema or if schema is other than dict.
# Add any specific assertions in each test case, based on the expected response.

"""
Copyright start
MIT License
Copyright (c) 2026 Fortinet Inc
Copyright end
"""

import pytest
from testframework.conftest import valid_configuration, invalid_configuration, valid_configuration_with_token,\
    connector_id, connector_details, info_json, params_json
from testframework.helpers.test_helpers import run_health_check_success, run_invalid_config_test, run_success_test,\
    run_output_schema_validation, run_invalid_param_test, set_report_metadata


def run_invalid_param_test_wrapper(connector_details, operation_name, param_name, param_type, action_params):
    result = run_invalid_param_test(connector_details, operation_name, param_name,
                                    param_type, action_params)
    assert result.get('data', {}).get('hits') == []
    assert result.get('status') == 'Success'


@pytest.mark.check_health
def test_check_health_success(valid_configuration, connector_details):
    set_report_metadata(connector_details, "Health Check", "Verify with valid Configuration")
    result = run_health_check_success(valid_configuration, connector_details)
    assert result.get('status') == 'Available'
    

@pytest.mark.check_health
def test_check_health_invalid_server_url(invalid_configuration, connector_id, connector_details, params_json):
    set_report_metadata(connector_details, "Health Check", "Verify with invalid Server URL")
    result = run_invalid_config_test(invalid_configuration, connector_id, connector_details, param_name='server_url',
                                     param_type='text', config=params_json['config'])
    assert result.get('status') == "Disconnected"
    

@pytest.mark.check_health
def test_check_health_invalid_api_key(invalid_configuration, connector_id, connector_details, params_json):
    set_report_metadata(connector_details, "Health Check", "Verify with invalid API Key")
    result = run_invalid_config_test(invalid_configuration, connector_id, connector_details, param_name='api_key',
                                     param_type='password', config=params_json['config'])
    assert result.get('status') == "Disconnected"
    

@pytest.mark.check_health
def test_check_health_invalid_org_id(invalid_configuration, connector_id, connector_details, params_json):
    set_report_metadata(connector_details, "Health Check", "Verify with invalid Organization ID")
    result = run_invalid_config_test(invalid_configuration, connector_id, connector_details, param_name='org_id',
                                     param_type='text', config=params_json['config'])
    assert result.get('status') == "Disconnected"
    

@pytest.mark.get_leaked_credentials
def test_get_leaked_credentials_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Leaked Credentials", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_leaked_credentials',
                                   action_params=params_json['get_leaked_credentials']):
        assert result.get('status') == "Success"


@pytest.mark.get_leaked_credentials
def test_validate_get_leaked_credentials_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Leaked Credentials", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_leaked_credentials', info_json, params_json['get_leaked_credentials'])
    

@pytest.mark.get_leaked_credentials
def test_get_leaked_credentials_invalid_breach_id(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Leaked Credentials", "Verify with invalid Breach ID")
    run_invalid_param_test_wrapper(connector_details, operation_name='get_leaked_credentials', param_name='breach_id',
                                    param_type='integer', action_params=params_json['get_leaked_credentials'])


@pytest.mark.get_leaked_credentials
def test_get_leaked_credentials_invalid_size(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Leaked Credentials", "Verify with invalid Size")
    result = run_invalid_param_test(connector_details, operation_name='get_leaked_credentials', param_name='size',
                                    param_type='integer', action_params=params_json['get_leaked_credentials'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_leaked_credentials
def test_get_leaked_credentials_invalid_q(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Leaked Credentials", "Verify with invalid Keyword")
    run_invalid_param_test_wrapper(connector_details, operation_name='get_leaked_credentials', param_name='q',
                                    param_type='text', action_params=params_json['get_leaked_credentials'])

@pytest.mark.get_leaked_credentials
def test_get_leaked_credentials_invalid_email(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Leaked Credentials", "Verify with invalid Email ID")
    run_invalid_param_test_wrapper(connector_details, operation_name='get_leaked_credentials', param_name='email',
                                    param_type='text', action_params=params_json['get_leaked_credentials'])
    
@pytest.mark.get_leaked_credentials
def test_get_leaked_credentials_invalid_domain(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Leaked Credentials", "Verify with invalid Domain")
    run_invalid_param_test_wrapper(connector_details, operation_name='get_leaked_credentials', param_name='domain',
                                    param_type='text', action_params=params_json['get_leaked_credentials'])

@pytest.mark.get_leaked_credentials
def test_get_leaked_credentials_invalid_page(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Leaked Credentials", "Verify with invalid Page")
    result = run_invalid_param_test(connector_details, operation_name='get_leaked_credentials', param_name='page',
                                    param_type='integer', action_params=params_json['get_leaked_credentials'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_scan_statistics
def test_get_scan_statistics_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Scan Statistics", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_scan_statistics',
                                   action_params=params_json['get_scan_statistics']):
        assert result.get('status') == "Success"


@pytest.mark.get_scan_statistics
def test_validate_get_scan_statistics_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Scan Statistics", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_scan_statistics', info_json, params_json['get_scan_statistics'])
    

@pytest.mark.get_scan_statistics
def test_get_scan_statistics_invalid_groups_match_all(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Scan Statistics", "Verify with invalid Groups In (Match All)")
    result = run_invalid_param_test(connector_details, operation_name='get_scan_statistics', param_name='groups_match_all',
                                    param_type='text', action_params=params_json['get_scan_statistics'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_scan_statistics
def test_get_scan_statistics_invalid_tags_in(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Scan Statistics", "Verify with invalid Tags In (Match Any)")
    result = run_invalid_param_test(connector_details, operation_name='get_scan_statistics', param_name='tags_in',
                                    param_type='text', action_params=params_json['get_scan_statistics'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_scan_statistics
def test_get_scan_statistics_invalid_groups_in(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Scan Statistics", "Verify with invalid Groups In (Match Any)")
    result = run_invalid_param_test(connector_details, operation_name='get_scan_statistics', param_name='groups_in',
                                    param_type='text', action_params=params_json['get_scan_statistics'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_scan_statistics
def test_get_scan_statistics_invalid_tags_match_all(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Scan Statistics", "Verify with invalid Tags In (Match All)")
    result = run_invalid_param_test(connector_details, operation_name='get_scan_statistics', param_name='tags_match_all',
                                    param_type='text', action_params=params_json['get_scan_statistics'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_issues_discovered
def test_get_issues_discovered_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Issues Discovered", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_issues_discovered',
                                   action_params=params_json['get_issues_discovered']):
        assert result.get('status') == "Success"


@pytest.mark.get_issues_discovered
def test_validate_get_issues_discovered_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Issues Discovered", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_issues_discovered', info_json, params_json['get_issues_discovered'])
    

@pytest.mark.get_issues_discovered
def test_get_issues_discovered_invalid_countries(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Issues Discovered", "Verify with invalid Countries")
    result = run_invalid_param_test(connector_details, operation_name='get_issues_discovered', param_name='countries',
                                    param_type='text', action_params=params_json['get_issues_discovered'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_issues_discovered
def test_get_issues_discovered_invalid_size(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Issues Discovered", "Verify with invalid Size")
    result = run_invalid_param_test(connector_details, operation_name='get_issues_discovered', param_name='size',
                                    param_type='integer', action_params=params_json['get_issues_discovered'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_issues_discovered
def test_get_issues_discovered_invalid_issue_name_identifier(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Issues Discovered", "Verify with invalid Issue Name Identifier")
    run_invalid_param_test_wrapper(connector_details, operation_name='get_issues_discovered', param_name='issue_name_identifier',
                                    param_type='text', action_params=params_json['get_issues_discovered'])

@pytest.mark.get_issues_discovered
def test_get_issues_discovered_invalid_groups_in(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Issues Discovered", "Verify with invalid Groups In (Match Any)")
    result = run_invalid_param_test(connector_details, operation_name='get_issues_discovered', param_name='groups_in',
                                    param_type='text', action_params=params_json['get_issues_discovered'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_issues_discovered
def test_get_issues_discovered_invalid_groups_match_all(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Issues Discovered", "Verify with invalid Groups In (Match All)")
    result = run_invalid_param_test(connector_details, operation_name='get_issues_discovered', param_name='groups_match_all',
                                    param_type='text', action_params=params_json['get_issues_discovered'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_issues_discovered
def test_get_issues_discovered_invalid_page(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Issues Discovered", "Verify with invalid Page")
    result = run_invalid_param_test(connector_details, operation_name='get_issues_discovered', param_name='page',
                                    param_type='integer', action_params=params_json['get_issues_discovered'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_issues_discovered
def test_get_issues_discovered_invalid_tags_in(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Issues Discovered", "Verify with invalid Tags In (Match Any)")
    result = run_invalid_param_test(connector_details, operation_name='get_issues_discovered', param_name='tags_in',
                                    param_type='text', action_params=params_json['get_issues_discovered'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_issues_discovered
def test_get_issues_discovered_invalid_asset(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Issues Discovered", "Verify with invalid Asset")
    run_invalid_param_test_wrapper(connector_details, operation_name='get_issues_discovered', param_name='asset',
                                    param_type='text', action_params=params_json['get_issues_discovered'])

@pytest.mark.get_issues_discovered
def test_get_issues_discovered_invalid_tags_match_all(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Issues Discovered", "Verify with invalid Tags In (Match All)")
    result = run_invalid_param_test(connector_details, operation_name='get_issues_discovered', param_name='tags_match_all',
                                    param_type='text', action_params=params_json['get_issues_discovered'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_issue_by_id
def test_get_issue_by_id_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Issue By ID", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_issue_by_id',
                                   action_params=params_json['get_issue_by_id']):
        assert result.get('status') == "Success"


@pytest.mark.get_issue_by_id
def test_validate_get_issue_by_id_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Issue By ID", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_issue_by_id', info_json, params_json['get_issue_by_id'])
    

@pytest.mark.get_issue_by_id
def test_get_issue_by_id_invalid_issue_id(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Issue By ID", "Verify with invalid Issue ID")
    result = run_invalid_param_test(connector_details, operation_name='get_issue_by_id', param_name='issue_id',
                                    param_type='text', action_params=params_json['get_issue_by_id'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_issue_summary
def test_get_issue_summary_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Issue Summary", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_issue_summary',
                                   action_params=params_json['get_issue_summary']):
        assert result.get('status') == "Success"


@pytest.mark.get_issue_summary
def test_validate_get_issue_summary_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Issue Summary", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_issue_summary', info_json, params_json['get_issue_summary'])
    

@pytest.mark.get_issue_summary
def test_get_issue_summary_invalid_groups_match_all(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Issue Summary", "Verify with invalid Groups In (Match All)")
    result = run_invalid_param_test(connector_details, operation_name='get_issue_summary', param_name='groups_match_all',
                                    param_type='text', action_params=params_json['get_issue_summary'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_issue_summary
def test_get_issue_summary_invalid_groups_in(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Issue Summary", "Verify with invalid Groups In (Match Any)")
    result = run_invalid_param_test(connector_details, operation_name='get_issue_summary', param_name='groups_in',
                                    param_type='text', action_params=params_json['get_issue_summary'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_issue_summary
def test_get_issue_summary_invalid_tags_in(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Issue Summary", "Verify with invalid Tags In (Match Any)")
    result = run_invalid_param_test(connector_details, operation_name='get_issue_summary', param_name='tags_in',
                                    param_type='text', action_params=params_json['get_issue_summary'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_issue_summary
def test_get_issue_summary_invalid_tags_match_all(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Issue Summary", "Verify with invalid Tags In (Match All)")
    result = run_invalid_param_test(connector_details, operation_name='get_issue_summary', param_name='tags_match_all',
                                    param_type='text', action_params=params_json['get_issue_summary'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_archived_issues
def test_get_archived_issues_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Archived Issues", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_archived_issues',
                                   action_params=params_json['get_archived_issues']):
        assert result.get('status') == "Success"


@pytest.mark.get_archived_issues
def test_validate_get_archived_issues_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Archived Issues", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_archived_issues', info_json, params_json['get_archived_issues'])
    

@pytest.mark.get_archived_issues
def test_get_archived_issues_invalid_size(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Archived Issues", "Verify with invalid Size")
    result = run_invalid_param_test(connector_details, operation_name='get_archived_issues', param_name='size',
                                    param_type='integer', action_params=params_json['get_archived_issues'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_archived_issues
def test_get_archived_issues_invalid_groups_in(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Archived Issues", "Verify with invalid Groups In (Match Any)")
    result = run_invalid_param_test(connector_details, operation_name='get_archived_issues', param_name='groups_in',
                                    param_type='text', action_params=params_json['get_archived_issues'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_archived_issues
def test_get_archived_issues_invalid_groups_match_all(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Archived Issues", "Verify with invalid Groups In (Match All)")
    result = run_invalid_param_test(connector_details, operation_name='get_archived_issues', param_name='groups_match_all',
                                    param_type='text', action_params=params_json['get_archived_issues'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_archived_issues
def test_get_archived_issues_invalid_page(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Archived Issues", "Verify with invalid Page")
    result = run_invalid_param_test(connector_details, operation_name='get_archived_issues', param_name='page',
                                    param_type='integer', action_params=params_json['get_archived_issues'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_archived_issues
def test_get_archived_issues_invalid_tags_in(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Archived Issues", "Verify with invalid Tags In (Match Any)")
    result = run_invalid_param_test(connector_details, operation_name='get_archived_issues', param_name='tags_in',
                                    param_type='text', action_params=params_json['get_archived_issues'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_archived_issues
def test_get_archived_issues_invalid_asset(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Archived Issues", "Verify with invalid Asset")
    result = run_invalid_param_test(connector_details, operation_name='get_archived_issues', param_name='asset',
                                    param_type='text', action_params=params_json['get_archived_issues'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_archived_issues
def test_get_archived_issues_invalid_tags_match_all(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Archived Issues", "Verify with invalid Tags In (Match All)")
    result = run_invalid_param_test(connector_details, operation_name='get_archived_issues', param_name='tags_match_all',
                                    param_type='text', action_params=params_json['get_archived_issues'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_archived_assets
def test_get_archived_assets_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Archived Assets", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_archived_assets',
                                   action_params=params_json['get_archived_assets']):
        assert result.get('status') == "Success"


@pytest.mark.get_archived_assets
def test_validate_get_archived_assets_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Archived Assets", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_archived_assets', info_json, params_json['get_archived_assets'])
    

@pytest.mark.get_archived_assets
def test_get_archived_assets_invalid_size(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Archived Assets", "Verify with invalid Size")
    result = run_invalid_param_test(connector_details, operation_name='get_archived_assets', param_name='size',
                                    param_type='integer', action_params=params_json['get_archived_assets'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_archived_assets
def test_get_archived_assets_invalid_groups_in(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Archived Assets", "Verify with invalid Groups In (Match Any)")
    result = run_invalid_param_test(connector_details, operation_name='get_archived_assets', param_name='groups_in',
                                    param_type='text', action_params=params_json['get_archived_assets'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_archived_assets
def test_get_archived_assets_invalid_groups_match_all(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Archived Assets", "Verify with invalid Groups In (Match All)")
    result = run_invalid_param_test(connector_details, operation_name='get_archived_assets', param_name='groups_match_all',
                                    param_type='text', action_params=params_json['get_archived_assets'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_archived_assets
def test_get_archived_assets_invalid_page(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Archived Assets", "Verify with invalid Page")
    result = run_invalid_param_test(connector_details, operation_name='get_archived_assets', param_name='page',
                                    param_type='integer', action_params=params_json['get_archived_assets'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_archived_assets
def test_get_archived_assets_invalid_tags_in(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Archived Assets", "Verify with invalid Tags In (Match Any)")
    result = run_invalid_param_test(connector_details, operation_name='get_archived_assets', param_name='tags_in',
                                    param_type='text', action_params=params_json['get_archived_assets'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_archived_assets
def test_get_archived_assets_invalid_asset(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Archived Assets", "Verify with invalid Asset")
    result = run_invalid_param_test(connector_details, operation_name='get_archived_assets', param_name='asset',
                                    param_type='text', action_params=params_json['get_archived_assets'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_archived_assets
def test_get_archived_assets_invalid_tags_match_all(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Archived Assets", "Verify with invalid Tags In (Match All)")
    result = run_invalid_param_test(connector_details, operation_name='get_archived_assets', param_name='tags_match_all',
                                    param_type='text', action_params=params_json['get_archived_assets'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_asset_asns
def test_get_asset_asns_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Asset ASNs", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_asset_asns',
                                   action_params=params_json['get_asset_asns']):
        assert result.get('status') == "Success"


@pytest.mark.get_asset_asns
def test_validate_get_asset_asns_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Asset ASNs", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_asset_asns', info_json, params_json['get_asset_asns'])
    

@pytest.mark.get_asset_asns
def test_get_asset_asns_invalid_cloud_metadata(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Asset ASNs", "Verify with invalid Cloud Metadata")
    result = run_invalid_param_test(connector_details, operation_name='get_asset_asns', param_name='cloud_metadata',
                                    param_type='json', action_params=params_json['get_asset_asns'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_asset_asns
def test_get_asset_asns_invalid_size(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Asset ASNs", "Verify with invalid Size")
    result = run_invalid_param_test(connector_details, operation_name='get_asset_asns', param_name='size',
                                    param_type='integer', action_params=params_json['get_asset_asns'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_asset_asns
def test_get_asset_asns_invalid_groups_in(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Asset ASNs", "Verify with invalid Groups In (Match Any)")
    result = run_invalid_param_test(connector_details, operation_name='get_asset_asns', param_name='groups_in',
                                    param_type='text', action_params=params_json['get_asset_asns'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_asset_asns
def test_get_asset_asns_invalid_groups_match_all(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Asset ASNs", "Verify with invalid Groups In (Match All)")
    result = run_invalid_param_test(connector_details, operation_name='get_asset_asns', param_name='groups_match_all',
                                    param_type='text', action_params=params_json['get_asset_asns'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_asset_asns
def test_get_asset_asns_invalid_page(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Asset ASNs", "Verify with invalid Page")
    result = run_invalid_param_test(connector_details, operation_name='get_asset_asns', param_name='page',
                                    param_type='integer', action_params=params_json['get_asset_asns'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_asset_asns
def test_get_asset_asns_invalid_tags_in(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Asset ASNs", "Verify with invalid Tags In (Match Any)")
    result = run_invalid_param_test(connector_details, operation_name='get_asset_asns', param_name='tags_in',
                                    param_type='text', action_params=params_json['get_asset_asns'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_asset_asns
def test_get_asset_asns_invalid_asset(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Asset ASNs", "Verify with invalid Asset")
    result = run_invalid_param_test(connector_details, operation_name='get_asset_asns', param_name='asset',
                                    param_type='text', action_params=params_json['get_asset_asns'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_asset_asns
def test_get_asset_asns_invalid_tags_match_all(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Asset ASNs", "Verify with invalid Tags In (Match All)")
    result = run_invalid_param_test(connector_details, operation_name='get_asset_asns', param_name='tags_match_all',
                                    param_type='text', action_params=params_json['get_asset_asns'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_asns_by_asset_id
def test_get_asns_by_asset_id_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get ASNs by Asset ID", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_asns_by_asset_id',
                                   action_params=params_json['get_asns_by_asset_id']):
        assert result.get('status') == "Success"


@pytest.mark.get_asns_by_asset_id
def test_validate_get_asns_by_asset_id_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get ASNs by Asset ID", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_asns_by_asset_id', info_json, params_json['get_asns_by_asset_id'])
    

@pytest.mark.get_asns_by_asset_id
def test_get_asns_by_asset_id_invalid_asset_id(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get ASNs by Asset ID", "Verify with invalid Asset ID")
    result = run_invalid_param_test(connector_details, operation_name='get_asns_by_asset_id', param_name='asset_id',
                                    param_type='text', action_params=params_json['get_asns_by_asset_id'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_domains
def test_get_domains_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Domains", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_domains',
                                   action_params=params_json['get_domains']):
        assert result.get('status') == "Success"


@pytest.mark.get_domains
def test_validate_get_domains_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Domains", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_domains', info_json, params_json['get_domains'])
    

@pytest.mark.get_domains
def test_get_domains_invalid_cloud_metadata(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Domains", "Verify with invalid Cloud Metadata")
    result = run_invalid_param_test(connector_details, operation_name='get_domains', param_name='cloud_metadata',
                                    param_type='json', action_params=params_json['get_domains'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_domains
def test_get_domains_invalid_ports(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Domains", "Verify with invalid Ports")
    result = run_invalid_param_test(connector_details, operation_name='get_domains', param_name='ports',
                                    param_type='text', action_params=params_json['get_domains'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_domains
def test_get_domains_invalid_size(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Domains", "Verify with invalid Size")
    result = run_invalid_param_test(connector_details, operation_name='get_domains', param_name='size',
                                    param_type='integer', action_params=params_json['get_domains'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_domains
def test_get_domains_invalid_groups_in(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Domains", "Verify with invalid Groups In (Match Any)")
    result = run_invalid_param_test(connector_details, operation_name='get_domains', param_name='groups_in',
                                    param_type='text', action_params=params_json['get_domains'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_domains
def test_get_domains_invalid_groups_match_all(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Domains", "Verify with invalid Groups In (Match All)")
    result = run_invalid_param_test(connector_details, operation_name='get_domains', param_name='groups_match_all',
                                    param_type='text', action_params=params_json['get_domains'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_domains
def test_get_domains_invalid_page(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Domains", "Verify with invalid Page")
    result = run_invalid_param_test(connector_details, operation_name='get_domains', param_name='page',
                                    param_type='integer', action_params=params_json['get_domains'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_domains
def test_get_domains_invalid_tags_in(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Domains", "Verify with invalid Tags In (Match Any)")
    result = run_invalid_param_test(connector_details, operation_name='get_domains', param_name='tags_in',
                                    param_type='text', action_params=params_json['get_domains'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_domains
def test_get_domains_invalid_asset(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Domains", "Verify with invalid Asset")
    result = run_invalid_param_test(connector_details, operation_name='get_domains', param_name='asset',
                                    param_type='text', action_params=params_json['get_domains'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_domains
def test_get_domains_invalid_technologies(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Domains", "Verify with invalid Technologies")
    run_invalid_param_test_wrapper(connector_details, operation_name='get_domains', param_name='technologies',
                                    param_type='text', action_params=params_json['get_domains'])

@pytest.mark.get_domains
def test_get_domains_invalid_tags_match_all(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Domains", "Verify with invalid Tags In (Match All)")
    result = run_invalid_param_test(connector_details, operation_name='get_domains', param_name='tags_match_all',
                                    param_type='text', action_params=params_json['get_domains'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_domain_by_asset_id
def test_get_domain_by_asset_id_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Domain by Asset ID", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_domain_by_asset_id',
                                   action_params=params_json['get_domain_by_asset_id']):
        assert result.get('status') == "Success"


@pytest.mark.get_domain_by_asset_id
def test_validate_get_domain_by_asset_id_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Domain by Asset ID", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_domain_by_asset_id', info_json, params_json['get_domain_by_asset_id'])
    

@pytest.mark.get_domain_by_asset_id
def test_get_domain_by_asset_id_invalid_asset_id(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Domain by Asset ID", "Verify with invalid Asset ID")
    result = run_invalid_param_test(connector_details, operation_name='get_domain_by_asset_id', param_name='asset_id',
                                    param_type='text', action_params=params_json['get_domain_by_asset_id'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_ips
def test_get_ips_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get IPs", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_ips',
                                   action_params=params_json['get_ips']):
        assert result.get('status') == "Success"


@pytest.mark.get_ips
def test_validate_get_ips_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get IPs", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_ips', info_json, params_json['get_ips'])
    

@pytest.mark.get_ips
def test_get_ips_invalid_ip_prefix(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get IPs", "Verify with invalid IP Prefix")
    result = run_invalid_param_test(connector_details, operation_name='get_ips', param_name='ip_prefix',
                                    param_type='text', action_params=params_json['get_ips'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_ips
def test_get_ips_invalid_countries(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get IPs", "Verify with invalid Countries")
    result = run_invalid_param_test(connector_details, operation_name='get_ips', param_name='countries',
                                    param_type='text', action_params=params_json['get_ips'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_ips
def test_get_ips_invalid_cloud_metadata(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get IPs", "Verify with invalid Cloud Metadata")
    result = run_invalid_param_test(connector_details, operation_name='get_ips', param_name='cloud_metadata',
                                    param_type='json', action_params=params_json['get_ips'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_ips
def test_get_ips_invalid_ports(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get IPs", "Verify with invalid Ports")
    result = run_invalid_param_test(connector_details, operation_name='get_ips', param_name='ports',
                                    param_type='text', action_params=params_json['get_ips'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_ips
def test_get_ips_invalid_size(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get IPs", "Verify with invalid Size")
    result = run_invalid_param_test(connector_details, operation_name='get_ips', param_name='size',
                                    param_type='integer', action_params=params_json['get_ips'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_ips
def test_get_ips_invalid_groups_in(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get IPs", "Verify with invalid Groups In (Match Any)")
    result = run_invalid_param_test(connector_details, operation_name='get_ips', param_name='groups_in',
                                    param_type='text', action_params=params_json['get_ips'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_ips
def test_get_ips_invalid_groups_match_all(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get IPs", "Verify with invalid Groups In (Match All)")
    result = run_invalid_param_test(connector_details, operation_name='get_ips', param_name='groups_match_all',
                                    param_type='text', action_params=params_json['get_ips'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_ips
def test_get_ips_invalid_page(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get IPs", "Verify with invalid Page")
    result = run_invalid_param_test(connector_details, operation_name='get_ips', param_name='page',
                                    param_type='integer', action_params=params_json['get_ips'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_ips
def test_get_ips_invalid_tags_in(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get IPs", "Verify with invalid Tags In (Match Any)")
    result = run_invalid_param_test(connector_details, operation_name='get_ips', param_name='tags_in',
                                    param_type='text', action_params=params_json['get_ips'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_ips
def test_get_ips_invalid_asset(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get IPs", "Verify with invalid Asset")
    result = run_invalid_param_test(connector_details, operation_name='get_ips', param_name='asset',
                                    param_type='text', action_params=params_json['get_ips'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_ips
def test_get_ips_invalid_tags_match_all(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get IPs", "Verify with invalid Tags In (Match All)")
    result = run_invalid_param_test(connector_details, operation_name='get_ips', param_name='tags_match_all',
                                    param_type='text', action_params=params_json['get_ips'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_ips_by_asset_id
def test_get_ips_by_asset_id_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get IP by Asset ID", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_ips_by_asset_id',
                                   action_params=params_json['get_ips_by_asset_id']):
        assert result.get('status') == "Success"


@pytest.mark.get_ips_by_asset_id
def test_validate_get_ips_by_asset_id_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get IP by Asset ID", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_ips_by_asset_id', info_json, params_json['get_ips_by_asset_id'])
    

@pytest.mark.get_ips_by_asset_id
def test_get_ips_by_asset_id_invalid_asset_id(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get IP by Asset ID", "Verify with invalid Asset ID")
    result = run_invalid_param_test(connector_details, operation_name='get_ips_by_asset_id', param_name='asset_id',
                                    param_type='text', action_params=params_json['get_ips_by_asset_id'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_prefixes
def test_get_prefixes_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Prefixes", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_prefixes',
                                   action_params=params_json['get_prefixes']):
        assert result.get('status') == "Success"


@pytest.mark.get_prefixes
def test_validate_get_prefixes_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Prefixes", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_prefixes', info_json, params_json['get_prefixes'])
    

@pytest.mark.get_prefixes
def test_get_prefixes_invalid_cloud_metadata(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Prefixes", "Verify with invalid Cloud Metadata")
    result = run_invalid_param_test(connector_details, operation_name='get_prefixes', param_name='cloud_metadata',
                                    param_type='json', action_params=params_json['get_prefixes'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_prefixes
def test_get_prefixes_invalid_size(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Prefixes", "Verify with invalid Size")
    result = run_invalid_param_test(connector_details, operation_name='get_prefixes', param_name='size',
                                    param_type='integer', action_params=params_json['get_prefixes'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_prefixes
def test_get_prefixes_invalid_groups_in(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Prefixes", "Verify with invalid Groups In (Match Any)")
    result = run_invalid_param_test(connector_details, operation_name='get_prefixes', param_name='groups_in',
                                    param_type='text', action_params=params_json['get_prefixes'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_prefixes
def test_get_prefixes_invalid_groups_match_all(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Prefixes", "Verify with invalid Groups In (Match All)")
    result = run_invalid_param_test(connector_details, operation_name='get_prefixes', param_name='groups_match_all',
                                    param_type='text', action_params=params_json['get_prefixes'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_prefixes
def test_get_prefixes_invalid_asn(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Prefixes", "Verify with invalid ASN")
    run_invalid_param_test_wrapper(connector_details, operation_name='get_prefixes', param_name='asn',
                                    param_type='text', action_params=params_json['get_prefixes'])

@pytest.mark.get_prefixes
def test_get_prefixes_invalid_tags_in(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Prefixes", "Verify with invalid Tags In (Match Any)")
    result = run_invalid_param_test(connector_details, operation_name='get_prefixes', param_name='tags_in',
                                    param_type='text', action_params=params_json['get_prefixes'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_prefixes
def test_get_prefixes_invalid_page(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Prefixes", "Verify with invalid Page")
    result = run_invalid_param_test(connector_details, operation_name='get_prefixes', param_name='page',
                                    param_type='integer', action_params=params_json['get_prefixes'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_prefixes
def test_get_prefixes_invalid_asset(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Prefixes", "Verify with invalid Asset")
    result = run_invalid_param_test(connector_details, operation_name='get_prefixes', param_name='asset',
                                    param_type='text', action_params=params_json['get_prefixes'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_prefixes
def test_get_prefixes_invalid_tags_match_all(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Prefixes", "Verify with invalid Tags In (Match All)")
    result = run_invalid_param_test(connector_details, operation_name='get_prefixes', param_name='tags_match_all',
                                    param_type='text', action_params=params_json['get_prefixes'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_prefixes_by_asset_id
def test_get_prefixes_by_asset_id_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Prefixes by Asset ID", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_prefixes_by_asset_id',
                                   action_params=params_json['get_prefixes_by_asset_id']):
        assert result.get('status') == "Success"


@pytest.mark.get_prefixes_by_asset_id
def test_validate_get_prefixes_by_asset_id_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Prefixes by Asset ID", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_prefixes_by_asset_id', info_json, params_json['get_prefixes_by_asset_id'])
    

@pytest.mark.get_prefixes_by_asset_id
def test_get_prefixes_by_asset_id_invalid_asset_id(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Prefixes by Asset ID", "Verify with invalid Asset ID")
    result = run_invalid_param_test(connector_details, operation_name='get_prefixes_by_asset_id', param_name='asset_id',
                                    param_type='text', action_params=params_json['get_prefixes_by_asset_id'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_subdomains
def test_get_subdomains_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Subdomains", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_subdomains',
                                   action_params=params_json['get_subdomains']):
        assert result.get('status') == "Success"


@pytest.mark.get_subdomains
def test_validate_get_subdomains_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Subdomains", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_subdomains', info_json, params_json['get_subdomains'])
    

@pytest.mark.get_subdomains
def test_get_subdomains_invalid_cloud_metadata(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Subdomains", "Verify with invalid Cloud Metadata")
    result = run_invalid_param_test(connector_details, operation_name='get_subdomains', param_name='cloud_metadata',
                                    param_type='json', action_params=params_json['get_subdomains'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_subdomains
def test_get_subdomains_invalid_ports(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Subdomains", "Verify with invalid Ports")
    result = run_invalid_param_test(connector_details, operation_name='get_subdomains', param_name='ports',
                                    param_type='text', action_params=params_json['get_subdomains'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_subdomains
def test_get_subdomains_invalid_size(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Subdomains", "Verify with invalid Size")
    result = run_invalid_param_test(connector_details, operation_name='get_subdomains', param_name='size',
                                    param_type='integer', action_params=params_json['get_subdomains'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_subdomains
def test_get_subdomains_invalid_domain(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Subdomains", "Verify with invalid Domain")
    run_invalid_param_test_wrapper(connector_details, operation_name='get_subdomains', param_name='domain',
                                    param_type='text', action_params=params_json['get_subdomains'])

@pytest.mark.get_subdomains
def test_get_subdomains_invalid_groups_in(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Subdomains", "Verify with invalid Groups In (Match Any)")
    result = run_invalid_param_test(connector_details, operation_name='get_subdomains', param_name='groups_in',
                                    param_type='text', action_params=params_json['get_subdomains'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_subdomains
def test_get_subdomains_invalid_groups_match_all(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Subdomains", "Verify with invalid Groups In (Match All)")
    result = run_invalid_param_test(connector_details, operation_name='get_subdomains', param_name='groups_match_all',
                                    param_type='text', action_params=params_json['get_subdomains'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_subdomains
def test_get_subdomains_invalid_page(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Subdomains", "Verify with invalid Page")
    result = run_invalid_param_test(connector_details, operation_name='get_subdomains', param_name='page',
                                    param_type='integer', action_params=params_json['get_subdomains'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_subdomains
def test_get_subdomains_invalid_tags_in(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Subdomains", "Verify with invalid Tags In (Match Any)")
    result = run_invalid_param_test(connector_details, operation_name='get_subdomains', param_name='tags_in',
                                    param_type='text', action_params=params_json['get_subdomains'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_subdomains
def test_get_subdomains_invalid_asset(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Subdomains", "Verify with invalid Asset")
    run_invalid_param_test_wrapper(connector_details, operation_name='get_subdomains', param_name='asset',
                                    param_type='text', action_params=params_json['get_subdomains'])

@pytest.mark.get_subdomains
def test_get_subdomains_invalid_technologies(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Subdomains", "Verify with invalid Technologies")
    run_invalid_param_test_wrapper(connector_details, operation_name='get_subdomains', param_name='technologies',
                                    param_type='text', action_params=params_json['get_subdomains'])

@pytest.mark.get_subdomains
def test_get_subdomains_invalid_tags_match_all(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Subdomains", "Verify with invalid Tags In (Match All)")
    result = run_invalid_param_test(connector_details, operation_name='get_subdomains', param_name='tags_match_all',
                                    param_type='text', action_params=params_json['get_subdomains'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_subdomain_by_asset_id
def test_get_subdomain_by_asset_id_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Subdomain by Asset ID", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_subdomain_by_asset_id',
                                   action_params=params_json['get_subdomain_by_asset_id']):
        assert result.get('status') == "Success"


@pytest.mark.get_subdomain_by_asset_id
def test_validate_get_subdomain_by_asset_id_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Subdomain by Asset ID", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_subdomain_by_asset_id', info_json, params_json['get_subdomain_by_asset_id'])
    

@pytest.mark.get_subdomain_by_asset_id
def test_get_subdomain_by_asset_id_invalid_asset_id(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Subdomain by Asset ID", "Verify with invalid Asset ID")
    result = run_invalid_param_test(connector_details, operation_name='get_subdomain_by_asset_id', param_name='asset_id',
                                    param_type='text', action_params=params_json['get_subdomain_by_asset_id'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_asset_statistics
def test_get_asset_statistics_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Asset Statistics", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_asset_statistics',
                                   action_params=params_json['get_asset_statistics']):
        assert result.get('status') == "Success"


@pytest.mark.get_asset_statistics
def test_validate_get_asset_statistics_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Asset Statistics", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_asset_statistics', info_json, params_json['get_asset_statistics'])
    

@pytest.mark.get_asset_statistics
def test_get_asset_statistics_invalid_countries(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Asset Statistics", "Verify with invalid Countries")
    result = run_invalid_param_test(connector_details, operation_name='get_asset_statistics', param_name='countries',
                                    param_type='text', action_params=params_json['get_asset_statistics'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_asset_statistics
def test_get_asset_statistics_invalid_ports(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Asset Statistics", "Verify with invalid Ports")
    result = run_invalid_param_test(connector_details, operation_name='get_asset_statistics', param_name='ports',
                                    param_type='text', action_params=params_json['get_asset_statistics'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_asset_statistics
def test_get_asset_statistics_invalid_groups_in(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Asset Statistics", "Verify with invalid Groups In (Match Any)")
    result = run_invalid_param_test(connector_details, operation_name='get_asset_statistics', param_name='groups_in',
                                    param_type='text', action_params=params_json['get_asset_statistics'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_asset_statistics
def test_get_asset_statistics_invalid_groups_match_all(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Asset Statistics", "Verify with invalid Groups In (Match All)")
    result = run_invalid_param_test(connector_details, operation_name='get_asset_statistics', param_name='groups_match_all',
                                    param_type='text', action_params=params_json['get_asset_statistics'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_asset_statistics
def test_get_asset_statistics_invalid_tags_in(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Asset Statistics", "Verify with invalid Tags In (Match Any)")
    result = run_invalid_param_test(connector_details, operation_name='get_asset_statistics', param_name='tags_in',
                                    param_type='text', action_params=params_json['get_asset_statistics'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_asset_statistics
def test_get_asset_statistics_invalid_technologies(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Asset Statistics", "Verify with invalid Technologies")
    result = run_invalid_param_test(connector_details, operation_name='get_asset_statistics', param_name='technologies',
                                    param_type='text', action_params=params_json['get_asset_statistics'])
    assert result.get('status') == 'Success'

@pytest.mark.get_asset_statistics
def test_get_asset_statistics_invalid_tags_match_all(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Asset Statistics", "Verify with invalid Tags In (Match All)")
    result = run_invalid_param_test(connector_details, operation_name='get_asset_statistics', param_name='tags_match_all',
                                    param_type='text', action_params=params_json['get_asset_statistics'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_breaches
def test_get_breaches_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Breaches", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_breaches',
                                   action_params=params_json['get_breaches']):
        assert result.get('status') == "Success"


@pytest.mark.get_breaches
def test_validate_get_breaches_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Breaches", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_breaches', info_json, params_json['get_breaches'])
    

@pytest.mark.get_breaches
def test_get_breaches_invalid_size(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Breaches", "Verify with invalid Size")
    result = run_invalid_param_test(connector_details, operation_name='get_breaches', param_name='size',
                                    param_type='integer', action_params=params_json['get_breaches'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_breaches
def test_get_breaches_invalid_q(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Breaches", "Verify with invalid Keyword")
    run_invalid_param_test_wrapper(connector_details, operation_name='get_breaches', param_name='q',
                                    param_type='text', action_params=params_json['get_breaches'])

@pytest.mark.get_breaches
def test_get_breaches_invalid_page(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Breaches", "Verify with invalid Page")
    result = run_invalid_param_test(connector_details, operation_name='get_breaches', param_name='page',
                                    param_type='integer', action_params=params_json['get_breaches'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_breaches
def test_get_breaches_invalid_name(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Breaches", "Verify with invalid Breach Name")
    run_invalid_param_test_wrapper(connector_details, operation_name='get_breaches', param_name='name',
                                    param_type='text', action_params=params_json['get_breaches'])

@pytest.mark.get_breaches_by_id
def test_get_breaches_by_id_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Breaches by ID", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_breaches_by_id',
                                   action_params=params_json['get_breaches_by_id']):
        assert result.get('status') == "Success"


@pytest.mark.get_breaches_by_id
def test_validate_get_breaches_by_id_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Breaches by ID", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_breaches_by_id', info_json, params_json['get_breaches_by_id'])
    

@pytest.mark.get_breaches_by_id
def test_get_breaches_by_id_invalid_breach_id(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Breaches by ID", "Verify with invalid Breach ID")
    result = run_invalid_param_test(connector_details, operation_name='get_breaches_by_id', param_name='breach_id',
                                    param_type='text', action_params=params_json['get_breaches_by_id'])
    assert result.get('status') == "failed"
    

@pytest.mark.generate_report
def test_generate_report_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Generate Report", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='generate_report',
                                   action_params=params_json['generate_report']):
        assert result.get('status') == "Success"


@pytest.mark.generate_report
def test_validate_generate_report_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Generate Report", "Validate Output Schema")
    run_output_schema_validation(cache, 'generate_report', info_json, params_json['generate_report'])
    

@pytest.mark.generate_report
def test_generate_report_invalid_groups_match_all(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Generate Report", "Verify with invalid Groups In (Match All)")
    result = run_invalid_param_test(connector_details, operation_name='generate_report', param_name='groups_match_all',
                                    param_type='text', action_params=params_json['generate_report'])
    assert result.get('status') == "failed"
    

@pytest.mark.generate_report
def test_generate_report_invalid_tags_in(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Generate Report", "Verify with invalid Tags In (Match Any)")
    result = run_invalid_param_test(connector_details, operation_name='generate_report', param_name='tags_in',
                                    param_type='text', action_params=params_json['generate_report'])
    assert result.get('status') == "failed"
    

@pytest.mark.generate_report
def test_generate_report_invalid_groups_in(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Generate Report", "Verify with invalid Groups In (Match Any)")
    result = run_invalid_param_test(connector_details, operation_name='generate_report', param_name='groups_in',
                                    param_type='text', action_params=params_json['generate_report'])
    assert result.get('status') == "failed"
    

@pytest.mark.generate_report
def test_generate_report_invalid_tags_match_all(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Generate Report", "Verify with invalid Tags In (Match All)")
    result = run_invalid_param_test(connector_details, operation_name='generate_report', param_name='tags_match_all',
                                    param_type='text', action_params=params_json['generate_report'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_report
def test_get_report_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Report", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_report',
                                   action_params=params_json['get_report']):
        assert result.get('status') == "Success"


@pytest.mark.get_report
def test_validate_get_report_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Report", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_report', info_json, params_json['get_report'])
    

@pytest.mark.get_report
def test_get_report_invalid_report_id(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Report", "Verify with invalid Report ID")
    result = run_invalid_param_test(connector_details, operation_name='get_report', param_name='report_id',
                                    param_type='text', action_params=params_json['get_report'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_exposed_services
def test_get_exposed_services_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Exposed Services", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_exposed_services',
                                   action_params=params_json['get_exposed_services']):
        assert result.get('status') == "Success"


@pytest.mark.get_exposed_services
def test_validate_get_exposed_services_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Exposed Services", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_exposed_services', info_json, params_json['get_exposed_services'])
    

@pytest.mark.get_exposed_services
def test_get_exposed_services_invalid_size(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Exposed Services", "Verify with invalid Size")
    result = run_invalid_param_test(connector_details, operation_name='get_exposed_services', param_name='size',
                                    param_type='integer', action_params=params_json['get_exposed_services'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_exposed_services
def test_get_exposed_services_invalid_ports(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Exposed Services", "Verify with invalid Ports")
    result = run_invalid_param_test(connector_details, operation_name='get_exposed_services', param_name='ports',
                                    param_type='text', action_params=params_json['get_exposed_services'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_exposed_services
def test_get_exposed_services_invalid_services(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Exposed Services", "Verify with invalid Services")
    run_invalid_param_test_wrapper(connector_details, operation_name='get_exposed_services', param_name='services',
                                    param_type='text', action_params=params_json['get_exposed_services'])

@pytest.mark.get_exposed_services
def test_get_exposed_services_invalid_service_banner(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Exposed Services", "Verify with invalid Services Banner")
    result = run_invalid_param_test(connector_details, operation_name='get_exposed_services', param_name='service_banner',
                                    param_type='text', action_params=params_json['get_exposed_services'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_exposed_services
def test_get_exposed_services_invalid_products(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Exposed Services", "Verify with invalid Products")
    run_invalid_param_test_wrapper(connector_details, operation_name='get_exposed_services', param_name='products',
                                    param_type='text', action_params=params_json['get_exposed_services'])

@pytest.mark.get_exposed_services
def test_get_exposed_services_invalid_page(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Exposed Services", "Verify with invalid Page")
    result = run_invalid_param_test(connector_details, operation_name='get_exposed_services', param_name='page',
                                    param_type='integer', action_params=params_json['get_exposed_services'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_exposed_services
def test_get_exposed_services_invalid_asset(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Exposed Services", "Verify with invalid Asset")
    result = run_invalid_param_test(connector_details, operation_name='get_exposed_services', param_name='asset',
                                    param_type='text', action_params=params_json['get_exposed_services'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_cloud_integrations
def test_get_cloud_integrations_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Cloud Integrations", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_cloud_integrations',
                                   action_params=params_json['get_cloud_integrations']):
        assert result.get('status') == "Success"


@pytest.mark.get_cloud_integrations
def test_validate_get_cloud_integrations_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Cloud Integrations", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_cloud_integrations', info_json, params_json['get_cloud_integrations'])
    

@pytest.mark.get_cloud_integrations
def test_get_cloud_integrations_invalid_page(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Cloud Integrations", "Verify with invalid Page")
    result = run_invalid_param_test(connector_details, operation_name='get_cloud_integrations', param_name='page',
                                    param_type='integer', action_params=params_json['get_cloud_integrations'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_cloud_integrations
def test_get_cloud_integrations_invalid_size(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Cloud Integrations", "Verify with invalid Size")
    result = run_invalid_param_test(connector_details, operation_name='get_cloud_integrations', param_name='size',
                                    param_type='integer', action_params=params_json['get_cloud_integrations'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_fgt_integrations
def test_get_fgt_integrations_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get FortiGate Integrations", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_fgt_integrations',
                                   action_params=params_json['get_fgt_integrations']):
        assert result.get('status') == "Success"


@pytest.mark.get_fgt_integrations
def test_validate_get_fgt_integrations_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get FortiGate Integrations", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_fgt_integrations', info_json, params_json['get_fgt_integrations'])
    

@pytest.mark.get_fgt_integrations
def test_get_fgt_integrations_invalid_page(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get FortiGate Integrations", "Verify with invalid Page")
    result = run_invalid_param_test(connector_details, operation_name='get_fgt_integrations', param_name='page',
                                    param_type='integer', action_params=params_json['get_fgt_integrations'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_fgt_integrations
def test_get_fgt_integrations_invalid_size(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get FortiGate Integrations", "Verify with invalid Size")
    result = run_invalid_param_test(connector_details, operation_name='get_fgt_integrations', param_name='size',
                                    param_type='integer', action_params=params_json['get_fgt_integrations'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_security_insights
def test_get_security_insights_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Security Insights", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_security_insights',
                                   action_params=params_json['get_security_insights']):
        assert result.get('status') == "Success"


@pytest.mark.get_security_insights
def test_validate_get_security_insights_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Security Insights", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_security_insights', info_json, params_json['get_security_insights'])
    

@pytest.mark.get_security_insights
def test_get_security_insights_invalid_domain(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Security Insights", "Verify with invalid Domain")
    result = run_invalid_param_test(connector_details, operation_name='get_security_insights', param_name='domain',
                                    param_type='text', action_params=params_json['get_security_insights'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_archived_issue_comments
def test_get_archived_issue_comments_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Archived Issue Comments", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_archived_issue_comments',
                                   action_params=params_json['get_archived_issue_comments']):
        assert result.get('status') == "Success"


@pytest.mark.get_archived_issue_comments
def test_validate_get_archived_issue_comments_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Archived Issue Comments", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_archived_issue_comments', info_json, params_json['get_archived_issue_comments'])
    

@pytest.mark.get_archived_issue_comments
def test_get_archived_issue_comments_invalid_issue_id(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Archived Issue Comments", "Verify with invalid Issue ID")
    result = run_invalid_param_test(connector_details, operation_name='get_archived_issue_comments', param_name='issue_id',
                                    param_type='text', action_params=params_json['get_archived_issue_comments'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_archived_issue_comments
def test_get_archived_issue_comments_invalid_page(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Archived Issue Comments", "Verify with invalid Page")
    result = run_invalid_param_test(connector_details, operation_name='get_archived_issue_comments', param_name='page',
                                    param_type='integer', action_params=params_json['get_archived_issue_comments'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_archived_issue_comments
def test_get_archived_issue_comments_invalid_size(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Archived Issue Comments", "Verify with invalid Size")
    result = run_invalid_param_test(connector_details, operation_name='get_archived_issue_comments', param_name='size',
                                    param_type='integer', action_params=params_json['get_archived_issue_comments'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_issue_comments
def test_get_issue_comments_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Issue Comments", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_issue_comments',
                                   action_params=params_json['get_issue_comments']):
        assert result.get('status') == "Success"


@pytest.mark.get_issue_comments
def test_validate_get_issue_comments_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Issue Comments", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_issue_comments', info_json, params_json['get_issue_comments'])
    

@pytest.mark.get_issue_comments
def test_get_issue_comments_invalid_issue_id(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Issue Comments", "Verify with invalid Issue ID")
    result = run_invalid_param_test(connector_details, operation_name='get_issue_comments', param_name='issue_id',
                                    param_type='text', action_params=params_json['get_issue_comments'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_issue_comments
def test_get_issue_comments_invalid_page(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Issue Comments", "Verify with invalid Page")
    result = run_invalid_param_test(connector_details, operation_name='get_issue_comments', param_name='page',
                                    param_type='integer', action_params=params_json['get_issue_comments'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_issue_comments
def test_get_issue_comments_invalid_size(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Issue Comments", "Verify with invalid Size")
    result = run_invalid_param_test(connector_details, operation_name='get_issue_comments', param_name='size',
                                    param_type='integer', action_params=params_json['get_issue_comments'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_tags
def test_get_tags_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Tags", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_tags',
                                   action_params=params_json['get_tags']):
        assert result.get('status') == "Success"


@pytest.mark.get_tags
def test_validate_get_tags_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Tags", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_tags', info_json, params_json['get_tags'])
    

@pytest.mark.get_tags
def test_get_tags_invalid_page(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Tags", "Verify with invalid Page")
    result = run_invalid_param_test(connector_details, operation_name='get_tags', param_name='page',
                                    param_type='integer', action_params=params_json['get_tags'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_tags
def test_get_tags_invalid_size(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Tags", "Verify with invalid Size")
    result = run_invalid_param_test(connector_details, operation_name='get_tags', param_name='size',
                                    param_type='integer', action_params=params_json['get_tags'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_tags
def test_get_tags_invalid_name(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Tags", "Verify with invalid Name")
    result = run_invalid_param_test(connector_details, operation_name='get_tags', param_name='name',
                                    param_type='text', action_params=params_json['get_tags'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_tag_by_id
def test_get_tag_by_id_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Tag Details", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_tag_by_id',
                                   action_params=params_json['get_tag_by_id']):
        assert result.get('status') == "Success"


@pytest.mark.get_tag_by_id
def test_validate_get_tag_by_id_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Tag Details", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_tag_by_id', info_json, params_json['get_tag_by_id'])
    

@pytest.mark.get_tag_by_id
def test_get_tag_by_id_invalid_tag_id(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Tag Details", "Verify with invalid Tag ID")
    result = run_invalid_param_test(connector_details, operation_name='get_tag_by_id', param_name='tag_id',
                                    param_type='text', action_params=params_json['get_tag_by_id'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_groups
def test_get_groups_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Groups", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_groups',
                                   action_params=params_json['get_groups']):
        assert result.get('status') == "Success"


@pytest.mark.get_groups
def test_validate_get_groups_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Groups", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_groups', info_json, params_json['get_groups'])
    

@pytest.mark.get_groups
def test_get_groups_invalid_page(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Groups", "Verify with invalid Page")
    result = run_invalid_param_test(connector_details, operation_name='get_groups', param_name='page',
                                    param_type='integer', action_params=params_json['get_groups'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_groups
def test_get_groups_invalid_size(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Groups", "Verify with invalid Size")
    result = run_invalid_param_test(connector_details, operation_name='get_groups', param_name='size',
                                    param_type='integer', action_params=params_json['get_groups'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_groups
def test_get_groups_invalid_name(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Groups", "Verify with invalid Group Name")
    result = run_invalid_param_test(connector_details, operation_name='get_groups', param_name='name',
                                    param_type='text', action_params=params_json['get_groups'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_group_by_id
def test_get_group_by_id_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Group Details", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_group_by_id',
                                   action_params=params_json['get_group_by_id']):
        assert result.get('status') == "Success"


@pytest.mark.get_group_by_id
def test_validate_get_group_by_id_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Group Details", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_group_by_id', info_json, params_json['get_group_by_id'])
    

@pytest.mark.get_group_by_id
def test_get_group_by_id_invalid_group_id(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Group Details", "Verify with invalid Group ID")
    result = run_invalid_param_test(connector_details, operation_name='get_group_by_id', param_name='group_id',
                                    param_type='text', action_params=params_json['get_group_by_id'])
    assert result.get('status') == "failed"


@pytest.mark.update_archived_asset
def test_update_archived_asset_invalid_asset_id(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Update Archived Asset", "Verify with invalid Asset ID")
    result = run_invalid_param_test(connector_details, operation_name='update_archived_asset', param_name='asset_id',
                                    param_type='text', action_params=params_json['update_archived_asset'])
    assert result.get('status') == "failed"


@pytest.mark.update_archived_issue
def test_update_archived_issue_invalid_issue_id(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Update Archived Issue", "Verify with invalid Issue ID")
    result = run_invalid_param_test(connector_details, operation_name='update_archived_issue', param_name='issue_id',
                                    param_type='text', action_params=params_json['update_archived_issue'])
    assert result.get('status') == "failed"


@pytest.mark.update_issue_status
def test_update_issue_status_invalid_issue_id(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Update Issue Status", "Verify with invalid Issue ID")
    result = run_invalid_param_test(connector_details, operation_name='update_issue_status', param_name='issue_id',
                                    param_type='text', action_params=params_json['update_issue_status'])
    assert result.get('status') == "failed"


@pytest.mark.update_asn_asset_status_to_false_positive
def test_update_asn_asset_status_to_false_positive_invalid_asset_id(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Update ASN Asset To False Positive", "Verify with invalid Asset ID")
    result = run_invalid_param_test(connector_details, operation_name='update_asn_asset_status_to_false_positive', param_name='asset_id',
                                    param_type='text', action_params=params_json['update_asn_asset_status_to_false_positive'])
    assert result.get('status') == "failed"


@pytest.mark.update_prefix_asset_status_to_false_positive
def test_update_prefix_asset_status_to_false_positive_invalid_asset_id(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Update IP Prefix Asset To False Positive", "Verify with invalid Asset ID")
    result = run_invalid_param_test(connector_details, operation_name='update_prefix_asset_status_to_false_positive', param_name='asset_id',
                                    param_type='text', action_params=params_json['update_prefix_asset_status_to_false_positive'])
    assert result.get('status') == "failed"


@pytest.mark.update_ip_asset_status_to_false_positive
def test_update_ip_asset_status_to_false_positive_invalid_asset_id(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Update IP Asset To False Positive", "Verify with invalid Asset ID")
    result = run_invalid_param_test(connector_details, operation_name='update_ip_asset_status_to_false_positive', param_name='asset_id',
                                    param_type='text', action_params=params_json['update_ip_asset_status_to_false_positive'])
    assert result.get('status') == "failed"


@pytest.mark.update_domain_asset_status_to_false_positive
def test_update_domain_asset_status_to_false_positive_invalid_asset_id(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Update Domain Asset To False Positive", "Verify with invalid Asset ID")
    result = run_invalid_param_test(connector_details, operation_name='update_domain_asset_status_to_false_positive', param_name='asset_id',
                                    param_type='text', action_params=params_json['update_domain_asset_status_to_false_positive'])
    assert result.get('status') == "failed"


@pytest.mark.update_subdomain_asset_status_to_false_positive
def test_update_subdomain_asset_status_to_false_positive_invalid_asset_id(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Update Sub-Domain Asset To False Positive", "Verify with invalid Asset ID")
    result = run_invalid_param_test(connector_details, operation_name='update_subdomain_asset_status_to_false_positive', param_name='asset_id',
                                    param_type='text', action_params=params_json['update_subdomain_asset_status_to_false_positive'])
    assert result.get('status') == "failed"


@pytest.mark.update_leaked_credential_status
def test_update_leaked_credential_status_invalid_leaked_cred_id(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Update Leaked Credential Status", "Verify with invalid Leaked Credential ID")
    result = run_invalid_param_test(connector_details, operation_name='update_leaked_credential_status', param_name='leaked_cred_id',
                                    param_type='text', action_params=params_json['update_leaked_credential_status'])
    assert result.get('status') == "failed"
