import subprocess

def test_redteam():

    # session_command = subprocess.Popen(["echo","use_session 'my-runner'" ], stdout=subprocess.PIPE, text=True)
    
    # Setup Moonshot CLI Subprocess
    run_cli_process = subprocess.Popen(["python3", "-m", "moonshot", "cli", "interactive"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, text=True, cwd="/Users/benedict/Documents/GitHub/test")
    
    # Send CLI Commands
    run_cli_process.stdin.write("use_session 'my-runner'" + "\n")
    run_cli_process.stdin.flush()

    # output, errors = run_cli_process.communicate(input=["use_session 'my_runner'","run_attack_module sample_attack_module \"this is my prompt\" -s \"test system prompt\" -m bleuscore"])
    run_cli_process.stdin.write('run_attack_module "this is my prompt" -s "test system prompt" -m bleuscore' + "\n") # Opens IO stream, write input, provide output and close IO stream
    run_cli_process.stdin.flush()
    run_cli_process.stdin.close()

    output = run_cli_process.stdout.read()
    
    # run_cli_process.stdin.close()
    # output = run_cli_process.stdout.read()

    # Print CLI Output
    print(output)
    # print(errors)

    assert output == "Test 1000"