"""
A Unit test for module2_variantvalidator.py
"""
# Import necessary packages
import pytest
from module2_variantvalidator import get_genomic_info_from_transcript

# Test function for genomic info from transcript endpoint
@pytest.mark.parametrize("transcript_id, expected_result", [
    ("INSERT REF SEQ TRANSCRIPT ID", (["EXPECTED OUTPUT"], ["EXPECTED OUTPUT"])),
    # Add more test cases as needed
])
def test_get_genomic_info_from_transcript(transcript_id, expected_result):
    genomic_hgvs, genomic_coordinates = get_genomic_info_from_transcript(transcript_id)
    assert (genomic_hgvs, genomic_coordinates) == expected_result

