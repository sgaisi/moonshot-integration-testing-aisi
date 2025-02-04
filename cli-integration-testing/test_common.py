import subprocess
from dotenv import load_dotenv
import os
import time
import shutil
from util.utils import *
load_dotenv()  # Load environment variables from .env file

AZURE_OPENAI_URI = os.getenv('URI')
AZURE_OPENAI_TOKEN = os.getenv('TOKEN')
# CLI_DIR = '/Users/jacksonboey/PycharmProjects/moonshot'
CLI_DIR = os.getenv('CLI_DIR')

def test_cli_list_endpoints():
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

    # Update Endpoints
    command = 'list_endpoints'
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
    assert last_line.replace(" ", "") == "ListofConnectorEndpoints"

def test_cli_list_prompt_templates():
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

    # Update Endpoints
    command = 'list_prompt_templates'
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
    assert last_line.replace(" ", "") == "ListofPromptTemplates"

def test_cli_list_connector_types():
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

    # Update Endpoints
    command = 'list_connector_types'
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
    assert last_line.replace(" ", "") == "ListofConnectorTypes"

def test_cli_view_endpoint():
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

        # Update Endpoints
        command = 'view_endpoint openai-gpt4'
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
        assert last_line.replace(" ", "") == "ListofConnectorEndpoints"


def test_cli_view_endpoint():
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

    # Update Endpoints
    command = 'view_endpoint openai-gpt4'
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
    assert last_line.replace(" ", "") == "ListofConnectorEndpoints"

def test_cli_add_endpoints():
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

    # Add Endpoints
    AZURE_MODEL='gpt-4o'
    timestamp = time.time()  # Get the current timestamp in seconds
    timestamp_int = str(int(timestamp))  # Remove the decimal part by converting to an integer
    command = 'add_endpoint azure-openai-gpt4o \'Azure OpenAI GPT4o '+timestamp_int+'\' ' + str(
        AZURE_OPENAI_URI) + ' ' + str(
        AZURE_OPENAI_TOKEN) + ' 1 1 \''+AZURE_MODEL+'\' "{\'timeout\': 300,\'max_attempts\': 3, \'temperature\': 0.5} "\n'

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
    assert last_line.replace(" ", "") == "[add_endpoint]:Endpoint(azure-openai-gpt4o-"+timestamp_int+")created."

def test_cli_delete_endpoint():
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

    # Add Endpoints
    AZURE_MODEL='gpt-4o'
    timestamp = time.time()  # Get the current timestamp in seconds
    timestamp_int = str(int(timestamp))  # Remove the decimal part by converting to an integer
    command = 'add_endpoint azure-openai-gpt4o \'Azure OpenAI GPT4o ' + timestamp_int + '\' ' + str(
        AZURE_OPENAI_URI) + ' ' + str(
        AZURE_OPENAI_TOKEN) + ' 1 1 \'' + AZURE_MODEL + '\' "{\'timeout\': 300,\'max_attempts\': 3, \'temperature\': 0.5} "\n'

    print('Command:', command)
    # Example command to send to the process
    process.stdin.write(command)
    process.stdin.flush()

    endpointName = "azure-openai-gpt4o-"+timestamp_int
    command = 'delete_endpoint ' + endpointName + '\n'
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
    last_line = output_lines[12]
    print('=========================Output Last Line:', last_line)
    assert last_line.replace(" ", "") == "Areyousureyouwanttodeletetheendpoint(y/N)?[delete_endpoint]:Endpointdeleted."

def test_cli_convert_dataset():
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

    timestamp = time.time()  # Get the current timestamp in seconds
    timestamp_int = str(int(timestamp))  # Remove the decimal part by converting to an integer
    # csvFilePath= '/Users/jacksonboey/PycharmProjects/moonshot-integration-testing/cli-integration-testing/your_dataset.csv'
    csvFilePath= '/home/runner/work/moonshot/moonshot/moonshot-integration-testing/cli-integration-testing/your_dataset.csv'
    command = 'convert_dataset \'dataset-name-'+timestamp_int+'\' \'A brief description\' \'http://reference.com\' \'MIT\' \''+csvFilePath+'\'\n'

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
    assert last_line.replace(" ", "") == "[convert_dataset]:Dataset(moonshot-data/datasets/dataset-name-"+timestamp_int+".json)created."

def test_cli_download_dataset_hf():
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

    timestamp = time.time()  # Get the current timestamp in seconds
    timestamp_int = str(int(timestamp))  # Remove the decimal part by converting to an integer
    command = 'download_dataset \'dataset-name-'+timestamp_int+'\' \'A brief description\' \'http://reference.com\' \'MIT\' "{\'dataset_name\': \'cais/mmlu\', \'dataset_config\': \'college_biology\', \'split\': \'dev\', \'input_col\': [\'question\',\'choices\'], \'target_col\': \'answer\'}"\n'
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
    assert last_line.replace(" ", "") == "[download_dataset]:Dataset(moonshot-data/datasets/dataset-name-"+timestamp_int+".json)created."

# def test_cli_download_dataset_csv():
#     command = (
#         'cd .. &&'
#         'source venv/bin/activate &&'
#         'cd moonshot &&'
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
#         #/home/runner/work/moonshot-data/moonshot-data for moonshot data repo
#         #/home/runner/work/moonshot/moonshot-data for moonshot repo
#     )
#     print('Path:', str(CLI_DIR))
#     # Ensure process.stdin is not None
#     if process.stdin is None:
#         raise RuntimeError("Failed to create stdin for the subprocess")
#
#     # # Example command to send to the process
#     # process.stdin.write('list_cookbooks\n')
#     # process.stdin.flush()
#
#     timestamp = time.time()  # Get the current timestamp in seconds
#     timestamp_int = str(int(timestamp))  # Remove the decimal part by converting to an integer
#     csvFilePath = '/Users/jacksonboey/PycharmProjects/moonshot-integration-testing/cli-integration-testing/your_dataset.csv'
#     command = 'download_dataset \'dataset-name-'+timestamp_int+'\' \'A brief description\' \'http://reference.com\' \'MIT\' "{\'csv_file_path\': \''+csvFilePath+'\'}"\n'
#     print('Command:', command)
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
#     last_line = output_lines[11]
#     print('=========================Output Last Line:', last_line)
#     assert last_line.replace(" ", "") == "[download_dataset]:Dataset(moonshot-data/datasets/dataset-name-"+timestamp_int+".json)created."

def test_cli_delete_prompt_template():
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

    # Copy file
    copy_file(CLI_DIR+'/moonshot-data/prompt-templates/squad-shifts.json')

    command = 'delete_prompt_template squad-shifts \n'

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
    current_path = CLI_DIR+"/moonshot-data/prompt-templates/copy_of_squad-shifts.json"  # Replace with the current file path
    new_name = "squad-shifts.json"  # Specify the new file name
    rename_file(current_path, new_name)
    assert last_line.replace(" ", "") == "Areyousureyouwanttodeletetheprompttemplate(y/N)?[delete_prompt_template]:Prompttemplatedeleted."

def test_cli_update_endpoint():
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

    # Update Endpoints
    AZURE_MODEL='gpt-4o'
    timestamp = time.time()  # Get the current timestamp in seconds
    timestamp_int = str(int(timestamp))  # Remove the decimal part by converting to an integer
    command = 'update_endpoint azure-openai-gpt4o "[(\'name\', \'Azure OpenAI GPT4o\'), (\'uri\', \'' + str(
        AZURE_OPENAI_URI) + '\'), (\'token\', \'' + str(
        AZURE_OPENAI_TOKEN) + '\'), (\'model\', \'gpt-4o\'), (\'params\', {\'timeout\': 300,\'max_attempts\': 3, \'temperature\': 0.5})]"\n'
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
    assert last_line.replace(" ", "") == "[update_endpoint]:Endpointupdated."