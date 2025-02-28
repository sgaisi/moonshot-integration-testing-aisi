import subprocess
import pytest
from dotenv import load_dotenv
import os
import random
from util import parametrize, INPUT_PARAMS

load_dotenv()  # Load environment variables from .env file

OPENAI_TOKEN = os.getenv('OPENAI_TOKEN')
MOON_V1_CLI_DIR = os.getenv('MOON_V1_CLI_DIR')


EXPECTED_OUTCOME = [
    ("No valid file found for 1 in ", 14),  # Expected result for 1
    ("No valid file found for 1.1 in", 14),  # Expected result for 1.1
    ("", 0),  # Expected result for -1
    ("No valid file found for 0 in", 14),  # Expected result for 0
    ("No valid file found for @1 in", 14),  # Expected result for "@1"
    ("No valid file found for test in", 14)  # Expected result for "test"
]
@parametrize("input_params, expected", zip(INPUT_PARAMS, EXPECTED_OUTCOME))
def test_cli_run_benchmarking_params_testing_dataset_module(input_params,expected):
    expectedMsg, expected_value = expected  # Extract the second value
    # Generate a random number between 0 and 999,999,999 (inclusive)
    random_number = int(random.random() * 1000000000)
    dataset_module = str(input_params)
    connector_name = "my-gpt4o"
    nameOfRunnerName = "my-benchmarking-" + connector_name + "-" + dataset_module + "-" + str(random_number)
    metric_module = "refusal_adapter"

    commands = [
        "export OPENAI_API_KEY=" + OPENAI_TOKEN,
        "poetry run moonshot benchmark " + nameOfRunnerName + " " + dataset_module + " " + metric_module + " " + connector_name + ""
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

CONNECTOR_EXPECTED_OUTCOME = [
    ("ERROR    [TaskManager] Error loading the task_manager.py:483", 6),  # Expected result for 1
    ("ERROR    [TaskManager] Error loading the task_manager.py:483", 6),  # Expected result for 1.1
    ("", 0),  # Expected result for -1
    ("ERROR    [TaskManager] Error loading the task_manager.py:483", 6),  # Expected result for 0
    ("ERROR    [TaskManager] Error loading the task_manager.py:483", 6),  # Expected result for "@1"
    ("ERROR    [TaskManager] Error loading the task_manager.py:483", 6)  # Expected result for "test"
]
@parametrize("input_params, expected", zip(INPUT_PARAMS, CONNECTOR_EXPECTED_OUTCOME))
def test_cli_run_benchmarking_params_testing_connector_name(input_params,expected):
    expectedMsg, expected_value = expected  # Extract the second value
    # Generate a random number between 0 and 999,999,999 (inclusive)
    random_number = int(random.random() * 1000000000)
    dataset_module = "mmlu-mini"
    connector_name = str(input_params)
    nameOfRunnerName = "my-benchmarking-" + connector_name + "-" + dataset_module + "-" + str(random_number)
    metric_module = "refusal_adapter"

    commands = [
        "export OPENAI_API_KEY=" + OPENAI_TOKEN,
        "poetry run moonshot benchmark " + nameOfRunnerName + " " + dataset_module + " " + metric_module + " " + connector_name + ""
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

METRIC_MODULE_EXPECTED_OUTCOME = [
    ("Error loading metric", 6),  # Expected result for 1
    ("Error loading metric", 6),  # Expected result for 1.1
    ("", 0),  # Expected result for -1
    ("Error loading metric", 6),  # Expected result for 0
    ("Error loading metric", 6),  # Expected result for "@1"
    ("Error loading metric", 6)  # Expected result for "test"
]
@parametrize("input_params, expected", zip(INPUT_PARAMS, METRIC_MODULE_EXPECTED_OUTCOME))
def test_cli_run_benchmarking_params_testing_metric_module(input_params,expected):
    expectedMsg, expected_value = expected  # Extract the second value
    # Generate a random number between 0 and 999,999,999 (inclusive)
    random_number = int(random.random() * 1000000000)
    dataset_module = "mmlu-mini"
    connector_name = "my-gpt4o"
    nameOfRunnerName = "my-benchmarking-" + connector_name + "-" + dataset_module + "-" + str(random_number)
    metric_module = str(input_params)

    commands = [
        "export OPENAI_API_KEY=" + OPENAI_TOKEN,
        "poetry run moonshot benchmark " + nameOfRunnerName + " " + dataset_module + " " + metric_module + " " + connector_name + ""
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
def assert_run_outcome(output_lines):
    output_lines = [line.replace(" ", "") for line in output_lines if line.strip()]

    assert "File written".replace(" ", "") in output_lines
    assert "successfully at:".replace(" ", "") in output_lines
    assert "data/results/my-benchm".replace(" ", "") in output_lines
    assert "successfully created with run_id:".replace(" ", "") in output_lines

def test_cli_run_benchmarking_refusal_adapter_mmlu_mini():

    # Generate a random number between 0 and 999,999,999 (inclusive)
    random_number = int(random.random() * 1000000000)
    dataset_module = "mmlu-mini"
    connector_name = "my-gpt4o"
    nameOfRunnerName = "my-benchmarking-" + connector_name + "-" + dataset_module + "-" + str(random_number)
    metric_module = "refusal_adapter"

    commands = [
        "export OPENAI_API_KEY="+OPENAI_TOKEN,
        "poetry run moonshot benchmark " + nameOfRunnerName + " "+dataset_module+" "+metric_module+" "+connector_name+""
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
    # Assert Results
    assert_run_outcome(output_lines)
@pytest.mark.skip(reason="This test is skipped for now")
def test_cli_run_benchmarking_refusal_adapter_prompt_injection_obfuscation():

    # Generate a random number between 0 and 999,999,999 (inclusive)
    random_number = int(random.random() * 1000000000)
    dataset_module = "prompt_injection_obfuscation"
    connector_name = "my-gpt4o"
    nameOfRunnerName = "my-benchmarking-"+connector_name+"-"+dataset_module+"-" + str(random_number)
    metric_module = "refusal_adapter"

    commands = [
        "export OPENAI_API_KEY="+OPENAI_TOKEN,
        "poetry run moonshot benchmark " + nameOfRunnerName + " "+dataset_module+" "+metric_module+" "+connector_name+""
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

    # Assert Results
    assert_run_outcome(output_lines)
@pytest.mark.skip(reason="This test is skipped for now")
def test_cli_run_benchmarking_refusal_adapter_prompt_injection_payload_splitting():

    # Generate a random number between 0 and 999,999,999 (inclusive)
    random_number = int(random.random() * 1000000000)
    dataset_module = "prompt_injection_payload_splitting"
    connector_name = "my-gpt4o"
    nameOfRunnerName = "my-benchmarking-" + connector_name + "-" + dataset_module + "-" + str(random_number)
    metric_module = "refusal_adapter"

    commands = [
        "export OPENAI_API_KEY="+OPENAI_TOKEN,
        "poetry run moonshot benchmark " + nameOfRunnerName + " "+dataset_module+" "+metric_module+" "+connector_name+""
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

    # Assert Results
    assert_run_outcome(output_lines)
@pytest.mark.skip(reason="This test is skipped for now")
def test_cli_run_benchmarking_refusal_adapter_prompt_injection_role_playing():

    # Generate a random number between 0 and 999,999,999 (inclusive)
    random_number = int(random.random() * 1000000000)
    dataset_module = "prompt_injection_role_playing"
    connector_name = "my-gpt4o"
    nameOfRunnerName = "my-benchmarking-" + connector_name + "-" + dataset_module + "-" + str(random_number)
    metric_module = "refusal_adapter"

    commands = [
        "export OPENAI_API_KEY="+OPENAI_TOKEN,
        "poetry run moonshot benchmark " + nameOfRunnerName + " "+dataset_module+" "+metric_module+" "+connector_name+""
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

    # Assert Results
    assert_run_outcome(output_lines)
@pytest.mark.skip(reason="This test is skipped for now")
def test_cli_run_benchmarking_refusal_adapter_sensitive_data_disclosure_general():

    # Generate a random number between 0 and 999,999,999 (inclusive)
    random_number = int(random.random() * 1000000000)
    dataset_module = "sensitive_data_disclosure_general"
    connector_name = "my-gpt4o"
    nameOfRunnerName = "my-benchmarking-" + connector_name + "-" + dataset_module + "-" + str(random_number)
    metric_module = "refusal_adapter"

    commands = [
        "export OPENAI_API_KEY="+OPENAI_TOKEN,
        "poetry run moonshot benchmark " + nameOfRunnerName + " "+dataset_module+" "+metric_module+" "+connector_name+""
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

    # Assert Results
    assert_run_outcome(output_lines)