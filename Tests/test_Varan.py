"""
This test file is run to test for various Varan.py use cases and scenarios
"""
import pytest
from unittest.mock import patch
from flask import Flask
from Varan import VariantAnnotationToolClass

@pytest.fixture
def client():
    app = Flask(__name__)
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_with_ensembl(client):
    with patch('Varan.Main.call_module1_function', return_value={"results": "Test result from ensembl"}) as mock_call_module1_function:
        response = client.get('/Varan/ensembl/ENST12345/GRCh37')
        assert response.status_code == 200
        assert response.json == {"results": "Test result from ensembl"}
        mock_call_module1_function.assert_called_once_with('ENST12345')

def test_get_with_refseq(client):
    with patch('Varan.Main.module2_variantvalidator.get_genomic_info_from_transcript', return_value={"results": "Test result from refseq"}) as mock_get_genomic_info_from_transcript:
        response = client.get('/Varan/refseq/NM_12345.4/GRCh38')
        assert response.status_code == 200
        assert response.json == {"results": "Test result from refseq"}
        mock_get_genomic_info_from_transcript.assert_called_once_with('NM_12345.4')

def test_get_with_invalid_content_type(client):
    response = client.get('/Varan/invalid_route')
    assert response.status_code == 404

def test_get_with_missing_parameters(client):
    response = client.get('/Varan/ensembl/GRCh37')
    assert response.status_code == 400

def test_get_with_json_content_type(client):
    response = client.get('/Varan/ensembl/ENST12345/GRCh37', headers={'content-type': 'application/json'})
    assert response.status_code == 200
    assert response.content_type == 'application/json'

def test_get_with_xml_content_type(client):
    response = client.get('/Varan/ensembl/ENST12345/GRCh37', headers={'content-type': 'text/xml'})
    assert response.status_code == 200
    assert response.content_type == 'text/xml'
