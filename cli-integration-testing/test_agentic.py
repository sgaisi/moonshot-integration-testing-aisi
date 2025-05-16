import subprocess
from dotenv import load_dotenv
import os
import time
from util.utils import *

load_dotenv()  # Load environment variables from .env file

OPENAI_URI = os.getenv('OPENAI_URI')
OPENAI_TOKEN = os.getenv('OPENAI_TOKEN')
TOGETHER_TOKEN= os.getenv('TOGETHER_TOKEN')
CLI_DIR = os.getenv('CLI_DIR')

COMMAND = ('python -m moonshot cli interactive')

ENDPOINT = "openai-gpt4o"
ENDPOINT_NAME = "OpenAI GPT4o"
DATASET = "jt3-leakage-ia-en"

timestamp = time.time()
timestamp_int = str(int(timestamp))

RUNNER_NAME = "int-test-runner-" + timestamp_int

ORIGINAL_METRIC_FILE = "jointtesting3"
copy_file(f'{CLI_DIR}/moonshot-data-aisi/metrics/{ORIGINAL_METRIC_FILE}.py')
METRIC_FILE = f"copy_of_{ORIGINAL_METRIC_FILE}_{timestamp_int}"
rename_file(f'{CLI_DIR}/moonshot-data-aisi/metrics/copy_of_{ORIGINAL_METRIC_FILE}.py', f'{METRIC_FILE}.py')

RECIPE_FILE = "jt3-leakage-en"
copy_file(f'{CLI_DIR}/moonshot-data-aisi/recipes/{RECIPE_FILE}.json')
RECIPE_TO_DELETE = f"copy_of_{RECIPE_FILE}_{timestamp_int}"
rename_file(f'{CLI_DIR}/moonshot-data-aisi/recipes/copy_of_{RECIPE_FILE}.json', f'{RECIPE_TO_DELETE}.json')

def test_cli_view_recipe_agentic():
    # Initialize process
    process = subprocess.Popen(
        COMMAND,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        stdin=subprocess.PIPE,
        text=True,
        cwd=str(CLI_DIR),
    )
    print('Path:', str(CLI_DIR))
    if process.stdin is None:
        raise RuntimeError("Failed to create stdin for the subprocess")

    # Execute view_recipe
    command = (f'view_recipe {RECIPE_FILE}\n')
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
    assert last_line.replace(" ", "") == "ListofRecipes"

def test_cli_run_recipe_agentic():
    # Initialize process
    process = subprocess.Popen(
        COMMAND,
        shell=True,
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
    command = (
        f'update_endpoint {ENDPOINT} "[(\'name\', \'{ENDPOINT_NAME}\'), '
        f'(\'uri\', \'{str(OPENAI_URI)}\'), (\'token\', \'{str(OPENAI_TOKEN)}\'), '
        '(\'params\', {\'timeout\': 300,\'max_attempts\': 3, \'temperature\': 0.5})]"\n'
    )
    print('Command:', command)
    process.stdin.write(command)
    process.stdin.flush()

    # Execute run_recipe
    command = f'run_recipe "{RUNNER_NAME}" "[\'{RECIPE_FILE}\']" "[\'{ENDPOINT}\']" -l agentic -n 1 -r 1 -s " "\n'
    print('Command:', command)
    process.stdin.write(command)
    process.stdin.flush()

    # Capture the output and errors
    stdout, stderr = process.communicate()

    print("ERROR::" + stderr)
    # Validate output
    print('Output:', stdout)
    output_lines = stdout.splitlines()
    last_line = output_lines[-12]
    print('=========================Output Last Line:', last_line)
    assert last_line.replace(" ", "") == "RecipesResult"

def test_cli_view_dataset_agentic():
    # Initialize process
    process = subprocess.Popen(
        COMMAND,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        stdin=subprocess.PIPE,
        text=True,
        cwd=str(CLI_DIR),
    )
    print('Path:', str(CLI_DIR))
    if process.stdin is None:
        raise RuntimeError("Failed to create stdin for the subprocess")

    # Execute view_dataset
    command = (f'view_dataset {DATASET}\n')
    print('Command:', command)
    process.stdin.write(command)
    process.stdin.flush()

    # Capture the output and errors
    stdout, stderr = process.communicate()

    # Validate output
    print('Output:', stdout)
    output_lines = stdout.splitlines()
    last_line = output_lines[12]
    print('=========================Output Last Line:', last_line)
    assert last_line.replace(" ", "") == "ListofDatasets"

def test_cli_view_metric_agentic():
    # Initialize process
    process = subprocess.Popen(
        COMMAND,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        stdin=subprocess.PIPE,
        text=True,
        cwd=str(CLI_DIR),
    )
    print('Path:', str(CLI_DIR))
    if process.stdin is None:
        raise RuntimeError("Failed to create stdin for the subprocess")

    # Execute view_metric
    command = (f'view_metric {METRIC_FILE}\n')
    print('Command:', command)
    process.stdin.write(command)
    process.stdin.flush()

    # Capture the output and errors
    stdout, stderr = process.communicate()

    # Validate output
    print('Output:', stdout)
    output_lines = stdout.splitlines()
    last_line = output_lines[12]
    print('=========================Output Last Line:', last_line)
    assert last_line.replace(" ", "") == "ListofMetrics"

def test_cli_view_result_agentic():
    # Initialize process
    process = subprocess.Popen(
        COMMAND,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        stdin=subprocess.PIPE,
        text=True,
        cwd=str(CLI_DIR),
    )
    print('Path:', str(CLI_DIR))
    if process.stdin is None:
        raise RuntimeError("Failed to create stdin for the subprocess")

    # Execute view_result
    command = f'view_result {RUNNER_NAME}\n'
    process.stdin.write(command)
    process.stdin.flush()

    # Capture the output and errors
    stdout, stderr = process.communicate()

    # Validate output
    print('Output:', stdout)
    output_lines = stdout.splitlines()
    last_line = output_lines[-12]
    print('=========================Output Last Line:', last_line)
    assert last_line.replace(" ", "") == "RecipesResult"

def test_cli_view_run_agentic():
    # Initialize process
    process = subprocess.Popen(
        COMMAND,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        stdin=subprocess.PIPE,
        text=True,
        cwd=str(CLI_DIR),
    )
    print('Path:', str(CLI_DIR))
    if process.stdin is None:
        raise RuntimeError("Failed to create stdin for the subprocess")

    # Execute view_run
    command = f'view_run {RUNNER_NAME}\n'
    process.stdin.write(command)
    process.stdin.flush()

    # Capture the output and errors
    stdout, stderr = process.communicate()

    # Validate output
    print('Output:', stdout)
    output_lines = stdout.splitlines()
    last_line = output_lines[11]
    print('=========================Output Last Line:', last_line)
    assert last_line.replace(" ", "") == "ListofRuns"

def test_cli_view_runner_agentic():
    # Initialize process
    process = subprocess.Popen(
        COMMAND,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        stdin=subprocess.PIPE,
        text=True,
        cwd=str(CLI_DIR),
    )
    print('Path:', str(CLI_DIR))
    if process.stdin is None:
        raise RuntimeError("Failed to create stdin for the subprocess")

    # Execute view_runner
    command = f'view_runner {RUNNER_NAME}\n'
    process.stdin.write(command)
    process.stdin.flush()

    # Capture the output and errors
    stdout, stderr = process.communicate()

    # Validate output
    print('Output:', stdout)
    output_lines = stdout.splitlines()
    last_line = output_lines[11]
    print('=========================Output Last Line:', last_line)
    assert last_line.replace(" ", "") == "ListofRunners"

def test_cli_delete_metric_agentic():
    # Initialize process
    process = subprocess.Popen(
        COMMAND,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        stdin=subprocess.PIPE,
        text=True,
        cwd=str(CLI_DIR),
    )
    print('Path:', str(CLI_DIR))
    if process.stdin is None:
        raise RuntimeError("Failed to create stdin for the subprocess")

    # Execute delete_metric
    command = f'delete_metric {METRIC_FILE} \n'
    print('Command:', command)
    process.stdin.write(command)
    process.stdin.flush()
    command = 'y\n'
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
    assert last_line.replace(" ", "") == "Areyousureyouwanttodeletethemetric(y/N)?[delete_metric]:Metricdeleted."

def test_cli_delete_result_agentic():
    # Initialize process
    process = subprocess.Popen(
        COMMAND,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        stdin=subprocess.PIPE,
        text=True,
        cwd=str(CLI_DIR),
    )
    print('Path:', str(CLI_DIR))
    if process.stdin is None:
        raise RuntimeError("Failed to create stdin for the subprocess")

    # Execute delete_result
    command = f'delete_result {RUNNER_NAME}\n'
    print('Command:', command)
    process.stdin.write(command)
    process.stdin.flush()
    command = 'y\n'
    print('Command:', command)
    process.stdin.write(command)
    process.stdin.flush()

    # Capture the output and errors
    stdout, stderr = process.communicate()

    # Validate output
    print('Output:', stdout)
    output_lines = stdout.splitlines()
    last_line = output_lines[-2]
    print('=========================Output Last Line:', last_line)
    assert last_line.replace(" ", "") == "Areyousureyouwanttodeletetheresult(y/N)?[delete_result]:Resultdeleted."


def test_cli_delete_runner_agentic():
    # Initialize process
    process = subprocess.Popen(
        COMMAND,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        stdin=subprocess.PIPE,
        text=True,
        cwd=str(CLI_DIR),
    )
    print('Path:', str(CLI_DIR))
    if process.stdin is None:
        raise RuntimeError("Failed to create stdin for the subprocess")

    # Execute delete_runner
    command = f'delete_runner {RUNNER_NAME}\n'
    print('Command:', command)
    process.stdin.write(command)
    process.stdin.flush()
    command = 'y\n'
    print('Command:', command)
    process.stdin.write(command)
    process.stdin.flush()

    # Capture the output and errors
    stdout, stderr = process.communicate()

    # Validate output
    print('Output:', stdout)
    output_lines = stdout.splitlines()
    last_line = output_lines[-2]
    print('=========================Output Last Line:', last_line)
    assert last_line.replace(" ", "") == "Areyousureyouwanttodeletetherunner(y/N)?[delete_runner]:Runnerdeleted."

def test_cli_delete_recipe_agentic():
    # Initialize process
    process = subprocess.Popen(
        COMMAND,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        stdin=subprocess.PIPE,
        text=True,
        cwd=str(CLI_DIR),
    )
    print('Path:', str(CLI_DIR))
    if process.stdin is None:
        raise RuntimeError("Failed to create stdin for the subprocess")

    # Execute delete_recipe
    command = f'delete_recipe {RECIPE_TO_DELETE}\n'
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
