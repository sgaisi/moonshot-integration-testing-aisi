import subprocess
from dotenv import load_dotenv
import os
import random

load_dotenv()  # Load environment variables from .env file

OPENAI_TOKEN = os.getenv('OPENAI_TOKEN')
MOON_V1_CLI_DIR = os.getenv('CLI_DIR')
def test_cli_run_benchmarking():

    # Generate a random number between 0 and 999,999,999 (inclusive)
    random_number = int(random.random() * 1000000000)
    nameOfRunnerName = "my-benchmarking-runner-" + str(random_number)

    commands = [
        "export OPENAI_API_KEY="+OPENAI_TOKEN,
        "poetry run python __main__.py create-benchmark-test " + nameOfRunnerName + " mmlu-mini refusal_adapter my-gpt4o"
    ]
    # Join commands with '&&' to ensure the next runs only if the previous succeeds
    full_command = "&&".join(commands)
    print(f"Running combined command: {full_command}")

    process = subprocess.Popen(
        full_command,
        shell=True,  # Allows for complex shell commands
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        stdin=subprocess.PIPE,
        text=True,
        cwd=str(CLI_DIR),
    )
    print('Path:', str(CLI_DIR))
    # Ensure process.stdin is not None
    if process.stdin is None:
        raise RuntimeError("Failed to create stdin for the subprocess")

    # Capture the output and errors
    stdout, stderr = process.communicate()

    print('Output:', stdout)
    # Split the output into lines
    output_lines = stdout.splitlines()

    # Get the last line of the output
    line_12 = output_lines[-12]
    line_12_expected = "File written"
    line_11 = output_lines[-11]
    line_11_expected = "successfully at:"
    line_10 = output_lines[-10]
    line_10_expected = "data/results/my-benchm"
    print('=========================Output Last Line:', line_12)
    print('=========================Output Last Line:', line_11)
    print('=========================Output Last Line:', line_10)
    assert line_12.replace(" ", "") == line_12_expected.replace(" ", "")
    assert line_11.replace(" ", "") == line_11_expected.replace(" ", "")
    assert line_10.replace(" ", "") == line_10_expected.replace(" ", "")

