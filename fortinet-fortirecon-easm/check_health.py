"""
Copyright start
MIT License
Copyright (c) 2025 Fortinet Inc
Copyright end
"""

from .scan_statistics import get_scan_statistics


def check_health_ex(config):
    get_scan_statistics(config, {})
    return True
