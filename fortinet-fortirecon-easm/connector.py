"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""

from connectors.core.connector import Connector, get_logger, ConnectorError
from .operations import operations
from. check_health import check_health_ex
logger = get_logger('fortinet-fortirecon-easm')


class FortiReconEASM(Connector):
    def execute(self, config, operation, params, **kwargs):
        try:
            logger.info('In execute() Operation:[{}]'.format(operation))
            operation = operations.get(operation, None)
            if not operation:
                logger.info('Unsupported operation [{}]'.format(operation))
                raise ConnectorError('Unsupported operation')
            result = operation(config, params)
            return result
        except Exception as err:
            logger.exception(str(err))
            raise ConnectorError(err)

    def check_health(self, config, **kwargs):
        try:
            return check_health_ex(config)
        except Exception as err:
            logger.exception(str(err))
            raise ConnectorError(err)
