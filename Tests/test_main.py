import pytest
from unittest.mock import patch
from Main import app, call_module1_function

# Test case for calling module function with ENST transcript ID
@patch('Main.module1_variantrecoder.ensemblMapper', return_value="Module 1 Output")
def test_call_module1_function_with_ENST(mock_ensemblMapper):
    with app.test_client() as client:
        data = {"transcript_model": "ENST12345"}
        response = call_module1_function(data["transcript_model"])
        assert response.status_code == 200
        assert response.json == {"module1_output": "Module 1 Output", "ensembleTranscript": "ENST12345"}

# Test case for calling module function with NM transcript ID
@patch('Main.module2_variantvalidator.get_genomic_info_from_transcript', return_value="Module 2 Output")
def test_call_module1_function_with_NM(mock_get_genomic_info):
    with app.test_client() as client:
        data = {"transcript_model": "NM_12345"}
        response = call_module1_function(data["transcript_model"])
        assert response.status_code == 200
        assert response.json == {"module2_output": "Module 2 Output", "transcript_id": "NM_12345"}

# Test case for calling module function with invalid transcript ID
def test_call_module1_function_with_invalid_transcript_id():
    with app.test_client() as client:
        response = call_module1_function("Invalid_ID")
        assert response.status_code == 400
        assert response.data.decode() == "Invalid input: transcript_id should contain 'ENST' or 'NM_'"

# Test case for calling module function with missing JSON data
def test_call_module1_function_with_missing_json_data():
    with app.test_client() as client:
        response = call_module1_function("")
        assert response.status_code == 400
        assert response.data.decode() == "Invalid input: JSON data not provided"
