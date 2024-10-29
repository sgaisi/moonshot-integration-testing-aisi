import random
import subprocess
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

CLI_DIR = '/Users/jacksonboey/PycharmProjects/moonshot'
def test_cli_benchmark():
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
