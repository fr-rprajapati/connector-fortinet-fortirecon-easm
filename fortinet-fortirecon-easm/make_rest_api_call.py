"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""
import json

import requests
from datetime import datetime
from connectors.core.connector import get_logger, ConnectorError
from .constants import COMMA_SEPARATED_INPUT_PARAM, SEARCH_TYPE_MAPPING

error_msg = {
    401: 'Authentication failed due to invalid credentials',
    429: 'Rate limit was exceeded',
    403: 'Token is invalid or expired',
    "ssl_error": 'SSL certificate validation failed',
    'time_out': 'The request timed out while trying to connect to the remote server',
}

logger = get_logger("fortinet-fortirecon-easm")


class MakeRestApiCall:

    def __init__(self, config):
        self.server_url = config.get('server_url').strip().strip('/')
        if not self.server_url.startswith('http') or not self.server_url.startswith('https'):
            self.server_url = 'https://' + self.server_url
        self.api_key = config.get("api_key")
        self.org_id = config.get('org_id')
        self.headers = {
            "accept": "application/json",
            "Authorization": self.api_key
        }
        self.verify_ssl = config.get("verify_ssl", True)

    def make_request(self, endpoint='', params=None, data=None, method='GET', url=None, flag=True):
        try:
            if url is None:
                url = '{0}{1}'.format(self.server_url, endpoint.format(org_id=self.org_id))
            headers = self.headers if flag else None
            response = requests.request(method=method, url=url, headers=headers, json=data,
                                        params=params, verify=self.verify_ssl)
            try:
                from connectors.debug_utils.curl_script import make_curl
                make_curl(method, url, headers=headers, params=params, json=data, verify_ssl=self.verify_ssl)
            except Exception as err:
                logger.debug(f"Error in curl utils: {str(err)}")
            if response.ok:
                try:
                    return response.json()
                except:
                    return response.text
            else:
                logger.error("Error: {0}".format(response.json()))
                raise ConnectorError('{0}'.format(error_msg.get(response.status_code, response.text)))
        except requests.exceptions.SSLError as e:
            logger.exception('{0}'.format(e))
            raise ConnectorError('{0}'.format(error_msg.get('ssl_error')))
        except requests.exceptions.ConnectionError as e:
            logger.exception('{0}'.format(e))
            raise ConnectorError('{0}'.format(error_msg.get('time_out')))
        except Exception as e:
            logger.error('{0}'.format(e))
            raise ConnectorError('{0}'.format(e))

    def convert_date(self, date_ts):
        conv_date_time = datetime.strptime(date_ts, "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d")
        return conv_date_time

    def build_payload(self, params: {}):
        logger.debug("Input Params: {0}".format(params))
        data = {}
        for k, v in params.items():
            if not (v == '' or v is None):
                if k in COMMA_SEPARATED_INPUT_PARAM:
                    if isinstance(v, (list, tuple)):
                        data[k] = ",".join(map(str, v))
                    elif type(v) is str:
                        data[k] = v.replace(" ", '')
                    else:
                        data[k] = v
                elif k == 'search_type':
                    data[k] = SEARCH_TYPE_MAPPING.get(v, v)
                elif k == 'ports':
                    if isinstance(v, (tuple, list)):
                        data[k] = ",".join(map(str, v))
                    elif isinstance(v, str):
                        data[k] = v.replace(' ', '')
                    else:
                        data[k] = v
                elif k == 'cloud_metadata':
                    data[k] = json.dumps(v)
                else:
                    data[k] = v
        return data
