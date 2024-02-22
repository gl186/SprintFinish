"""
Unit Testing of Module5_VR_SPDI_code.py using Pytest- Nurhayu
"""
from Modules.module5_VR_SPDI_code import get_SPDI  # Import module5 function
import pytest

# The code that interacts with Ensembl Variant Recoder
def get_SPDI(spdi):
    # Connect to Ensembl Variant Recoder and retrieve relevant data

    return f"SPDI result for {spdi}"

# Define a fixture for spdi
@pytest.fixture
def spdi():
    return "spdi"

# Write the test
def test_get_SPDI(spdi):
    result = get_SPDI(spdi)
    expected_result = "SPDI result for spdi"
    assert result == expected_result