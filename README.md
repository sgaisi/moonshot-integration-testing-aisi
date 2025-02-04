# Moonshot Integration Testing

## Overview

This repository contains integration tests for [Project Moonshot](https://github.com/aiverify-foundation/moonshot), a toolkit designed to evaluate and red-team Large Language Model (LLM) applications. The integration tests ensure that various components of Moonshot work seamlessly together, maintaining the toolkit's reliability and performance.

## Prerequisites

Before running the integration tests, ensure you have the following installed:

- **Python**: Version 3.11 or later
- **Node.js**: Version 20.11.1 LTS or later (if testing the Web UI)
- **Git**: For version control

## Installation

**Clone the Repository**:

   ```bash
   git clone https://github.com/aiverify-foundation/moonshot-integration-testing.git
   cd moonshot-integration-testing
   ```

## Running the CLI Integration Tests

To execute the integration tests:

1. **Navigate to the Test Directory**:

   ```bash
   cd cli-integration-testing
   ```
2. **Set Up the Virtual Environment**:

   It's recommended to use a virtual environment to manage dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Python Dependencies**:

   Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```
3. **Setup Env File**:

   Create a .env file:

   ```bash
   touch .env
   ```

   Open the .env file in a text editor and define your environment variables:
   ```bash
   # .env
   AZURE_OPENAI_URI =
   AZURE_OPENAI_TOKEN =
   URI2 = 
   TOKEN2 = 
   ADDITIONAL_PARAMETERS = '{"timeout": 300, "max_attempts": 3,"temperature": 0.5 }'
   TOGETHER_TOKEN = 
   OPENAI_TOKEN = 
   AWS_ACCESS_KEY_ID=""
   AWS_SECRET_ACCESS_KEY=""
   GOOGLE_TOKEN = ""
   CLI_DIR = ''# Path of Moonshot Library
   ```

4. **Run Tests**:

   Use the following command to run all tests:

   ```bash
   pytest
   ```

   For more detailed output:

   ```bash
   pytest -v
   ```

   To run a specific test module:

   ```bash
   pytest test_module.py
   ```
## Running the UI Integration Tests

To execute the integration tests:

1. **Navigate to the Test Directory**:

   ```bash
   cd ui-integration-testing
   ```
2. **Set Up the Virtual Environment**:

   It's recommended to use a virtual environment to manage dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Node Dependencies**:

   Install the required Python packages:

   ```bash
   npm install
   ```
4. **Setup Env File**:

   Create a .env file:

   ```bash
   touch .env
   ```

   Open the .env file in a text editor and define your environment variables:
   ```bash
   # .env
   URI =
   TOKEN =
   URI2 =
   TOKEN2 =
   ADDITIONAL_PARAMETERS = '{"timeout": 300, "max_attempts": 3,"temperature": 0.5 }'
   TOGETHER_TOKEN =
   OPENAI_TOKEN = 
   AWS_ACCESS_KEY_ID=""
   AWS_SECRET_ACCESS_KEY=""
   GOOGLE_TOKEN = 
   ```
5. **Run Tests**:

   Use the following command to run all tests:

   ```bash
   npx playwright test tests
   ```
   To run a specific test module:

   ```bash
   npx playwright test tests/test_module.spec.ts
   ```
   
## Directory Structure

A brief overview of the repository structure:

```
moonshot-integration-testing/         # Integration test cases
├── cli-integration-testing/                   
│   ├── utils                         # Common Utils Functions to support automation on Data Preparation
│   ├── test_api.py                   # Tests for the Moonshot APIs
│   ├── test_benchmark.py             # Tests for the CLI Command - Moonshot Benchmarking CLI Commands Scope
│   ├── test_common.py                # Tests for the CLI Command - Moonshot Common CLI Commands Scope
│   ├── test_red_team.py              # Tests for the CLI Command - Moonshot Red Teaming CLI Commands Scope
│   └── 
├── ui-integration-testing/           # Moonshot UI Integration test cases
│   ├── tests/
│   ├── ├── benchmarking.spec.ts      # Tests for the Web UI - Moonshot Benchmarking Scope
│   ├── ├── endpoint.spec.ts          # Tests for the Web UI - Moonshot Endpoint Scope
│   ├── ├── homepage.spec.ts          # Tests for the Web UI - Moonshot Homepage Scope
│   ├── ├── red_teaming.spec.ts       # Tests for the Web UI - Moonshot Red Teaming Scope
│   └── 
├── .gitignore
├── README.md                # Project documentation
└── LICENSE                  # License information
```

## Contributing

We welcome contributions to enhance the integration tests for Moonshot. To contribute:

1. **Fork the Repository**: Click the "Fork" button at the top right of this page.
2. **Create a New Branch**: Use a descriptive name for your branch.
3. **Make Your Changes**: Implement your improvements or fixes.
4. **Submit a Pull Request**: Provide a clear description of your changes.

Please ensure that your contributions align with the project's coding standards and pass all existing tests.

## License

This project is licensed under the Apache-2.0 License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

Special thanks to all contributors and the AI Verify Foundation for their support in developing and maintaining the Moonshot project.
```

This template provides a comprehensive guide for users and contributors, covering installation, usage, and contribution guidelines. Feel free to customize it further based on the specific details and requirements of your project. 
