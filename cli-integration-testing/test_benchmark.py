import subprocess
import time

from dotenv import load_dotenv
import os

import random

load_dotenv()  # Load environment variables from .env file

AZURE_OPENAI_URI = os.getenv('AZURE_OPENAI_URI')
AZURE_OPENAI_TOKEN = os.getenv('AZURE_OPENAI_TOKEN')
# CLI_DIR = '/Users/jacksonboey/PycharmProjects/moonshot'
# CLI_DIR = os.getenv('CLI_DIR')
CLI_DIR = '/Users/jacksonboey/PycharmProjects/moonshot'
def test_cli_benchmark():
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
        #/home/runner/work/moonshot-data/moonshot-data for moonshot data repo
        #/home/runner/work/moonshot/moonshot-data for moonshot repo
    )
    print('Path:', str(CLI_DIR))
    # Ensure process.stdin is not None
    if process.stdin is None:
        raise RuntimeError("Failed to create stdin for the subprocess")

    # # Example command to send to the process
    # process.stdin.write('list_cookbooks\n')
    # process.stdin.flush()

    # Update Endpoints
    command = 'update_endpoint azure-openai-gpt4o "[(\'name\', \'Azure OpenAI GPT4o\'), (\'uri\', \''+str(AZURE_OPENAI_URI)+'\'), (\'token\', \''+str(AZURE_OPENAI_TOKEN)+'\'), (\'params\', {\'timeout\': 300, \'allow_retries\': True, \'num_of_retries\': 3, \'temperature\': 0.5, \'model\': \'gpt-4o\'})]"\n'
    print('Command:', command)
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    # Generate a random number between 0 and 999,999,999 (inclusive)
    random_number = int(random.random() * 1000000000)
    nameOfRunnerFileName = "my-benchmarking-runner-" + str(random_number)
    nameOfRunnerName = "my benchmarking runner " + str(random_number)
    command = 'run_cookbook "' + nameOfRunnerName + '" "[\'chinese-safety-cookbook\']" "[\'azure-openai-gpt4o\']" -n 1 -r 1 -s "You are an intelligent AI"\n'
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

def test_cli_add_cookbook():
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
        #/home/runner/work/moonshot-data/moonshot-data for moonshot data repo
        #/home/runner/work/moonshot/moonshot-data for moonshot repo
    )
    print('Path:', str(CLI_DIR))
    # Ensure process.stdin is not None
    if process.stdin is None:
        raise RuntimeError("Failed to create stdin for the subprocess")

    timestamp = time.time()  # Get the current timestamp in seconds
    timestamp_int = str(int(timestamp))  # Remove the decimal part by converting to an integer
    command = ('add_cookbook \'My new cookbook '+timestamp_int+'\' \'I am cookbook description\' "[\'analogical-similarity\','
               '\'auto-categorisation\']"\n')
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
    assert last_line.replace(" ", "") == "[add_cookbook]:Cookbook(my-new-cookbook-"+timestamp_int+")created."

def test_cli_add_recipe():
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
        #/home/runner/work/moonshot-data/moonshot-data for moonshot data repo
        #/home/runner/work/moonshot/moonshot-data for moonshot repo
    )
    print('Path:', str(CLI_DIR))
    # Ensure process.stdin is not None
    if process.stdin is None:
        raise RuntimeError("Failed to create stdin for the subprocess")

    timestamp = time.time()  # Get the current timestamp in seconds
    timestamp_int = str(int(timestamp))  # Remove the decimal part by converting to an integer
    command = ('add_recipe \'My new recipe '+timestamp_int+'\' \'I am recipe description\' "[\'category1\',\'category2\']" "[\'bbq-lite-age-ambiguous\']" "[\'bertscore\',\'bleuscore\']" -p "[\'analogical-similarity\',\'mmlu\']" -t "[\'tag1\',\'tag2\']" -g "{\'A\':[80,100],\'B\':[60,79],\'C\':[40,59],\'D\':[20,39],\'E\':[0,19]}"\n')
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
    assert last_line.replace(" ", "") == "[add_recipe]:Recipe(my-new-recipe-"+timestamp_int+")created."

def test_cli_delete_recipe():
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
        #/home/runner/work/moonshot-data/moonshot-data for moonshot data repo
        #/home/runner/work/moonshot/moonshot-data for moonshot repo
    )
    print('Path:', str(CLI_DIR))
    # Ensure process.stdin is not None
    if process.stdin is None:
        raise RuntimeError("Failed to create stdin for the subprocess")

    timestamp = time.time()  # Get the current timestamp in seconds
    timestamp_int = str(int(timestamp))  # Remove the decimal part by converting to an integer
    command = ('add_recipe \'My new recipe '+timestamp_int+'\' \'I am recipe description\' "[\'category1\',\'category2\']" "[\'bbq-lite-age-ambiguous\']" "[\'bertscore\',\'bleuscore\']" -p "[\'analogical-similarity\',\'mmlu\']" -t "[\'tag1\',\'tag2\']" -g "{\'A\':[80,100],\'B\':[60,79],\'C\':[40,59],\'D\':[20,39],\'E\':[0,19]}"\n')
    print('Command:', command)
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    command = ('delete_recipe my-new-recipe-'+timestamp_int+'\n')
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
    last_line = output_lines[12]
    print('=========================Output Last Line:', last_line)
    assert last_line.replace(" ", "") == "Areyousureyouwanttodeletetherecipe(y/N)?[delete_recipe]:Recipedeleted."