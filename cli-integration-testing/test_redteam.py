import random

import pytest
import subprocess
from dotenv import load_dotenv
import os

import random

load_dotenv()  # Load environment variables from .env file

AZURE_OPENAI_URI = os.getenv('AZURE_OPENAI_URI')
AZURE_OPENAI_TOKEN = os.getenv('AZURE_OPENAI_TOKEN')
# CLI_DIR = '/Users/jacksonboey/PycharmProjects/moonshot'
CLI_DIR = os.getenv('CLI_DIR')
def test_cli_red_teaming():
    command = (
        # 'cd .. &&'
        # 'source venv/bin/activate &&'
        # 'cd moonshot &&'
        'python3 -m moonshot cli interactive'
    )
    process = subprocess.Popen(
        command,
        shell=True,  # Allows for complex shell commands
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        stdin=subprocess.PIPE,
        text=True,
        cwd=str(CLI_DIR),
    )

    # Ensure process.stdin is not None
    if process.stdin is None:
        raise RuntimeError("Failed to create stdin for the subprocess")

    # # Example command to send to the process
    # process.stdin.write('list_cookbooks\n')
    # process.stdin.flush()

    # Generate a random number between 0 and 999,999,999 (inclusive)
    random_number = int(random.random() * 1000000000)
    nameOfRunnerFileName = "my-red-teaming-runner-" + str(random_number)

    file_path = str(CLI_DIR)+"/moonshot-data/generated-outputs/runners/"+nameOfRunnerFileName+".json"

    # # Example command to send to the process
    # process.stdin.write('use_session "my-runner"\n')
    # process.stdin.flush()

    command = 'new_session '+nameOfRunnerFileName+' -e "[\'ollama-llama3\']" -c add_previous_prompt -p mmlu \n'
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    # Example command to send to the process
    process.stdin.write('run_attack_module charswap_attack "this is my prompt"\n')
    process.stdin.flush()

    # # Capture the output and errors
    # stdout, stderr = process.communicate()

    # Capture the output and errors
    stdout, stderr = process.communicate()

    print('Output:', stdout)

    if os.path.exists(file_path):
        print(f"File exists: {file_path}")
        assert True


    else:
        print(f"File does not exist: {file_path}")
        pytest.fail()