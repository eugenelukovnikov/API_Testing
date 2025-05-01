from brewery_api.settings import *

import os
import sys
import pytest

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PROJECT_ROOT)


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.allure_report_dir = "allure-results"
                    



    