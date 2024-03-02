"""
Unit Testing of Module4_VEP_code.py
"""
import requests
import requests_mock

from Modules.module4_VEP import get_variant_annotation  # Import module4 function


def test_get_variant_annotation():
    with requests_mock.Mocker() as m:
        # Mock URL
        mock_url = 'https://rest.ensembl.org/vep/human/hgvs/NM_000138.5:c.356G>A'
        # Expected mock response data
        mock_response_data = "VEP result for NM_000138.5:c.356G>A"
        # Setup mock
        m.get(mock_url, json=mock_response_data)

        # Expected result
        expected_result = "VEP result for NM_000138.5:c.356G>A"

        # Call the function with a test transcript
        result = get_variant_annotation("NM_000138.5:c.356G>A")

        # Assert that the function returns the expected result based on the mock response
        assert result == expected_result


def test_get_variant_annotation_failure():
    genomic_transcript = "NM_invalid"
    with requests_mock.Mocker() as m:
        m.get("https://rest.ensembl.org/vep/human/hgvs/NM_invalid",
              status_code=404)

        result = get_variant_annotation(genomic_transcript)
        assert result == None


def test_get_variant_annotation_exception():
    genomic_transcript = "NM_except"
    with requests_mock.Mocker() as m:
        m.get("https://rest.ensembl.org/vep/human/hgvs/NM_except",
              exc=requests.exceptions.ConnectTimeout)

        result = get_variant_annotation(genomic_transcript)
        assert result is None
