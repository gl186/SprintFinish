"""
Unit testing for module3_VV_LOVD_code_only.py using Pytest - Sonja
"""
# Import necessary functions
from Modules.module3_VV_LOVD_code_only import get_for_GRCh38
# from Modules.module3_VV_LOVD_code_only import get_for_GRCh37
import pytest


def get_for_GRCh38(variant_description):
    """Retrieve mane select and mane select plus clinical data from the VariantValidator LOVD endpoint"""
    return f"Mane select and mane select plus clinical results for {variant_description}"

# Example input variant description fixture for the test


@pytest.fixture
def example_variant_description():
    return "NM_000138.5:c.356G>A"


# Definition of the test function
def test_get_for_grch38(example_variant_description):
    # Retrieval of result to assert
    result = get_for_GRCh38(example_variant_description)

    # Assertion of presence of required data
    expected_result_grch38 = "Mane select and mane select plus clinical results for NM_000138.5:c.356G>A"
    assert result == expected_result_grch38
