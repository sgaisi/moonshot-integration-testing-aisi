from dotenv import load_dotenv
import os
from util import parametrize, INPUT_PARAMS

load_dotenv()  # Load environment variables from .env file

AZURE_OPENAI_URI = os.getenv('AZURE_OPENAI_URI')
AZURE_OPENAI_TOKEN = os.getenv('AZURE_OPENAI_TOKEN')

EXPECTED_OUTCOME = [
    "Success",      # Expected result
    "Failed",      # Expected result
    "Failed",      # Expected result
    "Failed",      # Expected result
    "Failed",     # Expected result
    "Failed",     # Expected result
]
@parametrize("input_params, expected", zip(INPUT_PARAMS, EXPECTED_OUTCOME))
def test_parametrize(input_params,expected):
    print("Parameters : "+str(input_params)+":  "+ str(expected))
    assert input_params == expected