import random
import time

import pytest
import subprocess
from dotenv import load_dotenv
import os
import shutil
import random

load_dotenv()  # Load environment variables from .env file

AZURE_OPENAI_URI = os.getenv('AZURE_OPENAI_URI')
AZURE_OPENAI_TOKEN = os.getenv('AZURE_OPENAI_TOKEN')
# CLI_DIR = '/Users/jacksonboey/PycharmProjects/moonshot'
CLI_DIR = os.getenv('CLI_DIR')

def copy_file(file_path):
    # Get the file name and directory path
    directory, filename = os.path.split(file_path)

    # Create a new file name by appending "_copy" to the original file name
    new_filename = f"copy_of_{filename}"

    # Create the full path for the new file
    new_file_path = os.path.join(directory, new_filename)

    # Copy the file to the new location
    shutil.copy(file_path, new_file_path)

    print(f"File copied to: {new_file_path}")


def rename_file(current_path, new_name):
    # Get the directory path from the current file path
    directory = os.path.dirname(current_path)

    # Create the new file path with the new name
    new_file_path = os.path.join(directory, new_name)

    # Rename the file
    os.rename(current_path, new_file_path)

    print(f"File renamed to: {new_file_path}")
    return new_file_path  # Optionally return the new file path


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

    process.stdin.write('add_bookmark ollama-llama3 1 my-bookmarked-prompt' + str(random_number))
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

    process.stdin.write('add_bookmark ollama-llama3 1 my-bookmarked-prompt' + str(random_number) + '\n')
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

    # Copy file
    copy_file(CLI_DIR + '/moonshot-data/attack-modules/sample_attack_module.py')

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
    current_path = CLI_DIR + "/moonshot-data/attack-modules/copy_of_sample_attack_module.py"  # Replace with the current file path
    new_name = "sample_attack_module.py"  # Specify the new file name
    rename_file(current_path, new_name)

    print('=========================Output Last Line:', last_line)
    assert last_line == "Are you sure you want to delete the attack module (y/N)? [delete_attack_module]: Attack module deleted."


def test_cli_delete_context_strategy():
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

    # Copy file
    copy_file(CLI_DIR + '/moonshot-data/context-strategy/add_previous_prompt.py')

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
    current_path = CLI_DIR + "/moonshot-data/context-strategy/copy_of_add_previous_prompt.py"  # Replace with the current file path
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

    # # Example command to send to the process
    # process.stdin.write('list_cookbooks\n')
    # process.stdin.flush()

    # Generate a random number between 0 and 999,999,999 (inclusive)
    random_number = int(random.random() * 1000000000)
    nameOfRunnerFileName = "my-red-teaming-runner-" + str(random_number)

    command = 'new_session ' + nameOfRunnerFileName + ' -e "[\'ollama-llama3\']" -c add_previous_prompt -p mmlu \n'
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

    # # Example command to send to the process
    # process.stdin.write('list_cookbooks\n')
    # process.stdin.flush()

    # Generate a random number between 0 and 999,999,999 (inclusive)
    random_number = int(random.random() * 1000000000)
    nameOfRunnerFileName = "my-red-teaming-runner-" + str(random_number)

    command = 'new_session ' + nameOfRunnerFileName + ' -e "[\'ollama-llama3\']" -c add_previous_prompt -p mmlu \n'
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

    # # Example command to send to the process
    # process.stdin.write('list_cookbooks\n')
    # process.stdin.flush()

    # Generate a random number between 0 and 999,999,999 (inclusive)
    random_number = int(random.random() * 1000000000)
    nameOfRunnerFileName = "my-red-teaming-runner-" + str(random_number)

    command = 'new_session ' + nameOfRunnerFileName + ' -e "[\'ollama-llama3\']" -c add_previous_prompt -p mmlu \n'
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

    # # Example command to send to the process
    # process.stdin.write('use_session "my-runner"\n')
    # process.stdin.flush()

    command = 'new_session ' + nameOfRunnerFileName + ' -e "[\'ollama-llama3\']" -c add_previous_prompt -p mmlu \n'
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    process.stdin.write('run_attack_module charswap_attack "this is my prompt"\n')
    process.stdin.flush()

    process.stdin.write('add_bookmark ollama-llama3 1 my-bookmarked-prompt' + str(random_number) + '\n')
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
    assert 'Bookmarks exported successfully. Written to: moonshot-data/generated-outputs/bookmarks/' + Export_File_Name + '.json' == last_line


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

    # # Example command to send to the process
    # process.stdin.write('use_session "my-runner"\n')
    # process.stdin.flush()

    command = 'new_session ' + nameOfRunnerFileName + ' -e "[\'ollama-llama3\']" -c add_previous_prompt -p mmlu \n'
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    process.stdin.write('run_attack_module charswap_attack "this is my prompt"\n')
    process.stdin.flush()

    process.stdin.write('add_bookmark ollama-llama3 1 my-bookmarked-prompt' + str(random_number) + '\n')
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

    # # Example command to send to the process
    # process.stdin.write('use_session "my-runner"\n')
    # process.stdin.flush()

    command = 'new_session ' + nameOfRunnerFileName + ' -e "[\'ollama-llama3\']" -c add_previous_prompt -p mmlu \n'
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    process.stdin.write('run_attack_module charswap_attack "this is my prompt"\n')
    process.stdin.flush()

    process.stdin.write('add_bookmark ollama-llama3 1 my-bookmarked-prompt' + str(random_number) + '\n')
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
    file_path = str(CLI_DIR) + "/moonshot-data/generated-outputs/runners/" + nameOfRunnerFileName + ".json"

    # # Example command to send to the process
    # process.stdin.write('use_session "my-runner"\n')
    # process.stdin.flush()

    command = 'new_session ' + nameOfRunnerFileName + ' -e "[\'ollama-llama3\']" -c add_previous_prompt -p mmlu \n'
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
    last_line = output_lines[22]
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
    file_path = str(CLI_DIR) + "/moonshot-data/generated-outputs/runners/" + nameOfRunnerFileName + ".json"

    # # Example command to send to the process
    # process.stdin.write('use_session "my-runner"\n')
    # process.stdin.flush()

    command = 'new_session ' + nameOfRunnerFileName + ' -e "[\'ollama-llama3\']" -c add_previous_prompt -p mmlu \n'
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
    last_line = output_lines[22]
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
    file_path = str(CLI_DIR) + "/moonshot-data/generated-outputs/runners/" + nameOfRunnerFileName + ".json"

    # # Example command to send to the process
    # process.stdin.write('use_session "my-runner"\n')
    # process.stdin.flush()

    command = 'new_session ' + nameOfRunnerFileName + ' -e "[\'ollama-llama3\']" -c add_previous_prompt -p mmlu \n'
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
    last_line = output_lines[22]
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

    # # Example command to send to the process
    # process.stdin.write('use_session "my-runner"\n')
    # process.stdin.flush()

    command = 'new_session ' + nameOfRunnerFileName + ' -e "[\'ollama-llama3\']" -c add_previous_prompt -p mmlu \n'
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    process.stdin.write('run_attack_module charswap_attack "this is my prompt"\n')
    process.stdin.flush()

    process.stdin.write('add_bookmark ollama-llama3 1 my-bookmarked-prompt' + str(random_number) + '\n')
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
    file_path = str(CLI_DIR) + "/moonshot-data/generated-outputs/runners/" + nameOfRunnerFileName + ".json"

    # # Example command to send to the process
    # process.stdin.write('use_session "my-runner"\n')
    # process.stdin.flush()

    command = 'new_session ' + nameOfRunnerFileName + ' -e "[\'ollama-llama3\']" -c add_previous_prompt -p mmlu \n'
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
    last_line = output_lines[23]
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
    file_path = str(CLI_DIR) + "/moonshot-data/generated-outputs/runners/" + nameOfRunnerFileName + ".json"

    # # Example command to send to the process
    # process.stdin.write('use_session "my-runner"\n')
    # process.stdin.flush()

    command = 'new_session ' + nameOfRunnerFileName + ' -e "[\'ollama-llama3\']" -c add_previous_prompt -p mmlu \n'
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
    last_line = output_lines[23]
    print('=========================Output Last Line:', last_line)
    # Assert that '1' is present in the string
    assert 'Cleared prompt template.' == last_line

    if os.path.exists(file_path):
        print(f"File exists: {file_path}")
        assert True


    else:
        print(f"File does not exist: {file_path}")
        pytest.fail()
