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

def test_cli():


    assert True