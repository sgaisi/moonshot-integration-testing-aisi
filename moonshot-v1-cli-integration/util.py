# utils.py

import pytest

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
