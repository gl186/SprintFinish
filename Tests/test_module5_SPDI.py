"""
Unit Testing of Module4_VEP_code.py using
"""
import requests
import requests_mock
from Modules.module5_SPDI import get_variant_annotation2  # Import module5 function


def test_get_variant_annotation2():
    with requests_mock.Mocker() as m:
        # Mock URL
        mock_url = 'https://rest.ensembl.org/variant_recoder/human/rs56116432.?'
        # Expected mock response data
        mock_response_data = "SPDI result for rs56116432."
        # Setup mock
        m.get(mock_url, json=mock_response_data)

        # Expected result
        expected_result = "SPDI result for rs56116432."

        # Call the function with a test transcript
        result = get_variant_annotation2("rs56116432.")

        # Assert that the function returns the expected result based on the mock response
        assert result == expected_result


def test_get_variant_annotation2_failure():
    genomic_transcript = "rs_invalid"
    with requests_mock.Mocker() as m:
        m.get("https://rest.ensembl.org/variant_recoder/human/rs_invalid?",
              status_code=404)

        result = get_variant_annotation2(genomic_transcript)
        assert result == None


def test_get_variant_annotation2_exception():
    genomic_transcript = "rs_except"
    with requests_mock.Mocker() as m:
        m.get("https://rest.ensembl.org/variant_recoder/human/rs_except?",
              exc=requests.exceptions.ConnectTimeout)

        result = get_variant_annotation2(genomic_transcript)
        assert result is None
