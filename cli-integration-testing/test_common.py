import random
import subprocess
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

CLI_DIR = '/Users/jacksonboey/PycharmProjects/moonshot'
def test_cli_list_endpoints():
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

    # # Example command to send to the process
    # process.stdin.write('list_cookbooks\n')
    # process.stdin.flush()

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

    # # Example command to send to the process
    # process.stdin.write('list_cookbooks\n')
    # process.stdin.flush()

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

    # # Example command to send to the process
    # process.stdin.write('list_cookbooks\n')
    # process.stdin.flush()

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