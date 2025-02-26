import subprocess
from dotenv import load_dotenv
import os
import random

load_dotenv()  # Load environment variables from .env file

OPENAI_TOKEN = os.getenv('OPENAI_TOKEN')
MOON_V1_CLI_DIR = os.getenv('MOON_V1_CLI_DIR')

def assert_run_outcome(output_lines,test_run_name):
    # Get the last line of the output
    line_3 = output_lines[-3]
    line_3_expected = "successfully created with run_id:"
    line_2_1 = output_lines[-2] + output_lines[-1]
    line_2_1_expected = test_run_name
    print('=========================Output Last Line:', line_3)
    print('=========================Output Last Line:', line_2_1)
    assert line_3.replace(" ", "") == line_3_expected.replace(" ", "")
    assert line_2_1.replace(" ", "") == line_2_1_expected.replace(" ", "")

def test_cli_run_benchmarking_refusal_adapter_mmlu_mini():

    # Generate a random number between 0 and 999,999,999 (inclusive)
    random_number = int(random.random() * 1000000000)
    dataset_module = "mmlu-mini"
    nameOfRunnerName = "my-benchmarking-runner-"+dataset_module+"-" + str(random_number)
    metric_module = "refusal_adapter"
    connector_name = "my-gpt4o"

    commands = [
        "export OPENAI_API_KEY="+OPENAI_TOKEN,
        "poetry run python __main__.py create-benchmark-test " + nameOfRunnerName + " "+dataset_module+" "+metric_module+" "+connector_name+""
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
    #Assert Results
    # Get the last line of the output
    line_13 = output_lines[-13]
    line_13_expected = "File written"
    line_12 = output_lines[-12]
    line_12_expected = "successfully at:"
    line_11 = output_lines[-11]
    line_11_expected = "data/results/my-benchm"
    print('=========================Output Last Line:', line_13)
    print('=========================Output Last Line:', line_12)
    print('=========================Output Last Line:', line_11)
    assert line_13.replace(" ", "") == line_13_expected.replace(" ", "")
    assert line_12.replace(" ", "") == line_12_expected.replace(" ", "")
    assert line_11.replace(" ", "") == line_11_expected.replace(" ", "")
    assert_run_outcome(output_lines,nameOfRunnerName)

def test_cli_run_benchmarking_refusal_adapter_prompt_injection_obfuscation():

    # Generate a random number between 0 and 999,999,999 (inclusive)
    random_number = int(random.random() * 1000000000)
    dataset_module = "prompt_injection_obfuscation"
    nameOfRunnerName = "my-benchmarking-runner-"+dataset_module+"-" + str(random_number)
    metric_module = "refusal_adapter"
    connector_name = "my-gpt4o"

    commands = [
        "export OPENAI_API_KEY="+OPENAI_TOKEN,
        "poetry run python __main__.py create-benchmark-test " + nameOfRunnerName + " "+dataset_module+" "+metric_module+" "+connector_name+""
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
    assert_run_outcome(output_lines, nameOfRunnerName)

def test_cli_run_benchmarking_refusal_adapter_prompt_injection_payload_splitting():

    # Generate a random number between 0 and 999,999,999 (inclusive)
    random_number = int(random.random() * 1000000000)
    dataset_module = "prompt_injection_payload_splitting"
    nameOfRunnerName = "my-benchmarking-runner-"+dataset_module+"-" + str(random_number)
    metric_module = "refusal_adapter"
    connector_name = "my-gpt4o"

    commands = [
        "export OPENAI_API_KEY="+OPENAI_TOKEN,
        "poetry run python __main__.py create-benchmark-test " + nameOfRunnerName + " "+dataset_module+" "+metric_module+" "+connector_name+""
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
    # Get the last line of the output
    line_4 = output_lines[-4]
    line_4_expected = "successfully created with run_id:"
    line_3_2_1 = output_lines[-3]+output_lines[-2] + output_lines[-1]
    line_3_2_1_expected = nameOfRunnerName
    print('=========================Output Last Line:', line_4)
    print('=========================Output Last Line:', line_3_2_1)
    assert line_4.replace(" ", "") == line_4_expected.replace(" ", "")
    assert line_3_2_1.replace(" ", "") == line_3_2_1_expected.replace(" ", "")

def test_cli_run_benchmarking_refusal_adapter_prompt_injection_role_playing():

    # Generate a random number between 0 and 999,999,999 (inclusive)
    random_number = int(random.random() * 1000000000)
    dataset_module = "prompt_injection_role_playing"
    nameOfRunnerName = "my-benchmarking-runner-"+dataset_module+"-" + str(random_number)
    metric_module = "refusal_adapter"
    connector_name = "my-gpt4o"

    commands = [
        "export OPENAI_API_KEY="+OPENAI_TOKEN,
        "poetry run python __main__.py create-benchmark-test " + nameOfRunnerName + " "+dataset_module+" "+metric_module+" "+connector_name+""
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
    assert_run_outcome(output_lines, nameOfRunnerName)

def test_cli_run_benchmarking_refusal_adapter_sensitive_data_disclosure_general():

    # Generate a random number between 0 and 999,999,999 (inclusive)
    random_number = int(random.random() * 1000000000)
    dataset_module = "sensitive_data_disclosure_general"
    nameOfRunnerName = "my-benchmarking-runner-"+dataset_module+"-" + str(random_number)
    metric_module = "refusal_adapter"
    connector_name = "my-gpt4o"

    commands = [
        "export OPENAI_API_KEY="+OPENAI_TOKEN,
        "poetry run python __main__.py create-benchmark-test " + nameOfRunnerName + " "+dataset_module+" "+metric_module+" "+connector_name+""
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
    assert_run_outcome(output_lines, nameOfRunnerName)