import random
import time

import pytest
import subprocess
from dotenv import load_dotenv
import os
import shutil
import random
from util.utils import *

load_dotenv()  # Load environment variables from .env file

OPENAI_URI = os.getenv('OPENAI_URI')
OPENAI_TOKEN = os.getenv('OPENAI_TOKEN')
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

    file_path = str(CLI_DIR) + "/moonshot-data-aisi/generated-outputs/runners/" + nameOfRunnerFileName + ".json"

    # Update Endpoints
    command = 'update_endpoint openai-gpt4o "[(\'name\', \'OpenAI GPT4o\'), (\'uri\', \'' + str(
        OPENAI_URI) + '\'), (\'token\', \'' + str(
        OPENAI_TOKEN) + '\'), (\'model\', \'gpt-4o\'), (\'params\', {\'timeout\': 300,\'max_attempts\': 3, \'temperature\': 0.5})]"\n'
    print('Command:', command)
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    command = 'new_session ' + nameOfRunnerFileName + ' -e "[\'openai-gpt4o\']" -c add_previous_prompt -p mmlu \n'
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
        # cwd="/Users/jacksonboey/PycharmProjects/moonshot",
        # /home/runner/work/moonshot-data/moonshot-data for moonshot data repo
        # /home/runner/work/moonshot/moonshot-data for moonshot repo
    )
    print('Path:', str(CLI_DIR))
    # Ensure process.stdin is not None
    if process.stdin is None:
        raise RuntimeError("Failed to create stdin for the subprocess")

    # Generate a random number between 0 and 999,999,999 (inclusive)
    random_number = int(random.random() * 1000000000)
    nameOfRunnerFileName = "my-red-teaming-runner-" + str(random_number)

    # Update Endpoints
    command = 'update_endpoint openai-gpt4o "[(\'name\', \'OpenAI GPT4o\'), (\'uri\', \'' + str(
        OPENAI_URI) + '\'), (\'token\', \'' + str(
        OPENAI_TOKEN) + '\'), (\'model\', \'gpt-4o\'), (\'params\', {\'timeout\': 300,\'max_attempts\': 3, \'temperature\': 0.5})]"\n'
    print('Command:', command)
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    command = 'new_session ' + nameOfRunnerFileName + ' -e "[\'openai-gpt4o\']" -c add_previous_prompt -p mmlu \n'
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    process.stdin.write('run_attack_module charswap_attack "this is my prompt"\n')
    process.stdin.flush()

    process.stdin.write('add_bookmark openai-gpt4o 1 my-bookmarked-prompt' + str(random_number) + '\n')
    process.stdin.flush()

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

    # Check if "Bookmark List" exists
    bookmark_keyword_found = False
    for line in output_lines:
        if "Bookmark List" in line:
            bookmark_keyword_found = True
            print("Found 'Bookmark List' in line:", line)
            break

    if not bookmark_keyword_found:
        print("'Bookmark List' not found.")

    assert bookmark_keyword_found == True


def test_cli_list_context_strategies():
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

    # Update Endpoints
    command = 'update_endpoint openai-gpt4o "[(\'name\', \'OpenAI GPT4o\'), (\'uri\', \'' + str(
        OPENAI_URI) + '\'), (\'token\', \'' + str(
        OPENAI_TOKEN) + '\'), (\'model\', \'gpt-4o\'), (\'params\', {\'timeout\': 300,\'max_attempts\': 3, \'temperature\': 0.5})]"\n'
    print('Command:', command)
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    command = 'new_session ' + nameOfRunnerFileName + ' -e "[\'openai-gpt4o\']" -c add_previous_prompt -p mmlu \n'
    print('command2:', command)
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
    last_line = output_lines[30]
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

    # Update Endpoints
    command = 'update_endpoint openai-gpt4o "[(\'name\', \'OpenAI GPT4o\'), (\'uri\', \'' + str(
        OPENAI_URI) + '\'), (\'token\', \'' + str(
        OPENAI_TOKEN) + '\'), (\'model\', \'gpt-4o\'), (\'params\', {\'timeout\': 300,\'max_attempts\': 3, \'temperature\': 0.5})]"\n'
    print('Command:', command)
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    command = 'new_session ' + nameOfRunnerFileName + ' -e "[\'openai-gpt4o\']" -c add_previous_prompt -p mmlu \n'
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    process.stdin.write('run_attack_module charswap_attack "this is my prompt"\n')
    process.stdin.flush()

    process.stdin.write('add_bookmark openai-gpt4o 1 my-bookmarked-prompt' + str(random_number))
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

    # Update Endpoints
    command = 'update_endpoint openai-gpt4o "[(\'name\', \'OpenAI GPT4o\'), (\'uri\', \'' + str(
        OPENAI_URI) + '\'), (\'token\', \'' + str(
        OPENAI_TOKEN) + '\'), (\'model\', \'gpt-4o\'), (\'params\', {\'timeout\': 300,\'max_attempts\': 3, \'temperature\': 0.5})]"\n'
    print('Command:', command)
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    command = 'new_session ' + nameOfRunnerFileName + ' -e "[\'openai-gpt4o\']" -c add_previous_prompt -p mmlu \n'
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    process.stdin.write('run_attack_module charswap_attack "this is my prompt"\n')
    process.stdin.flush()

    process.stdin.write('add_bookmark openai-gpt4o 1 my-bookmarked-prompt' + str(random_number) + '\n')
    process.stdin.flush()

    process.stdin.write('delete_bookmark my-bookmarked-prompt' + str(random_number) + '\n')
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


def test_cli_delete_attack_module():
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
        # cwd="/Users/jacksonboey/PycharmProjects/moonshot",
        # /home/runner/work/moonshot-data/moonshot-data for moonshot data repo
        # /home/runner/work/moonshot/moonshot-data for moonshot repo
    )
    print('Path:', str(CLI_DIR))
    # Ensure process.stdin is not None
    if process.stdin is None:
        raise RuntimeError("Failed to create stdin for the subprocess")

    # Copy file
    copy_file(CLI_DIR + '/moonshot-data-aisi/attack-modules/sample_attack_module.py')

    command = ('delete_attack_module sample_attack_module\n')
    print('Command:', command)
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    command = ('y\n')
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
    last_line = output_lines[-2]

    # Restore file
    current_path = CLI_DIR + "/moonshot-data-aisi/attack-modules/copy_of_sample_attack_module.py"  # Replace with the current file path
    new_name = "sample_attack_module.py"  # Specify the new file name
    rename_file(current_path, new_name)

    print('=========================Output Last Line:', last_line)
    assert last_line == "Are you sure you want to delete the attack module (y/N)? [delete_attack_module]: Attack module deleted."


def test_cli_delete_context_strategy():
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
        # cwd="/Users/jacksonboey/PycharmProjects/moonshot",
        # /home/runner/work/moonshot-data/moonshot-data for moonshot data repo
        # /home/runner/work/moonshot/moonshot-data for moonshot repo
    )
    print('Path:', str(CLI_DIR))
    # Ensure process.stdin is not None
    if process.stdin is None:
        raise RuntimeError("Failed to create stdin for the subprocess")

    # Copy file
    copy_file(CLI_DIR + '/moonshot-data-aisi/context-strategy/add_previous_prompt.py')

    command = ('delete_context_strategy add_previous_prompt\n')
    print('Command:', command)
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    command = ('y\n')
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
    last_line = output_lines[-2]

    # Restore file
    current_path = CLI_DIR + "/moonshot-data-aisi/context-strategy/copy_of_add_previous_prompt.py"  # Replace with the current file path
    new_name = "add_previous_prompt.py"  # Specify the new file name
    rename_file(current_path, new_name)

    print('=========================Output Last Line:', last_line)
    assert last_line == "Are you sure you want to delete the context strategy (y/N)? [delete_context_strategy]: Context strategy deleted."


def test_cli_delete_session():
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

    # Update Endpoints
    command = 'update_endpoint openai-gpt4o "[(\'name\', \'OpenAI GPT4o\'), (\'uri\', \'' + str(
        OPENAI_URI) + '\'), (\'token\', \'' + str(
        OPENAI_TOKEN) + '\'), (\'model\', \'gpt-4o\'), (\'params\', {\'timeout\': 300,\'max_attempts\': 3, \'temperature\': 0.5})]"\n'
    print('Command:', command)
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    # Generate a random number between 0 and 999,999,999 (inclusive)
    random_number = int(random.random() * 1000000000)
    nameOfRunnerFileName = "my-red-teaming-runner-" + str(random_number)

    command = 'new_session ' + nameOfRunnerFileName + ' -e "[\'openai-gpt4o\']" -c add_previous_prompt -p mmlu \n'
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    # Example command to send to the process
    process.stdin.write('delete_session ' + nameOfRunnerFileName + '\n')
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
    assert last_line == "Are you sure you want to delete the session (y/N)? [delete_session]: Session deleted."


def test_cli_end_session():
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

    # Update Endpoints
    command = 'update_endpoint openai-gpt4o "[(\'name\', \'OpenAI GPT4o\'), (\'uri\', \'' + str(
        OPENAI_URI) + '\'), (\'token\', \'' + str(
        OPENAI_TOKEN) + '\'), (\'model\', \'gpt-4o\'), (\'params\', {\'timeout\': 300,\'max_attempts\': 3, \'temperature\': 0.5})]"\n'
    print('Command:', command)
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    # Generate a random number between 0 and 999,999,999 (inclusive)
    random_number = int(random.random() * 1000000000)
    nameOfRunnerFileName = "my-red-teaming-runner-" + str(random_number)

    command = 'new_session ' + nameOfRunnerFileName + ' -e "[\'openai-gpt4o\']" -c add_previous_prompt -p mmlu \n'
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    # Example command to send to the process
    process.stdin.write('end_session \n')
    process.stdin.flush()

    process.stdin.write('clear_context_strategy\n')
    process.stdin.flush()

    # Capture the output and errors
    stdout, stderr = process.communicate()

    print('Output:', stdout)
    # Split the output into lines
    output_lines = stdout.splitlines()

    # Get the last line of the output
    last_line = output_lines[-2]

    print('=========================Output Last Line:', last_line)
    assert last_line == "There is no active session. Activate a session to send a prompt with a context strategy."

def test_cli_export_bookmarks():
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

    # Update Endpoints
    command = 'update_endpoint openai-gpt4o "[(\'name\', \'OpenAI GPT4o\'), (\'uri\', \'' + str(
        OPENAI_URI) + '\'), (\'token\', \'' + str(
        OPENAI_TOKEN) + '\'), (\'model\', \'gpt-4o\'), (\'params\', {\'timeout\': 300,\'max_attempts\': 3, \'temperature\': 0.5})]"\n'
    print('Command:', command)
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    command = 'new_session ' + nameOfRunnerFileName + ' -e "[\'openai-gpt4o\']" -c add_previous_prompt -p mmlu \n'
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    process.stdin.write('run_attack_module charswap_attack "this is my prompt"\n')
    process.stdin.flush()

    process.stdin.write('add_bookmark openai-gpt4o 1 my-bookmarked-prompt' + str(random_number) + '\n')
    process.stdin.flush()

    Export_File_Name = 'my_list_of_exported_bookmarks_' + str(random_number)
    process.stdin.write('export_bookmarks \"' + Export_File_Name + '\"\n')
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
    assert 'Bookmarks exported successfully. Written to: moonshot-data-aisi/generated-outputs/bookmarks/' + Export_File_Name + '.json' == last_line # Uncomment before commit
    # assert 'Bookmarks exported successfully. Written to: moonshot-data-aisi\\generated-outputs\\bookmarks\\' + Export_File_Name + '.json' == last_line # Local Windows


def test_cli_use_bookmark():
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

    # Update Endpoints
    command = 'update_endpoint openai-gpt4o "[(\'name\', \'OpenAI GPT4o\'), (\'uri\', \'' + str(
        OPENAI_URI) + '\'), (\'token\', \'' + str(
        OPENAI_TOKEN) + '\'), (\'model\', \'gpt-4o\'), (\'params\', {\'timeout\': 300,\'max_attempts\': 3, \'temperature\': 0.5})]"\n'
    print('Command:', command)
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    command = 'new_session ' + nameOfRunnerFileName + ' -e "[\'openai-gpt4o\']" -c add_previous_prompt -p mmlu \n'
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    process.stdin.write('run_attack_module charswap_attack "this is my prompt"\n')
    process.stdin.flush()

    process.stdin.write('add_bookmark openai-gpt4o 1 my-bookmarked-prompt' + str(random_number) + '\n')
    process.stdin.flush()

    process.stdin.write('use_bookmark my-bookmarked-prompt' + str(random_number))
    process.stdin.flush()

    # Capture the output and errors
    stdout, stderr = process.communicate()

    print('Output:', stdout)
    # Split the output into lines

    output_lines = stdout.splitlines()

    # Get the fourth line of the output
    last_line = output_lines[-4]
    print('=========================Output Last Line:', last_line)
    # Assert that '1' is present in the string
    assert 'Copy this command and paste it below:' == last_line


def test_cli_use_bookmark():
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

    # Update Endpoints
    command = 'update_endpoint openai-gpt4o "[(\'name\', \'OpenAI GPT4o\'), (\'uri\', \'' + str(
        OPENAI_URI) + '\'), (\'token\', \'' + str(
        OPENAI_TOKEN) + '\'), (\'model\', \'gpt-4o\'), (\'params\', {\'timeout\': 300,\'max_attempts\': 3, \'temperature\': 0.5})]"\n'
    print('Command:', command)
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    command = 'new_session ' + nameOfRunnerFileName + ' -e "[\'openai-gpt4o\']" -c add_previous_prompt -p mmlu \n'
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    process.stdin.write('run_attack_module charswap_attack "this is my prompt"\n')
    process.stdin.flush()

    process.stdin.write('add_bookmark openai-gpt4o 1 my-bookmarked-prompt' + str(random_number) + '\n')
    process.stdin.flush()

    process.stdin.write('use_bookmark my-bookmarked-prompt' + str(random_number))
    process.stdin.flush()

    # Capture the output and errors
    stdout, stderr = process.communicate()

    print('Output:', stdout)
    # Split the output into lines

    output_lines = stdout.splitlines()

    # Get the fourth line of the output
    last_line = output_lines[-4]
    print('=========================Output Last Line:', last_line)
    # Assert that '1' is present in the string
    assert 'Copy this command and paste it below:' == last_line


def test_cli_use_context_strategy():
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

    # Generate a random number between 0 and 999,999,999 (inclusive)
    random_number = int(random.random() * 1000000000)
    nameOfRunnerFileName = "my-red-teaming-runner-" + str(random_number)
    file_path = str(CLI_DIR) + "/moonshot-data-aisi/generated-outputs/runners/" + nameOfRunnerFileName + ".json"

    # Update Endpoints
    command = 'update_endpoint openai-gpt4o "[(\'name\', \'OpenAI GPT4o\'), (\'uri\', \'' + str(
        OPENAI_URI) + '\'), (\'token\', \'' + str(
        OPENAI_TOKEN) + '\'), (\'model\', \'gpt-4o\'), (\'params\', {\'timeout\': 300,\'max_attempts\': 3, \'temperature\': 0.5})]"\n'
    print('Command:', command)
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    command = 'new_session ' + nameOfRunnerFileName + ' -e "[\'openai-gpt4o\']" -c add_previous_prompt -p mmlu \n'
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    process.stdin.write('use_context_strategy add_previous_prompt\n')
    process.stdin.flush()

    process.stdin.write('run_attack_module charswap_attack "this is my prompt"\n')
    process.stdin.flush()

    # Capture the output and errors
    stdout, stderr = process.communicate()

    print('Output:', stdout)
    # Split the output into lines

    output_lines = stdout.splitlines()

    # Get the fourth line of the output
    last_line = output_lines[23]
    print('=========================Output Last Line:', last_line)
    # Assert that '1' is present in the string
    assert 'Updated session: ' + nameOfRunnerFileName + '. Context Strategy: add_previous_prompt.No. of previous prompts for Context Strategy: 5.' == last_line

    if os.path.exists(file_path):
        print(f"File exists: {file_path}")
        assert True


    else:
        print(f"File does not exist: {file_path}")
        pytest.fail()


def test_cli_use_prompt_template():
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

    # Generate a random number between 0 and 999,999,999 (inclusive)
    random_number = int(random.random() * 1000000000)
    nameOfRunnerFileName = "my-red-teaming-runner-" + str(random_number)
    file_path = str(CLI_DIR) + "/moonshot-data-aisi/generated-outputs/runners/" + nameOfRunnerFileName + ".json"

    # Update Endpoints
    command = 'update_endpoint openai-gpt4o "[(\'name\', \'OpenAI GPT4o\'), (\'uri\', \'' + str(
        OPENAI_URI) + '\'), (\'token\', \'' + str(
        OPENAI_TOKEN) + '\'), (\'model\', \'gpt-4o\'), (\'params\', {\'timeout\': 300,\'max_attempts\': 3, \'temperature\': 0.5})]"\n'
    print('Command:', command)
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    command = 'new_session ' + nameOfRunnerFileName + ' -e "[\'openai-gpt4o\']" -c add_previous_prompt -p mmlu \n'
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    process.stdin.write('use_prompt_template \'analogical-similarity\'\n')
    process.stdin.flush()

    process.stdin.write('run_attack_module charswap_attack "this is my prompt"\n')
    process.stdin.flush()

    # Capture the output and errors
    stdout, stderr = process.communicate()

    print('Output:', stdout)
    # Split the output into lines

    output_lines = stdout.splitlines()

    # Get the fourth line of the output
    last_line = output_lines[23]
    print('=========================Output Last Line:', last_line)
    # Assert that '1' is present in the string
    assert 'Updated session: ' + nameOfRunnerFileName + '. Prompt Template: analogical-similarity.' == last_line

    if os.path.exists(file_path):
        print(f"File exists: {file_path}")
        assert True


    else:
        print(f"File does not exist: {file_path}")
        pytest.fail()


def test_cli_use_session():
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

    # Generate a random number between 0 and 999,999,999 (inclusive)
    random_number = int(random.random() * 1000000000)
    nameOfRunnerFileName = "my-red-teaming-runner-" + str(random_number)
    file_path = str(CLI_DIR) + "/moonshot-data-aisi/generated-outputs/runners/" + nameOfRunnerFileName + ".json"

    # Update Endpoints
    command = 'update_endpoint openai-gpt4o "[(\'name\', \'OpenAI GPT4o\'), (\'uri\', \'' + str(
        OPENAI_URI) + '\'), (\'token\', \'' + str(
        OPENAI_TOKEN) + '\'), (\'model\', \'gpt-4o\'), (\'params\', {\'timeout\': 300,\'max_attempts\': 3, \'temperature\': 0.5})]"\n'
    print('Command:', command)
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    command = 'new_session ' + nameOfRunnerFileName + ' -e "[\'openai-gpt4o\']" -c add_previous_prompt -p mmlu \n'
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    process.stdin.write('end_session\n')
    process.stdin.flush()

    process.stdin.write('use_session \'' + nameOfRunnerFileName + '\'\n')
    process.stdin.flush()

    process.stdin.write('run_attack_module charswap_attack "this is my prompt"\n')
    process.stdin.flush()

    # Capture the output and errors
    stdout, stderr = process.communicate()

    print('Output:', stdout)
    # Split the output into lines

    output_lines = stdout.splitlines()

    # Get the fourth line of the output
    last_line = output_lines[23]
    print('=========================Output Last Line:', last_line)
    assert "Usingsession:" + nameOfRunnerFileName + "." == last_line.replace(" ", "")

    if os.path.exists(file_path):
        print(f"File exists: {file_path}")
        assert True


    else:
        print(f"File does not exist: {file_path}")
        pytest.fail()


def test_cli_view_bookmark():
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

    # Update Endpoints
    command = 'update_endpoint openai-gpt4o "[(\'name\', \'OpenAI GPT4o\'), (\'uri\', \'' + str(
        OPENAI_URI) + '\'), (\'token\', \'' + str(
        OPENAI_TOKEN) + '\'), (\'model\', \'gpt-4o\'), (\'params\', {\'timeout\': 300,\'max_attempts\': 3, \'temperature\': 0.5})]"\n'
    print('Command:', command)
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    command = 'new_session ' + nameOfRunnerFileName + ' -e "[\'openai-gpt4o\']" -c add_previous_prompt -p mmlu \n'
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    process.stdin.write('run_attack_module charswap_attack "this is my prompt"\n')
    process.stdin.flush()

    process.stdin.write('add_bookmark openai-gpt4o 1 my-bookmarked-prompt' + str(random_number) + '\n')
    process.stdin.flush()

    process.stdin.write('view_bookmark my-bookmarked-prompt' + str(random_number) + '\n')
    process.stdin.flush()
    # Capture the output and errors
    stdout, stderr = process.communicate()

    print('Output:', stdout)
    # Split the output into lines

    output_lines = stdout.splitlines()

    print('=========================Output Last Line:', output_lines)
    for index,line in enumerate(output_lines):
        # Remove spaces and check if it matches 'Bookmark List'
        if line.replace(" ", "") == 'BookmarkList':  # Remove spaces and check if it matches exactly
            found_bookmark_list = True
            assert True
            break  # No need to check further if found

        if (index == len(output_lines) - 1) & (line.replace(" ", "") != 'BookmarkList'):
            pytest.fail()

def test_cli_clear_context_strategy():
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

    # Generate a random number between 0 and 999,999,999 (inclusive)
    random_number = int(random.random() * 1000000000)
    nameOfRunnerFileName = "my-red-teaming-runner-" + str(random_number)
    file_path = str(CLI_DIR) + "/moonshot-data-aisi/generated-outputs/runners/" + nameOfRunnerFileName + ".json"

    # Update Endpoints
    command = 'update_endpoint openai-gpt4o "[(\'name\', \'OpenAI GPT4o\'), (\'uri\', \'' + str(
        OPENAI_URI) + '\'), (\'token\', \'' + str(
        OPENAI_TOKEN) + '\'), (\'model\', \'gpt-4o\'), (\'params\', {\'timeout\': 300,\'max_attempts\': 3, \'temperature\': 0.5})]"\n'
    print('Command:', command)
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    command = 'new_session ' + nameOfRunnerFileName + ' -e "[\'openai-gpt4o\']" -c add_previous_prompt -p mmlu \n'
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    process.stdin.write('use_context_strategy add_previous_prompt\n')
    process.stdin.flush()

    process.stdin.write('clear_context_strategy\n')
    process.stdin.flush()

    process.stdin.write('run_attack_module charswap_attack "this is my prompt"\n')
    process.stdin.flush()

    # Capture the output and errors
    stdout, stderr = process.communicate()

    print('Output:', stdout)
    # Split the output into lines

    output_lines = stdout.splitlines()

    # Get the fourth line of the output
    last_line = output_lines[24]
    print('=========================Output Last Line:', last_line)
    # Assert that '1' is present in the string
    assert 'Cleared context strategy.' == last_line

    if os.path.exists(file_path):
        print(f"File exists: {file_path}")
        assert True


    else:
        print(f"File does not exist: {file_path}")
        pytest.fail()

def test_cli_clear_prompt_template():
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

    # Generate a random number between 0 and 999,999,999 (inclusive)
    random_number = int(random.random() * 1000000000)
    nameOfRunnerFileName = "my-red-teaming-runner-" + str(random_number)
    file_path = str(CLI_DIR) + "/moonshot-data-aisi/generated-outputs/runners/" + nameOfRunnerFileName + ".json"

    # Update Endpoints
    command = 'update_endpoint openai-gpt4o "[(\'name\', \'OpenAI GPT4o\'), (\'uri\', \'' + str(
        OPENAI_URI) + '\'), (\'token\', \'' + str(
        OPENAI_TOKEN) + '\'), (\'model\', \'gpt-4o\'), (\'params\', {\'timeout\': 300,\'max_attempts\': 3, \'temperature\': 0.5})]"\n'
    print('Command:', command)
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    command = 'new_session ' + nameOfRunnerFileName + ' -e "[\'openai-gpt4o\']" -c add_previous_prompt -p mmlu \n'
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    process.stdin.write('use_prompt_template \'analogical-similarity\'\n')
    process.stdin.flush()

    process.stdin.write('clear_prompt_template\n')
    process.stdin.flush()

    process.stdin.write('run_attack_module charswap_attack "this is my prompt"\n')
    process.stdin.flush()

    # Capture the output and errors
    stdout, stderr = process.communicate()

    print('Output:', stdout)
    # Split the output into lines

    output_lines = stdout.splitlines()

    # Get the fourth line of the output
    last_line = output_lines[24]
    print('=========================Output Last Line:', last_line)
    # Assert that '1' is present in the string
    assert 'Cleared prompt template.' == last_line

    if os.path.exists(file_path):
        print(f"File exists: {file_path}")
        assert True


    else:
        print(f"File does not exist: {file_path}")
        pytest.fail()
