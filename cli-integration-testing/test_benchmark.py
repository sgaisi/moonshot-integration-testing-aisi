import subprocess
from dotenv import load_dotenv
import os
import time
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


def test_cli_run_cookbook():
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

    # Update Endpoints
    command = 'update_endpoint azure-openai-gpt4o "[(\'name\', \'Azure OpenAI GPT4o\'), (\'uri\', \'' + str(
        AZURE_OPENAI_URI) + '\'), (\'token\', \'' + str(
        AZURE_OPENAI_TOKEN) + '\'), (\'params\', {\'timeout\': 300, \'allow_retries\': True, \'num_of_retries\': 3, \'temperature\': 0.5, \'model\': \'gpt-4o\'})]"\n'
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


def test_cli_run_recipe():
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

    # Update Endpoints
    command = 'update_endpoint azure-openai-gpt4o "[(\'name\', \'Azure OpenAI GPT4o\'), (\'uri\', \'' + str(
        AZURE_OPENAI_URI) + '\'), (\'token\', \'' + str(
        AZURE_OPENAI_TOKEN) + '\'), (\'params\', {\'timeout\': 300, \'allow_retries\': True, \'num_of_retries\': 3, \'temperature\': 0.5, \'model\': \'gpt-4o\'})]"\n'
    print('Command:', command)
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    # Generate a random number between 0 and 999,999,999 (inclusive)
    random_number = int(random.random() * 1000000000)
    nameOfRunnerFileName = "my-new-recipe-runner-" + str(random_number)
    nameOfRunnerName = "my new recipe runner " + str(random_number)
    command = 'run_recipe "' + nameOfRunnerName + '" "[\'bbq\',\'mmlu\']" "[\'azure-openai-gpt4o\']" -n 1 -r 1 -s "You are an intelligent AI"\n'
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

    # Capture the output and errors
    stdout, stderr = process.communicate()

    print('Output:', stdout)
    # Split the output into lines
    output_lines = stdout.splitlines()

    # Get the last line of the output
    last_line = output_lines[11]
    print('=========================Output Last Line:', last_line)
    assert last_line.replace(" ", "") == "[add_cookbook]:Cookbook(my-new-cookbook-" + timestamp_int + ")created."


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

    # Capture the output and errors
    stdout, stderr = process.communicate()

    print('Output:', stdout)
    # Split the output into lines
    output_lines = stdout.splitlines()

    # Get the last line of the output
    last_line = output_lines[11]
    print('=========================Output Last Line:', last_line)
    assert last_line.replace(" ", "") == "[add_recipe]:Recipe(my-new-recipe-" + timestamp_int + ")created."


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

    command = ('delete_recipe my-new-recipe-' + timestamp_int + '\n')
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


def test_cli_delete_metric():
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
    copy_file(CLI_DIR + '/moonshot-data/metrics/advglue.py')

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
    current_path = CLI_DIR + "/moonshot-data/metrics/copy_of_advglue.py"  # Replace with the current file path
    new_name = "advglue.py"  # Specify the new file name
    rename_file(current_path, new_name)
    assert last_line.replace(" ", "") == "Areyousureyouwanttodeletethemetric(y/N)?[delete_metric]:Metricdeleted."


def test_cli_delete_metric():
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
    copy_file(CLI_DIR + '/moonshot-data/metrics/advglue.py')

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
    current_path = CLI_DIR + "/moonshot-data/metrics/copy_of_advglue.py"  # Replace with the current file path
    new_name = "advglue.py"  # Specify the new file name
    rename_file(current_path, new_name)
    assert last_line.replace(" ", "") == "Areyousureyouwanttodeletethemetric(y/N)?[delete_metric]:Metricdeleted."


def test_cli_delete_result():
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

    # # Example command to send to the process
    # process.stdin.write('list_cookbooks\n')
    # process.stdin.flush()

    # Update Endpoints
    command = 'update_endpoint azure-openai-gpt4o "[(\'name\', \'Azure OpenAI GPT4o\'), (\'uri\', \'' + str(
        AZURE_OPENAI_URI) + '\'), (\'token\', \'' + str(
        AZURE_OPENAI_TOKEN) + '\'), (\'params\', {\'timeout\': 300, \'allow_retries\': True, \'num_of_retries\': 3, \'temperature\': 0.5, \'model\': \'gpt-4o\'})]"\n'
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

    # Update Endpoints
    command = 'delete_result ' + nameOfRunnerFileName + '\n'
    print('Command:', command)
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    # Update Endpoints
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
    last_line = output_lines[-2]
    print('=========================Output Last Line:', last_line)
    assert last_line.replace(" ", "") == "Areyousureyouwanttodeletetheresult(y/N)?[delete_result]:Resultdeleted."


def test_cli_delete_runner():
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

    # # Example command to send to the process
    # process.stdin.write('list_cookbooks\n')
    # process.stdin.flush()

    # Update Endpoints
    command = 'update_endpoint azure-openai-gpt4o "[(\'name\', \'Azure OpenAI GPT4o\'), (\'uri\', \'' + str(
        AZURE_OPENAI_URI) + '\'), (\'token\', \'' + str(
        AZURE_OPENAI_TOKEN) + '\'), (\'params\', {\'timeout\': 300, \'allow_retries\': True, \'num_of_retries\': 3, \'temperature\': 0.5, \'model\': \'gpt-4o\'})]"\n'
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

    # Update Endpoints
    command = 'delete_runner ' + nameOfRunnerFileName + '\n'
    print('Command:', command)
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    # Update Endpoints
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
    last_line = output_lines[-2]
    print('=========================Output Last Line:', last_line)
    assert last_line.replace(" ", "") == "Areyousureyouwanttodeletetherunner(y/N)?[delete_runner]:Runnerdeleted."


def test_cli_delete_runner():
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

    # Update Endpoints
    command = 'update_endpoint azure-openai-gpt4o "[(\'name\', \'Azure OpenAI GPT4o\'), (\'uri\', \'' + str(
        AZURE_OPENAI_URI) + '\'), (\'token\', \'' + str(
        AZURE_OPENAI_TOKEN) + '\'), (\'params\', {\'timeout\': 300, \'allow_retries\': True, \'num_of_retries\': 3, \'temperature\': 0.5, \'model\': \'gpt-4o\'})]"\n'
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

    # Update Endpoints
    command = 'delete_runner ' + nameOfRunnerFileName + '\n'
    print('Command:', command)
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    # Update Endpoints
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
    last_line = output_lines[-2]
    print('=========================Output Last Line:', last_line)
    assert last_line.replace(" ", "") == "Areyousureyouwanttodeletetherunner(y/N)?[delete_runner]:Runnerdeleted."


def test_cli_list_cookbooks():
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

    # Update Endpoints
    command = 'update_endpoint azure-openai-gpt4o "[(\'name\', \'Azure OpenAI GPT4o\'), (\'uri\', \'' + str(
        AZURE_OPENAI_URI) + '\'), (\'token\', \'' + str(
        AZURE_OPENAI_TOKEN) + '\'), (\'params\', {\'timeout\': 300, \'allow_retries\': True, \'num_of_retries\': 3, \'temperature\': 0.5, \'model\': \'gpt-4o\'})]"\n'
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


def test_cli_list_runs():
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

    # Update Endpoints
    command = 'update_endpoint azure-openai-gpt4o "[(\'name\', \'Azure OpenAI GPT4o\'), (\'uri\', \'' + str(
        AZURE_OPENAI_URI) + '\'), (\'token\', \'' + str(
        AZURE_OPENAI_TOKEN) + '\'), (\'params\', {\'timeout\': 300, \'allow_retries\': True, \'num_of_retries\': 3, \'temperature\': 0.5, \'model\': \'gpt-4o\'})]"\n'
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

    print('Output:', stdout)
    # Split the output into lines
    output_lines = stdout.splitlines()

    # Get the last line of the output
    last_line = output_lines[12]
    print('=========================Output Last Line:', last_line)
    assert last_line.replace(" ", "") == "Cookbook\"Mynewcookbook" + timestamp_int + "\""

def test_cli_view_recipe():
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

def test_cli_view_metric():
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

    # Update Endpoints
    command = 'update_endpoint azure-openai-gpt4o "[(\'name\', \'Azure OpenAI GPT4o\'), (\'uri\', \'' + str(
        AZURE_OPENAI_URI) + '\'), (\'token\', \'' + str(
        AZURE_OPENAI_TOKEN) + '\'), (\'params\', {\'timeout\': 300, \'allow_retries\': True, \'num_of_retries\': 3, \'temperature\': 0.5, \'model\': \'gpt-4o\'})]"\n'
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

    # Update Endpoints
    command = 'update_endpoint azure-openai-gpt4o "[(\'name\', \'Azure OpenAI GPT4o\'), (\'uri\', \'' + str(
        AZURE_OPENAI_URI) + '\'), (\'token\', \'' + str(
        AZURE_OPENAI_TOKEN) + '\'), (\'params\', {\'timeout\': 300, \'allow_retries\': True, \'num_of_retries\': 3, \'temperature\': 0.5, \'model\': \'gpt-4o\'})]"\n'
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

    # Update Endpoints
    command = 'update_endpoint azure-openai-gpt4o "[(\'name\', \'Azure OpenAI GPT4o\'), (\'uri\', \'' + str(
        AZURE_OPENAI_URI) + '\'), (\'token\', \'' + str(
        AZURE_OPENAI_TOKEN) + '\'), (\'params\', {\'timeout\': 300, \'allow_retries\': True, \'num_of_retries\': 3, \'temperature\': 0.5, \'model\': \'gpt-4o\'})]"\n'
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
