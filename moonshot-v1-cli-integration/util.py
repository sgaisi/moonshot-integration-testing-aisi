# utils.py
import pytest
import os


def parametrize(*args, **kwargs):
    """A utility wrapper for pytest's parametrize."""
    return pytest.mark.parametrize(*args, **kwargs)

# Predefined parameter sets for reuse
INPUT_PARAMS = [
    1,
    1.1,
    -1,
    0,
    "@1",
    "test"
]
def check_result_file_exists(filepath):
    assert os.path.isfile(filepath), f"Error: File '{filepath}' does not exist."