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
DATASET_1 = "jt3-leakage-te-en"
DATASET_2 = "jt3-leakage-ia-en"

timestamp = time.time()
timestamp_int = str(int(timestamp))

ORIGINAL_METRIC_FILE = "jointtesting3"
copy_file(f'{CLI_DIR}/moonshot-data-aisi/metrics/{ORIGINAL_METRIC_FILE}.py')
METRIC_FILE = f"copy_of_{ORIGINAL_METRIC_FILE}_{timestamp_int}"
rename_file(f'{CLI_DIR}/moonshot-data-aisi/metrics/copy_of_{ORIGINAL_METRIC_FILE}.py', f'{METRIC_FILE}.py')

COOKBOOK_NAME = f"test-agentic-cookbook-{timestamp_int}"
COOKBOOK_RUNNER_NAME = f"{COOKBOOK_NAME}-runner"

RECIPE_NAME = f"test-agentic-recipe-{timestamp_int}"
RECIPE_RUNNER_NAME = f"{RECIPE_NAME}-runner"

def test_cli_add_cookbook_agentic():
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
            'add_cookbook \'' + COOKBOOK_NAME + '\' \'I am cookbook description\' "[\'jt3-leakage-en\', \'jt3-fraud-en\']"\n')
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

def test_cli_add_recipe_agentic():
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
 
    # Execute add_recipe
    command = (
        f'add_recipe \'{RECIPE_NAME}\' \'Test recipe description\' "[\'category1\',\'category2\']" '
        f'"[\'{DATASET_1}\']" "[\'{METRIC_FILE}\']" -p "[]" -t "[\'tag1\',\'tag2\']" '
        '-g "{\'A\':[80,100],\'B\':[60,79],\'C\':[40,59],\'D\':[20,39],\'E\':[0,19]}"\n'
    )
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
    assert last_line.replace(" ", "") == f"[add_recipe]:Recipe({RECIPE_NAME})created."

def test_cli_run_cookbook_agentic():
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
    process.stdin.write(command)
    process.stdin.flush()

    # Execute run_cookbook
    command = f'run_cookbook "{COOKBOOK_RUNNER_NAME}" "[\'{COOKBOOK_NAME}\']" "[\'{ENDPOINT}\']" -l agentic -n 1 -r 1 -s " "\n'
    print('Command:', command)
    process.stdin.write(command)
    process.stdin.flush()

    # Capture the output and errors
    stdout, stderr = process.communicate()
    print('STDERR:', stderr)

    # Validate output
    print('Output:', stdout)
    output_lines = stdout.splitlines()
    last_line = output_lines[-16]
    print('=========================Output Last Line:', last_line)
    assert last_line.replace(" ", "") == "CookbookResult"

def test_cli_run_recipe_agentic():
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
    process.stdin.write(command)
    process.stdin.flush()

    # Execute run_recipe
    command = f'run_recipe "{RECIPE_RUNNER_NAME}" "[\'{RECIPE_NAME}\']" "[\'{ENDPOINT}\']" -l agentic -n 1 -r 1 -s " "\n'
    print('Command:', command)
    process.stdin.write(command)
    process.stdin.flush()

    # Capture the output and errors
    stdout, stderr = process.communicate()
    print('STDERR:', stderr)

    # Validate output
    print('Output:', stdout)
    output_lines = stdout.splitlines()
    last_line = output_lines[-12]
    print('=========================Output Last Line:', last_line)
    assert last_line.replace(" ", "") == "RecipesResult"

def test_cli_update_cookbook_agentic():
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
 
    # Execute update_cookbook
    command = (f'update_cookbook {COOKBOOK_NAME} "[(\'name\', \'{COOKBOOK_NAME}-new\'),'
               ' (\'description\', \'Updated description\'), (\'recipes\', [\'jt3-leakage-en\'])]"\n')
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
    assert last_line.replace(" ", "") == "[update_cookbook]:Cookbookupdated."

def test_cli_update_recipe_agentic():
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
 
    # Execute update_recipe
    command = (f'update_recipe {RECIPE_NAME} "[(\'name\', \'{RECIPE_NAME}-new\'), (\'tags\', [\'fairness\'])]"\n')
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
    assert last_line.replace(" ", "") == "[update_recipe]:Recipeupdated."

def test_cli_view_cookbook_agentic():
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

    # Execute view_cookbook
    command = ('view_cookbook ' + COOKBOOK_NAME + ' \n')
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
    assert last_line.replace(" ", "") == "Cookbook:\"" + COOKBOOK_NAME + "-new\""

def test_cli_view_recipe_agentic():
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
    command = (f'view_recipe {RECIPE_NAME}\n')
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

def test_cli_view_dataset_agentic():
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
    command = (f'view_dataset {DATASET_2}\n')
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
    command = f'view_result {RECIPE_RUNNER_NAME}\n'
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
    command = f'view_run {RECIPE_RUNNER_NAME}\n'
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
    command = f'view_runner {RECIPE_RUNNER_NAME}\n'
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
    command = f'delete_result {RECIPE_RUNNER_NAME}\n'
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
    command = f'delete_runner {RECIPE_RUNNER_NAME}\n'
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
    command = f'delete_recipe {RECIPE_NAME}\n'
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

def test_cli_delete_cookbook_agentic():
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
