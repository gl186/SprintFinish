import sys
import os
import pytest
import re
from unittest import mock
import requests_mock
from Modules.module1_variantrecoder import ensemblMapper
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_ensembl_mapper_success():
    with requests_mock.Mocker() as m:
        # Mock URL
        mock_url = 'https://rest.ensembl.org/variant_recoder/human/ENST00000366667:c.803C>T'
        # Expected mock response data
        mock_response_data = {"Genomic-HGVS": [{"hgvsg": "mocked_hgvs_response"}]}
        # Setup mock
        m.get(mock_url, json=mock_response_data)

        # Expected result
        expected_result = {"Genomic-HGVS": mock_response_data}

        # Call the function with a test transcript
        result = ensemblMapper("ENST00000366667:c.803C>T")

        # Assert that the function returns the expected result based on the mock response
        assert result == expected_result


# def test_ensembl_mapper_failure():
#     with requests_mock.Mocker() as m:
#         # Mock URL for a case that should fail or return empty
#         mock_url = 'https://rest.ensembl.org/variant_recoder/human/'
#         # Mock response for a failure scenario
#         m.get(mock_url, status_code=404)
#
#         # Expected result for a failure
#         expected_result = {"Genomic-HGVS": []}  # Adjust based on how your function handles errors
#
#         # Attempt to call the function with a transcript that causes failure
#         result = ensemblMapper("ENST00000366667:c.803C>T")
#
#         # Assert
#         assert result == expected_result


# def test_ensembl_mapper_failure():
#     with requests_mock.Mocker() as m:
#         # Use a regex to match any request to the variant recoder endpoint
#         mock_url_regex = re.compile(r'https://rest\.ensembl\.org/variant_recoder/human/.*')
#
#         # Setup the mock to return a 404 for any URL matching the regex
#         m.register_uri('GET', mock_url_regex, status_code=404)
#
#         # Example input, but your function should be able to handle any valid input since the mock is generalized
#         input_variant = "ENST00000366667:c.803C>T"
#
#         # Expected result for a failure, adjust based on your function's error handling
#         expected_result = {"Genomic-HGVS": []}
#
#         # Attempt to call the function with a variant
#         result = ensemblMapper(input_variant)
#
#         # Assert that the result matches the expected failure output
#         assert result == expected_result, "Function did not handle failure as expected"


def test_ensembl_mapper_failure():
    with requests_mock.Mocker() as m:
        mock_url_regex = re.compile(r'https://rest\.ensembl\.org/variant_recoder/human/.*')
        # Return a simple text message or empty content with a 404 status
        m.register_uri('GET', mock_url_regex, text='Not Found', status_code=404)

        input_variant = "ENST00000366667:c.803C>T"
        expected_result = {"Genomic-HGVS": []}

        result = ensemblMapper(input_variant)

        assert result == expected_result
