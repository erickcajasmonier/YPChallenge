import unittest
import pytest
import os
import requests
import json
import xml.etree.ElementTree as ET
from Helper.Common.data_helper import initialize_environment

initialize_environment()

def get_request_header(req_body_type, res_content_type):
    return {
        'Content-Type': 'application/{}'.format(req_body_type),
        'accept': 'application/{}'.format(res_content_type)
    }

def get_request_api(route, req_body_type='json', res_content_type='xml'):
    return requests.get(os.getenv('BASE_URL') + route,
                        headers=get_request_header(req_body_type, res_content_type))

def post_request_api(route, body='', req_body_type='json', res_content_type='xml'):
    if req_body_type == 'json':
        body = json.dumps(body)

    return requests.post(os.getenv('BASE_URL') + route,
                         headers=get_request_header(req_body_type, res_content_type), data=body)

def put_request_api(route, body, req_body_type='json', res_content_type='xml'):
    if req_body_type == 'json':
        body = json.dumps(body)

    return requests.put(os.getenv('BASE_URL') + route,
                        headers=get_request_header(req_body_type, res_content_type), data=body)

def delete_request_api(route, req_body_type='json', res_content_type='xml'):
    return requests.delete(os.getenv('BASE_URL') + route,
                           headers=get_request_header(req_body_type, res_content_type))

def get_xml_element_value(element_key_path, response, attribute = None):
    root = ET.fromstring(response.content)
    return root.find(element_key_path).text if attribute is None else root.find(element_key_path).attrib[attribute]

def get_xml_element_values(element_key_path, response):
    root = ET.fromstring(response.content)
    values_list = []
    for value in root.findall(element_key_path):
        values_list.append(value.text)
    return values_list