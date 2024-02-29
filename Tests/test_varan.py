import pytest
from Varan import application

@pytest.fixture
def client():
    application.config['TESTING'] = True  # Enable testing mode
    with application.test_client() as client:
        yield client

def test_variant_annotation_tool(client):
    # Example test for the "/<select_transcripts>/<transcript_model>/<genome_build>" endpoint
    select_transcripts = 'refseq'
    transcript_model = 'NM_000093.4'
    genome_build = 'GRCh37'
    content_type = 'application/json'  # or 'text/xml'

    # Construct the URL
    url = f"/transcript-mapper/{select_transcripts}/{transcript_model}/{genome_build}?content-type={content_type}"

    # Make a GET request
    response = client.get(url)

    # Assert the status code and response data structure
    assert response.status_code == 200
    # For JSON response
    if content_type == 'application/json':
        assert 'application/json' in response.content_type
        data = response.get_json()
        # Check if the response data is as expected
        assert isinstance(data, list)  # Check if the response is a list

