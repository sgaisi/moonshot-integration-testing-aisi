import subprocess

import pytest
from dotenv import load_dotenv
import os
import random
from util import parametrize, INPUT_PARAMS

load_dotenv()  # Load environment variables from .env file

OPENAI_TOKEN = os.getenv('OPENAI_TOKEN')
MOON_V1_CLI_DIR = os.getenv('MOON_V1_CLI_DIR')

def assert_run_outcome(output_lines,test_run_name):
    # Get the last line of the output
    line_3 = output_lines[-3]
    line_3_expected = "successfully created with"
    line_2 = output_lines[-2]
    line_2_expected = "run_id:"
    line_1 = output_lines[-1]
    line_1_expected = test_run_name
    print('=========================Output Last Line:', line_3)
    print('=========================Output Last Line:', line_2)
    print('=========================Output Last Line:', line_1)
    assert line_3.replace(" ", "") == line_3_expected.replace(" ", "")
    assert line_2.replace(" ", "") == line_2_expected.replace(" ", "")
    assert line_1.replace(" ", "") == line_1_expected.replace(" ", "")

EXPECTED_OUTCOME = [
    "successfully created with",      # Expected result for 1
    "successfully created with",      # Expected result for 1.1
    "successfully created with",      # Expected result for -1
    "successfully created with",      # Expected result for 0
    "successfully created with",     # Expected result for "@1"
    "successfully created with",     # Expected result for "test"
]
@pytest.mark.skip(reason="This test is skipped for now")
@parametrize("input_params, expected", zip(INPUT_PARAMS, EXPECTED_OUTCOME))
def test_cli_run_create_scan_test_params_testing(input_params,expected):

    # Generate a random number between 0 and 999,999,999 (inclusive)
    random_number = int(random.random() * 1000000000)
    attack_module = str(input_params)
    metric_module = "refusal_adapter"
    connector_name = "my-gpt4o"
    nameOfRunnerName = "test_run_" + connector_name + "_" + attack_module + "_" + str(random_number)
    commands = [
        "export OPENAI_API_KEY="+OPENAI_TOKEN,
        "poetry run moonshot scan " + nameOfRunnerName + " "+attack_module+" "+metric_module+" "+connector_name+""
    ]
    # Join commands with '&&' to ensure the next runs only if the previous succeeds
    full_command = "&&".join(commands)
    print(f"Running combined command: {full_command}")

    process = subprocess.Popen(
        full_command,
        shell=True,  # Allows for complex shell commands
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        stdin=subprocess.PIPE,
        text=True,
        cwd=str(MOON_V1_CLI_DIR),
    )
    print('Path:', str(MOON_V1_CLI_DIR))
    # Ensure process.stdin is not None
    if process.stdin is None:
        raise RuntimeError("Failed to create stdin for the subprocess")

    # Capture the output and errors
    stdout, stderr = process.communicate()

    print('Output:', stdout)
    # Split the output into lines
    output_lines = stdout.splitlines()
    #Assert Outcome
    assert output_lines[-4].replace(" ", "") == expected.replace(" ", "")

@pytest.mark.skip(reason="This test is skipped for now")
def test_cli_run_redteaming_hallucination_refusal_adapter():

    # Generate a random number between 0 and 999,999,999 (inclusive)
    random_number = int(random.random() * 1000000000)
    attack_module = "hallucination"
    metric_module = "refusal_adapter"
    connector_name = "my-gpt-o1"
    nameOfRunnerName = "test_run_" + connector_name + "_" + attack_module + "_" + str(random_number)
    commands = [
        "export OPENAI_API_KEY="+OPENAI_TOKEN,
        "poetry run moonshot scan " + nameOfRunnerName + " "+attack_module+" "+metric_module+" "+connector_name+""
    ]
    # Join commands with '&&' to ensure the next runs only if the previous succeeds
    full_command = "&&".join(commands)
    print(f"Running combined command: {full_command}")

    process = subprocess.Popen(
        full_command,
        shell=True,  # Allows for complex shell commands
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        stdin=subprocess.PIPE,
        text=True,
        cwd=str(MOON_V1_CLI_DIR),
    )
    print('Path:', str(MOON_V1_CLI_DIR))
    # Ensure process.stdin is not None
    if process.stdin is None:
        raise RuntimeError("Failed to create stdin for the subprocess")

    # Capture the output and errors
    stdout, stderr = process.communicate()

    print('Output:', stdout)
    # Split the output into lines
    output_lines = stdout.splitlines()
    #Assert Outcome
    # Get the last line of the output
    line_14 = output_lines[-14]
    line_14_expected = "File written"
    line_13 = output_lines[-13]
    line_13_expected = "successfully at:"
    line_12 = output_lines[-12]
    line_12_expected = "data/results/test_run_"
    print('=========================Output Last Line:', line_14)
    print('=========================Output Last Line:', line_13)
    print('=========================Output Last Line:', line_12)
    assert line_14.replace(" ", "") == line_14_expected.replace(" ", "")
    assert line_13.replace(" ", "") == line_13_expected.replace(" ", "")
    assert line_12.replace(" ", "") == line_12_expected.replace(" ", "")
    assert_run_outcome(output_lines,nameOfRunnerName)
@pytest.mark.skip(reason="This test is skipped for now")
def test_cli_run_redteaming_sensitive_data_disclosure_refusal_adapter():

    # Generate a random number between 0 and 999,999,999 (inclusive)
    random_number = int(random.random() * 1000000000)
    attack_module = "sensitive_data_disclosure"
    connector_name = "my-gpt-o1"
    nameOfRunnerName = "test_run_" + connector_name + "_" + attack_module + "_" + str(random_number)
    metric_module = "refusal_adapter"
    commands = [
        "export OPENAI_API_KEY="+OPENAI_TOKEN,
        "poetry run moonshot scan " + nameOfRunnerName + " "+attack_module+" "+metric_module+" "+connector_name+""
    ]
    # Join commands with '&&' to ensure the next runs only if the previous succeeds
    full_command = "&&".join(commands)
    print(f"Running combined command: {full_command}")

    process = subprocess.Popen(
        full_command,
        shell=True,  # Allows for complex shell commands
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        stdin=subprocess.PIPE,
        text=True,
        cwd=str(MOON_V1_CLI_DIR),
    )
    print('Path:', str(MOON_V1_CLI_DIR))
    # Ensure process.stdin is not None
    if process.stdin is None:
        raise RuntimeError("Failed to create stdin for the subprocess")

    # Capture the output and errors
    stdout, stderr = process.communicate()

    print('Output:', stdout)
    # Split the output into lines
    output_lines = stdout.splitlines()
    # Assert Outcome
    assert_run_outcome(output_lines,nameOfRunnerName)
@pytest.mark.skip(reason="This test is skipped for now")
def test_cli_run_redteaming_system_prompt_leakage_refusal_adapter():

    # Generate a random number between 0 and 999,999,999 (inclusive)
    random_number = int(random.random() * 1000000000)
    attack_module = "system_prompt_leakage"
    connector_name = "my-gpt-o1"
    nameOfRunnerName = "test_run_"+connector_name+"_"+attack_module+"_" + str(random_number)
    metric_module = "refusal_adapter"
    commands = [
        "export OPENAI_API_KEY="+OPENAI_TOKEN,
        "poetry run moonshot scan " + nameOfRunnerName + " "+attack_module+" "+metric_module+" "+connector_name+""
    ]
    # Join commands with '&&' to ensure the next runs only if the previous succeeds
    full_command = "&&".join(commands)
    print(f"Running combined command: {full_command}")

    process = subprocess.Popen(
        full_command,
        shell=True,  # Allows for complex shell commands
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        stdin=subprocess.PIPE,
        text=True,
        cwd=str(MOON_V1_CLI_DIR),
    )
    print('Path:', str(MOON_V1_CLI_DIR))
    # Ensure process.stdin is not None
    if process.stdin is None:
        raise RuntimeError("Failed to create stdin for the subprocess")

    # Capture the output and errors
    stdout, stderr = process.communicate()

    print('Output:', stdout)
    # Split the output into lines
    output_lines = stdout.splitlines()

    #Assert Outcome
    # Get the last line of the output
    line_16 = output_lines[-16]
    line_16_expected = "File written"
    line_15 = output_lines[-15]
    line_15_expected = "successfully at:"
    line_14 = output_lines[-14]
    line_14_expected = "data/results/test_run_"
    print('=========================Output Last Line:', line_16)
    print('=========================Output Last Line:', line_15)
    print('=========================Output Last Line:', line_14)
    assert line_16.replace(" ", "") == line_16_expected.replace(" ", "")
    assert line_15.replace(" ", "") == line_15_expected.replace(" ", "")
    assert line_14.replace(" ", "") == line_14_expected.replace(" ", "")
    assert_run_outcome(output_lines, nameOfRunnerName)