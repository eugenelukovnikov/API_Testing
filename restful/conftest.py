from restful.settings import *

import os
import sys
import pytest

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PROJECT_ROOT)

from selenium import webdriver

#from restful.endpoints.restful_api import RestfulApi
from restful.endpoints import restful_api
from restful.payloads import payloads

@pytest.fixture
def obj_id():
    create_object = restful_api.RestfulApi()
    delete_object = restful_api.RestfulApi()
    post_payload = payloads.Payload.post()
    

    create_object.post_object(payload=post_payload)
    
    yield create_object.response_json['id']
    delete_object.delete_object(create_object.response_json['id'])

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.allure_report_dir = "allure-results"
                    



    