import subprocess

import pytest
from dotenv import load_dotenv
import os
import random
from util import *

load_dotenv()  # Load environment variables from .env file

OPENAI_TOKEN = os.getenv('OPENAI_TOKEN')
MOON_V1_CLI_DIR = os.getenv('MOON_V1_CLI_DIR')


def assert_run_outcome(output_lines):
    output_lines = [line.replace(" ", "") for line in output_lines if line.strip()]
    assert "File written".replace(" ", "") in output_lines
    assert "successfully at:".replace(" ", "") in output_lines
    assert "data/results/test_run_".replace(" ", "") in output_lines
    assert "successfully created with".replace(" ", "") in output_lines
    assert "run_id:".replace(" ", "") in output_lines

EXPECTED_OUTCOME = [
    ("Error loading attack"),  # Expected result for 1
    ("Error loading attack"),  # Expected result for 1.1
    (""),  # Expected result for -1
    ("Error loading attack"),  # Expected result for 0
    ("Error loading attack"),  # Expected result for "@1"
    ("Error loading attack")  # Expected result for "test"
]

@parametrize("input_params, expectedMsg", zip(INPUT_PARAMS, EXPECTED_OUTCOME))
def test_cli_run_create_scan_test_params_testing_attack_module(input_params,expectedMsg):
    # Generate a random number between 0 and 999,999,999 (inclusive)
    random_number = int(random.random() * 1000000000)
    attack_module = str(input_params)
    metric_module = "refusal_adapter"
    connector_name = "my-gpt4o-mini"
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
    output_lines = [line.replace(" ", "") for line in stdout.splitlines() if line.strip()]
    # Assert Outcome
    if input_params == -1:
        # Assert that the subprocess failed
        assert process.returncode != 0  # Ensure it exits with an error
        # Assert that the error contains Pydantic's validation message
        assert "Error: No such option: -1\n"
    else:
        assert expectedMsg.replace(" ", "") in output_lines

METRIC_PARAM_EXPECTED_OUTCOME = [
    ("Error loading metric"),  # Expected result for 1
    ("Error loading metric"),  # Expected result for 1.1
    (""),  # Expected result for -1
    ("Error loading metric"),  # Expected result for 0
    ("Error loading metric"),  # Expected result for "@1"
    ("Error loading metric")  # Expected result for "test"
]
@parametrize("input_params, expectedMsg", zip(INPUT_PARAMS, METRIC_PARAM_EXPECTED_OUTCOME))
def test_cli_run_create_scan_test_params_testing_metric_module(input_params,expectedMsg):
    # Generate a random number between 0 and 999,999,999 (inclusive)
    random_number = int(random.random() * 1000000000)
    attack_module = "hallucination"
    metric_module = str(input_params)
    connector_name = "my-gpt4o-mini"
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
    output_lines = [line.replace(" ", "") for line in stdout.splitlines() if line.strip()]
    # Assert Outcome
    if input_params == -1:
        # Assert that the subprocess failed
        assert process.returncode != 0  # Ensure it exits with an error
        # Assert that the error contains Pydantic's validation message
        assert "Error: No such option: -1\n"
    else:
        assert expectedMsg.replace(" ", "") in output_lines


CONNECTOR_PARAM_EXPECTED_OUTCOME = [
    ("Error loading the connector"),  # Expected result for 1
    ("Error loading the connector"),  # Expected result for 1.1
    ("", 0),  # Expected result for -1
    ("Error loading the connector"),  # Expected result for 0
    ("Error loading the connector"),  # Expected result for "@1"
    ("Error loading the connector")  # Expected result for "test"
]
@parametrize("input_params, expectedMsg", zip(INPUT_PARAMS, CONNECTOR_PARAM_EXPECTED_OUTCOME))
def test_cli_run_create_scan_test_params_testing_connector_name(input_params,expectedMsg):
    # Generate a random number between 0 and 999,999,999 (inclusive)
    random_number = int(random.random() * 1000000000)
    attack_module = "hallucination"
    metric_module = "refusal_adapter"
    connector_name = str(input_params)
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
    output_lines = [line.replace(" ", "") for line in stdout.splitlines() if line.strip()]
    # Assert Outcome
    if input_params == -1:
        # Assert that the subprocess failed
        assert process.returncode != 0  # Ensure it exits with an error
        # Assert that the error contains Pydantic's validation message
        assert "Error: No such option: -1\n"
    else:
        assert expectedMsg.replace(" ", "") in output_lines



def test_cli_run_redteaming_hallucination_refusal_adapter():

    # Generate a random number between 0 and 999,999,999 (inclusive)
    random_number = int(random.random() * 1000000000)
    attack_module = "hallucination"
    metric_module = "refusal_adapter"
    connector_name = "my-gpt4o-mini"
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
    assert_run_outcome(output_lines)
    check_result_file_exists(MOON_V1_CLI_DIR + "/data/results/" + nameOfRunnerName + ".json")

def test_cli_run_redteaming_sensitive_data_disclosure_refusal_adapter():

    # Generate a random number between 0 and 999,999,999 (inclusive)
    random_number = int(random.random() * 1000000000)
    attack_module = "sensitive_data_disclosure"
    connector_name = "my-gpt4o-mini"
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
    assert_run_outcome(output_lines)
    check_result_file_exists(MOON_V1_CLI_DIR + "/data/results/" + nameOfRunnerName + ".json")
def test_cli_run_redteaming_system_prompt_leakage_refusal_adapter():

    # Generate a random number between 0 and 999,999,999 (inclusive)
    random_number = int(random.random() * 1000000000)
    attack_module = "system_prompt_leakage"
    connector_name = "my-gpt4o-mini"
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

    # Assert Outcome
    assert_run_outcome(output_lines)
    check_result_file_exists(MOON_V1_CLI_DIR + "/data/results/" + nameOfRunnerName + ".json")