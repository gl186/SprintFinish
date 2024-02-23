 Set up Functional test for main.py
import pytest
from unittest.mock import patch
from Main import app

# Test case for calling module function with ENST transcript ID
@patch('module1_variantrecoder.function1', return_value="Module 1 Output")
def test_call_module_function_with_ENST(mock_function1):
    with app.test_client() as client:
        data = {"transcript_id": "ENST12345"}
        response = client.post('/module_function', json=data)
        assert response.status_code == 200
        assert response.json == {"module1_output": "Module 1 Output", "transcript_id": "ENST12345"}

# Test case for calling module function with NM transcript ID
@patch('module2_variantvalidator.function2', return_value="Module 2 Output")
def test_call_module_function_with_NM(mock_function2):
    with app.test_client() as client:
        data = {"transcript_id": "NM_12345"}
        response = client.post('/module_function', json=data)
        assert response.status_code == 200
        assert response.json == {"module2_output": "Module 2 Output", "transcript_id": "NM_12345"}

# Test case for calling module function with invalid transcript ID
def test_call_module_function_with_invalid_transcript_id():
    with app.test_client() as client:
        data = {"transcript_id": "Invalid_ID"}
        response = client.post('/module_function', json=data)
        assert response.status_code == 400
        assert response.data.decode() == "Invalid input: transcript_id should contain 'ENST' or 'NM_'"

# Test case for calling module function with missing JSON data
def test_call_module_function_with_missing_json_data():
    with app.test_client() as client:
        response = client.post('/module_function')
        assert response.status_code == 400
        assert response.data.decode() == "Invalid input: JSON data not provided"

