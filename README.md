# Moonshot Integration Testing

## Overview

This repository contains integration tests for [Project Moonshot](https://github.com/aiverify-foundation/moonshot), a toolkit designed to evaluate and red-team Large Language Model (LLM) applications. The integration tests ensure that various components of Moonshot work seamlessly together, maintaining the toolkit's reliability and performance.

## Prerequisites

Before running the integration tests, ensure you have the following installed:

- **Python**: Version 3.11 or later
- **Node.js**: Version 20.11.1 LTS or later (if testing the Web UI)
- **Git**: For version control

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/aiverify-foundation/moonshot-integration-testing.git
   cd moonshot-integration-testing
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

4. **Install Node.js Dependencies** (if applicable):

   If your integration tests involve the Moonshot Web UI:

   ```bash
   cd path_to_moonshot_web_ui
   npm install
   ```

## Running the CLI Integration Tests

To execute the integration tests:

1. **Navigate to the Test Directory**:

   ```bash
   cd cli-integration-testing
   ```

2. **Run Tests**:

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
## Running the CLI Integration Tests

To execute the integration tests:

1. **Navigate to the Test Directory**:

   ```bash
   cd cli-integration-testing
   ```

2. **Run Tests**:

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

## Directory Structure

A brief overview of the repository structure:

```
moonshot-integration-testing/
├── ui-integration-testing/                   # Integration test cases
│   ├── __init__.py
│   ├── test_cli.py          # Tests for the CLI
│   ├── test_ui.py           # Tests for the Web UI
│   └── 
├── cli-integration-testing/                   # Integration test cases
│   ├── tests/
│   ├── ├── benchmarking.spec.ts          # Tests for the Web UI - Moonshot Benchmarking
│   ├── ├── red_teaming.spec.ts          # Tests for the Web UI - Moonshot Benchmarking
│   └── 
├── .gitignore
├── requirements.txt         # Python dependencies
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
