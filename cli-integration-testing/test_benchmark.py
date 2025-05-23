import subprocess
from dotenv import load_dotenv
import os
import time
import random
from util.utils import *

load_dotenv()  # Load environment variables from .env file

OPENAI_URI = os.getenv('OPENAI_URI')
OPENAI_TOKEN = os.getenv('OPENAI_TOKEN')
TOGETHER_TOKEN= os.getenv('TOGETHER_TOKEN')
CLI_DIR = os.getenv('CLI_DIR')

COMMAND = ('python -m moonshot cli interactive')
timestamp = time.time()
timestamp_int = str(int(timestamp))
COOKBOOK_NAME = "test-cookbook-" + timestamp_int
RECIPE_NAME = "test-recipe-" + timestamp_int

def test_cli_add_cookbook():
    process = subprocess.Popen(
        COMMAND,
        shell=True,  # Allows for complex shell commands
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        stdin=subprocess.PIPE,
        text=True,
        cwd=str(CLI_DIR),
    )
    print('Path:', str(CLI_DIR))
    if process.stdin is None:
        raise RuntimeError("Failed to create stdin for the subprocess")

    # Execute add_cookbook
    command = (
            'add_cookbook \'' + COOKBOOK_NAME + '\' \'I am cookbook description\' "[\'singapore-facts\']"\n')
    print('Command:', command)
    process.stdin.write(command)
    process.stdin.flush()
 
    # Capture the output and errors
    stdout, stderr = process.communicate()

    # Validate output
    print('Output:', stdout)
    output_lines = stdout.splitlines()
    last_line = output_lines[11]
    print('=========================Output Last Line:', last_line)
    assert last_line.replace(" ", "") == "[add_cookbook]:Cookbook(" + COOKBOOK_NAME + ")created."


def test_cli_add_recipe():
    process = subprocess.Popen(
        COMMAND,
        shell=True,  # Allows for complex shell commands
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        stdin=subprocess.PIPE,
        text=True,
        cwd=str(CLI_DIR),
    )
    print('Path:', str(CLI_DIR))
    if process.stdin is None:
        raise RuntimeError("Failed to create stdin for the subprocess")

    # Execute add_recipe
    timestamp = time.time()
    timestamp_int = str(int(timestamp))
    command = (
            'add_recipe \'' + RECIPE_NAME + '\' \'I am recipe description\' "[\'category1\',\'category2\']"'
            ' "[\'bbq-lite-age-ambiguous\']" "[\'bertscore\',\'bleuscore\']" -p "[\'analogical-similarity\',\'mmlu\']"'
            ' -t "[\'tag1\',\'tag2\']" -g "{\'A\':[80,100],\'B\':[60,79],\'C\':[40,59],\'D\':[20,39],\'E\':[0,19]}"\n')
    print('Command:', command)
    process.stdin.write(command)
    process.stdin.flush()

    # Capture the output and errors
    stdout, stderr = process.communicate()

    # Validate output
    print('Output:', stdout)
    output_lines = stdout.splitlines()
    last_line = output_lines[11]
    print('=========================Output Last Line:', last_line)
    assert last_line.replace(" ", "") == "[add_recipe]:Recipe(" + RECIPE_NAME + ")created."

def test_cli_run_cookbook():
    process = subprocess.Popen(
        COMMAND,
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
    nameOfRunnerFileName = "my-benchmarking-runner-" + str(random_number)
    nameOfRunnerName = "my benchmarking runner " + str(random_number)
    command = ('run_cookbook "' + nameOfRunnerName + '" "[\'' + COOKBOOK_NAME + '\']" "[\'openai-gpt4o\']"'
               ' -n 1 -r 1 -s "You are an intelligent AI"\n')
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    # Capture the output and errors
    stdout, stderr = process.communicate()
    print("ERROR:::: "+ stderr)

    print('Output:', stdout)
    # Split the output into lines
    output_lines = stdout.splitlines()

    # Get the last line of the output
    last_line = output_lines[-14]
    print('=========================Output Last Line:', last_line)
    assert last_line.replace(" ", "") == "CookbookResult"

# def test_cli_run_cookbook_mlc_ai_safety():
#     command = (
#         # 'cd .. &&'
#         # 'source venv/bin/activate &&'
#         # 'cd moonshot &&'
#         'python -m moonshot cli interactive'
#     )

#     process = subprocess.Popen(
#         command,
#         shell=True,  # Allows for complex shell commands
#         stdout=subprocess.PIPE,
#         stderr=subprocess.PIPE,
#         stdin=subprocess.PIPE,
#         text=True,
#         cwd=str(CLI_DIR),
#         # cwd="/Users/jacksonboey/PycharmProjects/moonshot",
#         # /home/runner/work/moonshot-data/moonshot-data for moonshot data repo
#         # /home/runner/work/moonshot/moonshot-data for moonshot repo
#     )
#     print('Path:', str(CLI_DIR))
#     # Ensure process.stdin is not None
#     if process.stdin is None:
#         raise RuntimeError("Failed to create stdin for the subprocess")

#     # Update Endpoints
#     command = 'update_endpoint openai-gpt4o "[(\'name\', \'OpenAI GPT4o\'), (\'uri\', \'' + str(
#         OPENAI_URI) + '\'), (\'token\', \'' + str(
#         OPENAI_TOKEN) + '\'), (\'model\', \'gpt-4o\'), (\'params\', {\'timeout\': 300,\'max_attempts\': 3, \'temperature\': 0.5})]"\n'
#     print('Command:', command)
#     # Example command to send to the process
#     process.stdin.write(command)
#     process.stdin.flush()

#     # Update Evaluation Endpoint
#     command = 'update_endpoint together-llama-guard-7b-assistant "[(\'token\', \'' + str(TOGETHER_TOKEN) + '\')]"\n'
#     print('Command:', command)
#     # Example command to send to the process
#     process.stdin.write(command)
#     process.stdin.flush()

#     # Generate a random number between 0 and 999,999,999 (inclusive)
#     random_number = int(random.random() * 1000000000)
#     nameOfRunnerFileName = "my-benchmarking-runner-" + str(random_number)
#     nameOfRunnerName = "my benchmarking runner " + str(random_number)
#     command = 'run_cookbook "' + nameOfRunnerName + '" "[\'mlc-ai-safety\']" "[\'openai-gpt4o\']" -n 1 -r 1 -s "You are an intelligent AI"\n'
#     print('Command:', command)
#     # Example command to send to the process
#     process.stdin.write(command)
#     process.stdin.flush()

#     # Capture the output and errors
#     stdout, stderr = process.communicate()

#     print('Output:', stdout)
#     # Split the output into lines
#     output_lines = stdout.splitlines()

#     # Get the last line of the output
#     last_line = output_lines[-26]
#     print('=========================Output Last Line:', last_line)
#     assert last_line.replace(" ", "") == "CookbookResult"

# def test_cli_run_rag_cookbook():
#     command = (
#         # 'cd .. &&'
#         # 'source venv/bin/activate &&'
#         # 'cd moonshot &&'
#         'python3 -m moonshot cli interactive'
#     )
#
#     process = subprocess.Popen(
#         command,
#         shell=True,  # Allows for complex shell commands
#         stdout=subprocess.PIPE,
#         stderr=subprocess.PIPE,
#         stdin=subprocess.PIPE,
#         text=True,
#         cwd=str(CLI_DIR),
#         # cwd="/Users/jacksonboey/PycharmProjects/moonshot",
#         # /home/runner/work/moonshot-data/moonshot-data for moonshot data repo
#         # /home/runner/work/moonshot/moonshot-data for moonshot repo
#     )
#     print('Path:', str(CLI_DIR))
#     # Ensure process.stdin is not None
#     if process.stdin is None:
#         raise RuntimeError("Failed to create stdin for the subprocess")
#     #
#     current_path = CLI_DIR + "/moonshot-data/metrics/copy_of_advglue.py"  # Replace with the current file path
#
#     # Move Rag files to moonshot-data for testing
#     source = os.path.join(os.path.abspath("./"), "test_files/tera-connector.py")
#     destination = CLI_DIR + "/moonshot-data/connectors/tera-connector.py"
#     copy_and_move_file(source, destination)
#
#
#
#     # Update Endpoints
#     command = 'update_endpoint openai-gpt4o "[(\'name\', \'OpenAI GPT4o\'), (\'uri\', \'' + str(
#         OPENAI_URI) + '\'), (\'token\', \'' + str(
#         OPENAI_TOKEN) + '\'), (\'model\', \'gpt-4o\'), (\'params\', {\'timeout\': 300,\'max_attempts\': 3, \'temperature\': 0.5})]"\n'
#     print('Command:', command)
#     # Example command to send to the process
#     process.stdin.write(command)
#     process.stdin.flush()
#
#     # Generate a random number between 0 and 999,999,999 (inclusive)
#     random_number = int(random.random() * 1000000000)
#     nameOfRunnerFileName = "my-benchmarking-runner-" + str(random_number)
#     nameOfRunnerName = "my benchmarking runner " + str(random_number)
#     command = 'run_cookbook "' + nameOfRunnerName + '" "[\'singapore-context\']" "[\'openai-gpt4o\']" -n 1 -r 1 -s "You are an intelligent AI"\n'
#     # Example command to send to the process
#     process.stdin.write(command)
#     process.stdin.flush()
#
#     # Capture the output and errors
#     stdout, stderr = process.communicate()
#
#     print('Output:', stdout)
#     # Split the output into lines
#     output_lines = stdout.splitlines()
#
#     # Get the last line of the output
#     last_line = output_lines[-16]
#     print('=========================Output Last Line:', last_line)
#     assert last_line.replace(" ", "") == "CookbookResult"

def test_cli_run_recipe():
    process = subprocess.Popen(
        COMMAND,
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

    # Update Endpoints
    command = 'update_endpoint openai-gpt4o "[(\'name\', \'OpenAI GPT4o\'), (\'uri\', \'' + str(
        OPENAI_URI) + '\'), (\'token\', \'' + str(
        OPENAI_TOKEN) + '\'), (\'model\': \'gpt-4o\'), (\'params\', {\'timeout\': 300,\'max_attempts\': 3, \'temperature\': 0.5})]"\n'
    print('Command:', command)
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    # Generate a random number between 0 and 999,999,999 (inclusive)
    random_number = int(random.random() * 1000000000)
    nameOfRunnerFileName = "my-new-recipe-runner-" + str(random_number)
    nameOfRunnerName = "my new recipe runner " + str(random_number)
    command = 'run_recipe "' + nameOfRunnerName + '" "[\'bbq\',\'mmlu\']" "[\'openai-gpt4o\']" -n 1 -r 1 -s "You are an intelligent AI"\n'
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    # Capture the output and errors
    stdout, stderr = process.communicate()

    print('Output:', stdout)
    # Split the output into lines
    output_lines = stdout.splitlines()

    # Get the last line of the output
    last_line = output_lines[-14]
    print('=========================Output Last Line:', last_line)
    assert last_line.replace(" ", "") == "RecipesResult"

def test_cli_delete_cookbook():
    process = subprocess.Popen(
        COMMAND,
        shell=True,  # Allows for complex shell commands
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        stdin=subprocess.PIPE,
        text=True,
        cwd=str(CLI_DIR),
    )
    print('Path:', str(CLI_DIR))
    if process.stdin is None:
        raise RuntimeError("Failed to create stdin for the subprocess")

    # Execute delete_cookbook
    command = ('delete_cookbook ' + COOKBOOK_NAME + '\n')
    print('Command:', command)
    process.stdin.write(command)
    process.stdin.flush()
    command = ('y\n')
    print('Command:', command)
    process.stdin.write(command)
    process.stdin.flush()

    # Capture the output and errors
    stdout, stderr = process.communicate()

    # Validate output
    print('Output:', stdout)
    output_lines = stdout.splitlines()
    last_line = output_lines[11]
    print('=========================Output Last Line:', last_line)
    assert last_line.replace(" ", "") == "Areyousureyouwanttodeletethecookbook(y/N)?[delete_cookbook]:Cookbookdeleted."

def test_cli_delete_recipe():
    process = subprocess.Popen(
        COMMAND,
        shell=True,  # Allows for complex shell commands
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        stdin=subprocess.PIPE,
        text=True,
        cwd=str(CLI_DIR),
    )
    print('Path:', str(CLI_DIR))
    if process.stdin is None:
        raise RuntimeError("Failed to create stdin for the subprocess")

    command = ('delete_recipe ' + RECIPE_NAME + '\n')
    print('Command:', command)
    process.stdin.write(command)
    process.stdin.flush()

    command = ('y\n')
    print('Command:', command)
    process.stdin.write(command)
    process.stdin.flush()

    # Capture the output and errors
    stdout, stderr = process.communicate()

    # Validate output
    print('Output:', stdout)
    output_lines = stdout.splitlines()
    last_line = output_lines[11]
    print('=========================Output Last Line:', last_line)
    assert last_line.replace(" ", "") == "Areyousureyouwanttodeletetherecipe(y/N)?[delete_recipe]:Recipedeleted."


def test_cli_delete_metric():
    process = subprocess.Popen(
        COMMAND,
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
    copy_file(CLI_DIR + '/moonshot-data-aisi/metrics/advglue.py')

    command = 'delete_metric advglue \n'

    print('Command:', command)
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    command = 'y\n'

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
    # Restore file
    current_path = CLI_DIR + "/moonshot-data-aisi/metrics/copy_of_advglue.py"  # Replace with the current file path
    new_name = "advglue.py"  # Specify the new file name
    rename_file(current_path, new_name)
    assert last_line.replace(" ", "") == "Areyousureyouwanttodeletethemetric(y/N)?[delete_metric]:Metricdeleted."


def test_cli_delete_result():
    process = subprocess.Popen(
        COMMAND,
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

    # Update Endpoints
    command = 'update_endpoint openai-gpt4o "[(\'name\', \'OpenAI GPT4o\'), (\'uri\', \'' + str(
        OPENAI_URI) + '\'), (\'token\', \'' + str(
        OPENAI_TOKEN) + '\'), (\'model\': \'gpt-4o\'), (\'params\', {\'timeout\': 300,\'max_attempts\': 3, \'temperature\': 0.5})]"\n'
    print('Command:', command)
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    # Generate a random number between 0 and 999,999,999 (inclusive)
    random_number = int(random.random() * 1000000000)
    nameOfRunnerFileName = "my-benchmarking-runner-" + str(random_number)
    nameOfRunnerName = "my benchmarking runner " + str(random_number)
    command = 'run_cookbook "' + nameOfRunnerName + '" "[\'chinese-safety-cookbook\']" "[\'openai-gpt4o\']" -n 1 -r 1 -s "You are an intelligent AI"\n'
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    # Execute delete_result
    command = 'delete_result ' + nameOfRunnerFileName + '\n'
    print('Command:', command)
    process.stdin.write(command)
    process.stdin.flush()
    command = 'y\n'
    print('Command:', command)
    process.stdin.write(command)
    process.stdin.flush()

    # Capture the output and errors
    stdout, stderr = process.communicate()

    print('Output:', stdout)
    # Split the output into lines
    output_lines = stdout.splitlines()

    # Get the last line of the output
    last_line = output_lines[-2]
    print('=========================Output Last Line:', last_line)
    assert last_line.replace(" ", "") == "Areyousureyouwanttodeletetheresult(y/N)?[delete_result]:Resultdeleted."


def test_cli_delete_runner():
    run_recipe_process = subprocess.Popen(
        COMMAND,
        shell=True,  # Allows for complex shell commands
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        stdin=subprocess.PIPE,
        text=True,
        cwd=str(CLI_DIR),
    )
    print('Path:', str(CLI_DIR))
    # Ensure process.stdin is not None
    if run_recipe_process.stdin is None:
        raise RuntimeError("Failed to create stdin for the subprocess")

    # Update Endpoints
    command = 'update_endpoint openai-gpt4o "[(\'name\', \'OpenAI GPT4o\'), (\'uri\', \'' + str(
        OPENAI_URI) + '\'), (\'token\', \'' + str(
        OPENAI_TOKEN) + '\'), (\'model\': \'gpt-4o\'), (\'params\', {\'timeout\': 300,\'max_attempts\': 3, \'temperature\': 0.5})]"\n'
    print('Command:', command)
    # Example command to send to the process
    run_recipe_process.stdin.write(command)
    run_recipe_process.stdin.flush()

    # Generate a random number between 0 and 999,999,999 (inclusive)
    random_number = int(random.random() * 1000000000)
    nameOfRunnerFileName = "my-benchmarking-runner-" + str(random_number)
    nameOfRunnerName = "my benchmarking runner " + str(random_number)
    command = 'run_recipe "' + nameOfRunnerName + '" "[\'cbbq-lite\']" "[\'openai-gpt4o\']" -n 1 -r 1 -s "You are an intelligent AI"\n'
    # Example command to send to the process
    run_recipe_process.stdin.write(command)
    run_recipe_process.stdin.flush()

    # Capture the output and errors
    stdout, stderr = run_recipe_process.communicate()

    print('Output:', stdout)
    # Split the output into lines
    output_lines = stdout.splitlines()

    delete_runner_process = subprocess.Popen(
        COMMAND,
        shell=True,  # Allows for complex shell commands
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        stdin=subprocess.PIPE,
        text=True,
        cwd=str(CLI_DIR),
    )
    print('Path:', str(CLI_DIR))
    # Ensure process.stdin is not None
    if delete_runner_process.stdin is None:
        raise RuntimeError("Failed to create stdin for the subprocess")

    # Execute delete_runner
    command = 'delete_runner ' + nameOfRunnerFileName + '\n'
    print('Command:', command)
    delete_runner_process.stdin.write(command)
    delete_runner_process.stdin.flush()
    command = 'y\n'
    print('Command:', command)
    delete_runner_process.stdin.write(command)
    delete_runner_process.stdin.flush()

    # Capture the output and errors
    stdout, stderr = delete_runner_process.communicate()
    print("ERROR::" + stderr)

    print('Output:', stdout)
    # Split the output into lines
    output_lines += stdout.splitlines()

    # Get the last line of the output
    last_line = output_lines[-2]
    print('=========================Output Last Line:', last_line)
    assert last_line.replace(" ", "") == "Areyousureyouwanttodeletetherunner(y/N)?[delete_runner]:Runnerdeleted."

def test_cli_list_cookbooks():
    process = subprocess.Popen(
        COMMAND,
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

    timestamp = time.time()  # Get the current timestamp in seconds
    timestamp_int = str(int(timestamp))  # Remove the decimal part by converting to an integer
    command = ('list_cookbooks -f "risk"\n')
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
    assert last_line.replace(" ", "") == "ListofCookbooks"


def test_cli_list_datasets():
    process = subprocess.Popen(
        COMMAND,
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

    timestamp = time.time()  # Get the current timestamp in seconds
    timestamp_int = str(int(timestamp))  # Remove the decimal part by converting to an integer
    command = ('list_datasets -f "bbq"\n')
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
    assert last_line.replace(" ", "") == "ListofDatasets"


def test_cli_list_metrics():
    process = subprocess.Popen(
        COMMAND,
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

    timestamp = time.time()  # Get the current timestamp in seconds
    timestamp_int = str(int(timestamp))  # Remove the decimal part by converting to an integer
    command = ('list_metrics\n')
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
    assert last_line.replace(" ", "") == "ListofMetrics"


def test_cli_list_recipes():
    process = subprocess.Popen(
        COMMAND,
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

    timestamp = time.time()  # Get the current timestamp in seconds
    timestamp_int = str(int(timestamp))  # Remove the decimal part by converting to an integer
    command = ('list_recipes\n')
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
    assert last_line.replace(" ", "") == "ListofRecipes"


def test_cli_list_results():
    process = subprocess.Popen(
        COMMAND,
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

    # Update Endpoints
    command = 'update_endpoint openai-gpt4o "[(\'name\', \'OpenAI GPT4o\'), (\'uri\', \'' + str(
        OPENAI_URI) + '\'), (\'token\', \'' + str(
        OPENAI_TOKEN) + '\'), (\'model\': \'gpt-4o\'), (\'params\', {\'timeout\': 300,\'max_attempts\': 3, \'temperature\': 0.5})]"\n'
    print('Command:', command)
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    # Generate a random number between 0 and 999,999,999 (inclusive)
    random_number = int(random.random() * 1000000000)
    nameOfRunnerFileName = "my-benchmarking-runner-" + str(random_number)
    nameOfRunnerName = "my benchmarking runner " + str(random_number)
    command = 'run_cookbook "' + nameOfRunnerName + '" "[\'chinese-safety-cookbook\']" "[\'openai-gpt4o\']" -n 1 -r 1 -s "You are an intelligent AI"\n'
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    command = 'list_results -f "' + nameOfRunnerFileName + '"\n'
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    # Capture the output and errors
    stdout, stderr = process.communicate()

    print('Output:', stdout)
    # Split the output into lines
    output_lines = stdout.splitlines()

    # Get the last line of the output
    last_line = output_lines[27]
    print('=========================Output Last Line:', last_line)
    assert last_line.replace(" ", "") == "ListofResults"

def test_cli_list_runners():
    process = subprocess.Popen(
        COMMAND,
        shell=True,  # Allows for complex shell commands
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        stdin=subprocess.PIPE,
        text=True,
        cwd=str(CLI_DIR),
    )
    print('Path:', str(CLI_DIR))
    if process.stdin is None:
        raise RuntimeError("Failed to create stdin for the subprocess")

    # Update Endpoints
    command = 'update_endpoint openai-gpt4o "[(\'name\', \'OpenAI GPT4o\'), (\'uri\', \'' + str(
        OPENAI_URI) + '\'), (\'token\', \'' + str(
        OPENAI_TOKEN) + '\'), (\'model\': \'gpt-4o\'), (\'params\', {\'timeout\': 300,\'max_attempts\': 3, \'temperature\': 0.5})]"\n'
    process.stdin.write(command)
    process.stdin.flush()

    # Generate a random number between 0 and 999,999,999 (inclusive)
    random_number = int(random.random() * 1000000000)
    nameOfRunnerName = "my benchmarking runner " + str(random_number)
    command = 'run_cookbook "' + nameOfRunnerName + '" "[\'chinese-safety-cookbook\']" "[\'openai-gpt4o\']" -n 1 -r 1 -s "You are an intelligent AI"\n'
    process.stdin.write(command)
    process.stdin.flush()

    command = 'list_runners -f "run"\n'
    process.stdin.write(command)
    process.stdin.flush()

    # Capture the output and errors
    stdout, stderr = process.communicate()

    print('Output:', stdout)
    # Split the output into lines
    output_lines = stdout.splitlines()

    # Get the last line of the output
    last_line = output_lines[27]
    print('=========================Output Last Line:', last_line)
    assert last_line.replace(" ", "") == "ListofRunners"

def test_cli_list_runs():
    process = subprocess.Popen(
        COMMAND,
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

    # Update Endpoints
    command = 'update_endpoint openai-gpt4o "[(\'name\', \'OpenAI GPT4o\'), (\'uri\', \'' + str(
        OPENAI_URI) + '\'), (\'token\', \'' + str(
        OPENAI_TOKEN) + '\'), (\'model\': \'gpt-4o\'), (\'params\', {\'timeout\': 300,\'max_attempts\': 3, \'temperature\': 0.5})]"\n'
    print('Command:', command)
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    # Generate a random number between 0 and 999,999,999 (inclusive)
    random_number = int(random.random() * 1000000000)
    nameOfRunnerFileName = "my-benchmarking-runner-" + str(random_number)
    nameOfRunnerName = "my benchmarking runner " + str(random_number)
    command = 'run_cookbook "' + nameOfRunnerName + '" "[\'chinese-safety-cookbook\']" "[\'openai-gpt4o\']" -n 1 -r 1 -s "You are an intelligent AI"\n'
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    command = 'list_runs -f "run"\n'
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    # Capture the output and errors
    stdout, stderr = process.communicate()

    print('Output:', stdout)
    # Split the output into lines
    output_lines = stdout.splitlines()

    # Get the last line of the output
    last_line = output_lines[27]
    print('=========================Output Last Line:', last_line)
    assert last_line.replace(" ", "") == "ListofRuns"

def test_cli_update_cookbook():
    process = subprocess.Popen(
        COMMAND,
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

    timestamp = time.time()  # Get the current timestamp in seconds
    timestamp_int = str(int(timestamp))  # Remove the decimal part by converting to an integer
    command = (
            'add_cookbook \'My new cookbook ' + timestamp_int + '\' \'I am cookbook description\' "[\'analogical-similarity\','
                                                                '\'auto-categorisation\']"\n')
    print('Command:', command)
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    command = (
            'update_cookbook \'my-new-cookbook-' + timestamp_int + '\' "[(\'name\', \'Updated Cookbook Name ' + timestamp_int + '\'), (\'description\', \'Updated description\'), (\'recipes\', [\'analogical-similarity\'])]"\n')
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
    print('=========================Output Last Line:', last_line)
    assert last_line.replace(" ", "") == "[update_cookbook]:Cookbookupdated."


def test_cli_update_recipe():
    process = subprocess.Popen(
        COMMAND,
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

    timestamp = time.time()  # Get the current timestamp in seconds
    timestamp_int = str(int(timestamp))  # Remove the decimal part by converting to an integer
    command = (
            'add_recipe \'My new recipe ' + timestamp_int + '\' \'I am recipe description\' "[\'category1\',\'category2\']" "[\'bbq-lite-age-ambiguous\']" "[\'bertscore\',\'bleuscore\']" -p "[\'analogical-similarity\',\'mmlu\']" -t "[\'tag1\',\'tag2\']" -g "{\'A\':[80,100],\'B\':[60,79],\'C\':[40,59],\'D\':[20,39],\'E\':[0,19]}"\n')
    print('Command:', command)
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()
    command = (
            'update_recipe my-new-recipe-' + timestamp_int + ' "[(\'name\', \'My Updated Recipe ' + timestamp_int + '\'), (\'tags\', [\'fairness\', \'bbq\'])]"\n')
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
    print('=========================Output Last Line:', last_line)
    assert last_line.replace(" ", "") == "[update_recipe]:Recipeupdated."


def test_cli_view_cookbook():
    process = subprocess.Popen(
        COMMAND,
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

    timestamp = time.time()  # Get the current timestamp in seconds
    timestamp_int = str(int(timestamp))  # Remove the decimal part by converting to an integer
    command = (
            'add_cookbook \'My new cookbook ' + timestamp_int + '\' \'I am cookbook description\' "[\'analogical-similarity\','
                                                                '\'auto-categorisation\']"\n')
    print('Command:', command)
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    command = ('view_cookbook my-new-cookbook-' + timestamp_int + ' \n')
    print('Command:', command)
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    # Capture the output and errors
    stdout, stderr = process.communicate()
    print("Error:: " + stderr)

    print('Output:', stdout)
    # Split the output into lines
    output_lines = stdout.splitlines()

    # Get the last line of the output
    last_line = output_lines[12]
    print('=========================Output Last Line:', last_line)
    assert last_line.replace(" ", "") == "Cookbook:\"Mynewcookbook" + timestamp_int + "\""

def test_cli_view_recipe():
    process = subprocess.Popen(
        COMMAND,
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

    timestamp = time.time()  # Get the current timestamp in seconds
    timestamp_int = str(int(timestamp))  # Remove the decimal part by converting to an integer
    command = (
            'add_recipe \'My new recipe ' + timestamp_int + '\' \'I am recipe description\' "[\'category1\',\'category2\']" "[\'bbq-lite-age-ambiguous\']" "[\'bertscore\',\'bleuscore\']" -p "[\'analogical-similarity\',\'mmlu\']" -t "[\'tag1\',\'tag2\']" -g "{\'A\':[80,100],\'B\':[60,79],\'C\':[40,59],\'D\':[20,39],\'E\':[0,19]}"\n')
    print('Command:', command)
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    command = ('view_recipe my-new-recipe-' + timestamp_int + '\n')
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
    assert last_line.replace(" ", "") == "ListofRecipes"

def test_cli_view_dataset():
    process = subprocess.Popen(
        COMMAND,
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

    command = ('view_dataset bbq-lite-age-ambiguous\n')
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
    assert last_line.replace(" ", "") == "ListofDatasets"

def test_cli_view_metric():
    process = subprocess.Popen(
        COMMAND,
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

    command = ('view_metric advglue\n')
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
    assert last_line.replace(" ", "") == "ListofMetrics"

def test_cli_view_result():
    process = subprocess.Popen(
        COMMAND,
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

    # Update Endpoints
    command = 'update_endpoint openai-gpt4o "[(\'name\', \'OpenAI GPT4o\'), (\'uri\', \'' + str(
        OPENAI_URI) + '\'), (\'token\', \'' + str(
        OPENAI_TOKEN) + '\'), (\'model\': \'gpt-4o\'), (\'params\', {\'timeout\': 300,\'max_attempts\': 3, \'temperature\': 0.5})]"\n'
    print('Command:', command)
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    # Generate a random number between 0 and 999,999,999 (inclusive)
    random_number = int(random.random() * 1000000000)
    nameOfRunnerFileName = "my-benchmarking-runner-" + str(random_number)
    nameOfRunnerName = "my benchmarking runner " + str(random_number)
    command = 'run_cookbook "' + nameOfRunnerName + '" "[\'chinese-safety-cookbook\']" "[\'openai-gpt4o\']" -n 1 -r 1 -s "You are an intelligent AI"\n'
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    command = 'view_result '+nameOfRunnerFileName+'\n'
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    # Capture the output and errors
    stdout, stderr = process.communicate()

    print('Output:', stdout)
    # Split the output into lines
    output_lines = stdout.splitlines()

    # Get the last line of the output
    last_line = output_lines[-16]
    print('=========================Output Last Line:', last_line)
    assert last_line.replace(" ", "") == "CookbookResult"

def test_cli_view_run():
    process = subprocess.Popen(
        COMMAND,
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

    # Update Endpoints
    command = 'update_endpoint openai-gpt4o "[(\'name\', \'OpenAI GPT4o\'), (\'uri\', \'' + str(
        OPENAI_URI) + '\'), (\'token\', \'' + str(
        OPENAI_TOKEN) + '\'), (\'model\': \'gpt-4o\'), (\'params\', {\'timeout\': 300,\'max_attempts\': 3, \'temperature\': 0.5})]"\n'
    print('Command:', command)
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    # Generate a random number between 0 and 999,999,999 (inclusive)
    random_number = int(random.random() * 1000000000)
    nameOfRunnerFileName = "my-benchmarking-runner-" + str(random_number)
    nameOfRunnerName = "my benchmarking runner " + str(random_number)
    command = 'run_cookbook "' + nameOfRunnerName + '" "[\'chinese-safety-cookbook\']" "[\'openai-gpt4o\']" -n 1 -r 1 -s "You are an intelligent AI"\n'
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    command = 'view_run '+nameOfRunnerFileName+'\n'
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    # Capture the output and errors
    stdout, stderr = process.communicate()

    print('Output:', stdout)
    # Split the output into lines
    output_lines = stdout.splitlines()

    # Get the last line of the output
    last_line = output_lines[27]
    print('=========================Output Last Line:', last_line)
    assert last_line.replace(" ", "") == "ListofRuns"

def test_cli_view_runner():
    process = subprocess.Popen(
        COMMAND,
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

    # Update Endpoints
    command = 'update_endpoint openai-gpt4o "[(\'name\', \'OpenAI GPT4o\'), (\'uri\', \'' + str(
        OPENAI_URI) + '\'), (\'token\', \'' + str(
        OPENAI_TOKEN) + '\'), (\'model\': \'gpt-4o\'), (\'params\', {\'timeout\': 300,\'max_attempts\': 3, \'temperature\': 0.5})]"\n'
    print('Command:', command)
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    # Generate a random number between 0 and 999,999,999 (inclusive)
    random_number = int(random.random() * 1000000000)
    nameOfRunnerFileName = "my-benchmarking-runner-" + str(random_number)
    nameOfRunnerName = "my benchmarking runner " + str(random_number)
    command = 'run_cookbook "' + nameOfRunnerName + '" "[\'chinese-safety-cookbook\']" "[\'openai-gpt4o\']" -n 1 -r 1 -s "You are an intelligent AI"\n'
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    command = 'view_runner '+nameOfRunnerFileName+'\n'
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    # Capture the output and errors
    stdout, stderr = process.communicate()

    print('Output:', stdout)
    # Split the output into lines
    output_lines = stdout.splitlines()

    # Get the last line of the output
    last_line = output_lines[27]
    print('=========================Output Last Line:', last_line)
    assert last_line.replace(" ", "") == "ListofRunners"
