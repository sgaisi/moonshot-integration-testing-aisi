import random

import pytest
import subprocess
from dotenv import load_dotenv
import os

import random

load_dotenv()  # Load environment variables from .env file

AZURE_OPENAI_URI = os.getenv('AZURE_OPENAI_URI')
AZURE_OPENAI_TOKEN = os.getenv('AZURE_OPENAI_TOKEN')
CLI_DIR = '/Users/jacksonboey/PycharmProjects/moonshot'


# CLI_DIR = os.getenv('CLI_DIR')
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

    file_path = str(CLI_DIR) + "/moonshot-data/generated-outputs/runners/" + nameOfRunnerFileName + ".json"

    # # Example command to send to the process
    # process.stdin.write('use_session "my-runner"\n')
    # process.stdin.flush()

    command = 'new_session ' + nameOfRunnerFileName + ' -e "[\'ollama-llama3\']" -c add_previous_prompt -p mmlu \n'
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


def test_cli_list_attack_modules():
    command = (
        'cd .. &&'
        'source venv/bin/activate &&'
        'cd moonshot &&'
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
        # cwd="/Users/jacksonboey/PycharmProjects/moonshot",
        # /home/runner/work/moonshot-data/moonshot-data for moonshot data repo
        # /home/runner/work/moonshot/moonshot-data for moonshot repo
    )
    print('Path:', str(CLI_DIR))
    # Ensure process.stdin is not None
    if process.stdin is None:
        raise RuntimeError("Failed to create stdin for the subprocess")

    command = ('list_attack_modules\n')
    print('Command:', command)
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    # Capture the output and errors
    stdout, stderr = process.communicate()

    print('Output:', stdout)
    # Split the output into lines
    output_lines = stdout.splitlines()

    # Get the last line of the output
    last_line = output_lines[12]
    print('=========================Output Last Line:', last_line)
    assert last_line.replace(" ", "") == "AttackModuleList"


def test_cli_list_bookmarks():
    command = (
        'cd .. &&'
        'source venv/bin/activate &&'
        'cd moonshot &&'
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
        # cwd="/Users/jacksonboey/PycharmProjects/moonshot",
        # /home/runner/work/moonshot-data/moonshot-data for moonshot data repo
        # /home/runner/work/moonshot/moonshot-data for moonshot repo
    )
    print('Path:', str(CLI_DIR))
    # Ensure process.stdin is not None
    if process.stdin is None:
        raise RuntimeError("Failed to create stdin for the subprocess")

    command = ('list_bookmarks\n')
    print('Command:', command)
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    # Capture the output and errors
    stdout, stderr = process.communicate()

    print('Output:', stdout)
    # Split the output into lines
    output_lines = stdout.splitlines()

    # Get the last line of the output
    last_line = output_lines[11]
    print('=========================Output Last Line:', last_line)
    assert last_line.replace(" ", "") == "BookmarkList"


def test_cli_list_context_strategies():
    command = (
        'cd .. &&'
        'source venv/bin/activate &&'
        'cd moonshot &&'
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
        # cwd="/Users/jacksonboey/PycharmProjects/moonshot",
        # /home/runner/work/moonshot-data/moonshot-data for moonshot data repo
        # /home/runner/work/moonshot/moonshot-data for moonshot repo
    )
    print('Path:', str(CLI_DIR))
    # Ensure process.stdin is not None
    if process.stdin is None:
        raise RuntimeError("Failed to create stdin for the subprocess")

    command = ('list_context_strategies\n')
    print('Command:', command)
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    # Capture the output and errors
    stdout, stderr = process.communicate()

    print('Output:', stdout)
    # Split the output into lines
    output_lines = stdout.splitlines()

    # Get the last line of the output
    last_line = output_lines[11]
    print('=========================Output Last Line:', last_line)
    assert last_line.replace(" ", "") == "ContextStrategyList"


def test_cli_list_sessions():
    command = (
        'cd .. &&'
        'source venv/bin/activate &&'
        'cd moonshot &&'
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
        # cwd="/Users/jacksonboey/PycharmProjects/moonshot",
        # /home/runner/work/moonshot-data/moonshot-data for moonshot data repo
        # /home/runner/work/moonshot/moonshot-data for moonshot repo
    )
    print('Path:', str(CLI_DIR))
    # Ensure process.stdin is not None
    if process.stdin is None:
        raise RuntimeError("Failed to create stdin for the subprocess")

    command = ('list_sessions\n')
    print('Command:', command)
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    # Capture the output and errors
    stdout, stderr = process.communicate()

    print('Output:', stdout)
    # Split the output into lines
    output_lines = stdout.splitlines()

    # Get the last line of the output
    last_line = output_lines[11]
    print('=========================Output Last Line:', last_line)
    assert last_line.replace(" ", "") == "SessionList"


def test_cli_show_prompts():
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

    # # Example command to send to the process
    # process.stdin.write('use_session "my-runner"\n')
    # process.stdin.flush()

    command = 'new_session ' + nameOfRunnerFileName + ' -e "[\'ollama-llama3\']" -c add_previous_prompt -p mmlu \n'
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    process.stdin.write('run_attack_module charswap_attack "this is my prompt"\n')
    process.stdin.flush()

    process.stdin.write('show_prompts')
    process.stdin.flush()

    # Capture the output and errors
    stdout, stderr = process.communicate()

    print('Output:', stdout)
    # Split the output into lines

    output_lines = stdout.splitlines()

    # Get the last line of the output
    last_line = output_lines[29]
    print('=========================Output Last Line:', last_line)
    # Assert that '1' is present in the string
    assert '1' in last_line

def test_cli_add_bookmark():
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

    # # Example command to send to the process
    # process.stdin.write('use_session "my-runner"\n')
    # process.stdin.flush()

    command = 'new_session ' + nameOfRunnerFileName + ' -e "[\'ollama-llama3\']" -c add_previous_prompt -p mmlu \n'
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    process.stdin.write('run_attack_module charswap_attack "this is my prompt"\n')
    process.stdin.flush()

    process.stdin.write('add_bookmark ollama-llama3 1 my-bookmarked-prompt'+ str(random_number))
    process.stdin.flush()

    # Capture the output and errors
    stdout, stderr = process.communicate()

    print('Output:', stdout)
    # Split the output into lines

    output_lines = stdout.splitlines()

    # Get the last line of the output
    last_line = output_lines[-2]
    print('=========================Output Last Line:', last_line)
    # Assert that '1' is present in the string
    assert '[bookmark_prompt]: [Bookmark] Bookmark added successfully.' == last_line

def test_cli_delete_bookmark():
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

    # # Example command to send to the process
    # process.stdin.write('use_session "my-runner"\n')
    # process.stdin.flush()

    command = 'new_session ' + nameOfRunnerFileName + ' -e "[\'ollama-llama3\']" -c add_previous_prompt -p mmlu \n'
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    process.stdin.write('run_attack_module charswap_attack "this is my prompt"\n')
    process.stdin.flush()

    process.stdin.write('add_bookmark ollama-llama3 1 my-bookmarked-prompt'+ str(random_number)+'\n')
    process.stdin.flush()

    process.stdin.write('delete_bookmark my-bookmarked-prompt' + str(random_number)+'\n')
    process.stdin.flush()

    process.stdin.write('y\n')
    process.stdin.flush()

    # Capture the output and errors
    stdout, stderr = process.communicate()

    print('Output:', stdout)
    # Split the output into lines

    output_lines = stdout.splitlines()

    # Get the last line of the output
    last_line = output_lines[-2]
    print('=========================Output Last Line:', last_line)
    # Assert that '1' is present in the string
    assert 'Are you sure you want to delete the bookmark (y/N)? [delete_bookmark]: [Bookmark] Bookmark record deleted.' == last_line