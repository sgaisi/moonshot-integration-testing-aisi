import subprocess

def test_benchmark():

    # Setup Moonshot CLI Subprocess
    run_cli_process = subprocess.Popen(["python3", "-m", "moonshot", "cli", "interactive"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, cwd="/Users/benedict/Documents/GitHub/test")
    
    # Send CLI Commands
    output, error = run_cli_process.communicate(input='run_recipe "my new recipe runner 2" "[\'bbq\',\'mmlu\']" "[\'azure-openai-gpt4o\']" -n 1 -r 1 -s "You are an intelligent AI"') # Opens IO stream, write input, provide output and close IO stream

    # Print CLI Output
    output_string = "Time taken to run" in output
    error_string = "" in error
    print(output_string)
    print(error_string)

    # Assert Output & Error String
    assert output_string == True
    assert error_string == True