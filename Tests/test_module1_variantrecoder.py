import re
import requests_mock
from Modules.module1_variantrecoder import ensemblMapper


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


def test_ensembl_mapper_failure():
    with requests_mock.Mocker() as m:
        mock_url_regex = re.compile(r'https://rest\.ensembl\.org/variant_recoder/human/.*')
        # Return a simple text message or empty content with a 404 status
        m.register_uri('GET', mock_url_regex, text='Not Found', status_code=404)

        input_variant = "ENST00000366667:c.803C>T"
        expected_result = {"Genomic-HGVS": []}

        result = ensemblMapper(input_variant)

        assert result == expected_result
