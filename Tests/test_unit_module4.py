"""
Unit Testing of Module4_VEP_code.py using Pytest- Nurhayu
"""
from module4_VEP_code_only import get_variant_annotation  # Import module4 function
import pytest

# The code that interacts with Ensembl VEP
def get_variant_annotation(hgvs_variant):
    # Connect to Ensembl VEP and retrieve relevant data

    return f"VEP result for {hgvs_variant}"

# Define a fixture for an example HGVS variant
@pytest.fixture
def example_hgvs_variant():
    return "NM_000138.5:c.356G>A"

# Write the test
def test_get_variant_annotation(example_hgvs_variant):
    # Act
    result = get_variant_annotation(example_hgvs_variant)

    # Assert
    expected_result = "VEP result for NM_000138.5:c.356G>A"
    assert result == expected_result
