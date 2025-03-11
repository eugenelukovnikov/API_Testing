from settings import *
import os
import pytest


from selenium import webdriver

from endpoints.restful_api import RestfulApi
from endpoints.restful_api import RestfulApi
from payloads import payloads

@pytest.fixture
def obj_id():
    create_object = RestfulApi()
    delete_object = RestfulApi()
    post_payload = payloads.Payload.post()
    

    create_object.post_object(payload=post_payload)
    
    yield create_object.response_json['id']
    delete_object.delete_object(create_object.response_json['id'])

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.allure_report_dir = "allure-results"
                    



    