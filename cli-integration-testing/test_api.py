import random
import subprocess

import pytest
from dotenv import load_dotenv
import os
import http.client
import json
from util.utils import *

load_dotenv()  # Load environment variables from .env file

AZURE_OPENAI_URI = os.getenv('AZURE_OPENAI_URI')
AZURE_OPENAI_TOKEN = os.getenv('AZURE_OPENAI_TOKEN')
# CLI_DIR = '/Users/jacksonboey/PycharmProjects/moonshot'
# CLI_DIR = os.getenv('CLI_DIR')
CLI_DIR = '/Users/jacksonboey/PycharmProjects/moonshot'

# def test_replace_file_content():
#     # Example Usage
#     file_path = "example.txt"
#     new_content = "This is the new content of the file.\nIt will replace the old content."
#
#     replace_file_content(file_path, new_content)

def test_api_create_recipe():
    conn = http.client.HTTPConnection("127.0.0.1", 5000)
    # Generate a random number between 0 and 999,999,999 (inclusive)
    random_number = int(random.random() * 1000000000)

    payload = json.dumps({
        "name": "test-recipe-"+str(random_number),
        "tags": [
            ""
        ],
        "categories": [
            ""
        ],
        "datasets": [
            "sg-university-tutorial-questions-legal"
        ],
        "prompt_templates": [
            ""
        ],
        "metrics": [
            "samplemetric"
        ],
        "grading_scale": {}
    })
    headers = {
        'Content-Type': 'application/json'
    }
    conn.request("POST", "/api/v1/recipes", payload, headers)
    res = conn.getresponse()
    data = res.read()
    response = data.decode("utf-8")
    print("Output : "+response)

    assert response == "{\"message\":\"Recipe created successfully\"}"

def test_api_create_recipe_invalid_dataset():
    conn = http.client.HTTPConnection("127.0.0.1", 5000)
    # Generate a random number between 0 and 999,999,999 (inclusive)
    random_number = int(random.random() * 1000000000)

    payload = json.dumps({
        "name": "test-recipe-"+str(random_number),
        "tags": [
            ""
        ],
        "categories": [
            ""
        ],
        "datasets": [
            "data-set"
        ],
        "prompt_templates": [
            ""
        ],
        "metrics": [
            "samplemetric"
        ],
        "grading_scale": {}
    })
    headers = {
        'Content-Type': 'application/json'
    }
    conn.request("POST", "/api/v1/recipes", payload, headers)
    res = conn.getresponse()
    data = res.read()
    response = data.decode("utf-8")
    print("Output : "+response)
    error_message = '{"detail":"Failed to create recipe: [ServiceException] UnexpectedError in create_recipe - An unexpected error occurred: [Recipe] Dataset data-set does not exist."}'
    assert response == error_message

def test_api_create_recipe():
    conn = http.client.HTTPConnection("127.0.0.1", 5000)
    # Generate a random number between 0 and 999,999,999 (inclusive)
    random_number = int(random.random() * 1000000000)

    payload = json.dumps({
        "name": "test-recipe-"+str(random_number),
        "tags": [
            ""
        ],
        "categories": [
            ""
        ],
        "datasets": [
            "sg-university-tutorial-questions-legal"
        ],
        "prompt_templates": [
            ""
        ],
        "metrics": [
            "samplemetric"
        ],
        "grading_scale": {}
    })
    headers = {
        'Content-Type': 'application/json'
    }
    conn.request("POST", "/api/v1/recipes", payload, headers)
    res = conn.getresponse()
    data = res.read()
    response = data.decode("utf-8")
    print("Output : "+response)

    assert response == "{\"message\":\"Recipe created successfully\"}"
