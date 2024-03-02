"""Functional testing for the API"""

import pytest
from Varan import application


@pytest.fixture
def client():
    application.config['TESTING'] = True  # Enable testing mode
    with application.test_client() as client:
        yield client


def test_HGVS_endpoint(client):
    # Example test for the "/<select_transcripts>/<transcript_model>/<genome_build>" endpoint
    select_transcripts = 'refseq'
    transcript_model = 'NM_000093.4'
    genome_build = 'GRCh37'
    content_type = 'application/json'  # or 'text/xml'

    # Construct the URL
    url = f"/transcript-mapper/HGVS/{select_transcripts}/{transcript_model}/{genome_build}?content-type={content_type}"

    # Make a GET request
    response = client.get(url)

    # Assert the status code and response data structure
    assert response.status_code == 200
    assert 'application/json' in response.content_type
    data = response.get_json()
    # Check if the response data is as expected
    expected = [{'current_name': 'collagen type I alpha 1 chain', 'current_symbol': 'COL1A1', 'hgnc': 'HGNC:2197',
                 'previous_symbol': '', 'requested_symbol': 'COL1A1', 'transcripts': []}]
    assert data == expected


def test_LOVD_endpoint(client):
    # Example test for the "/<variant_description>/<select_transcripts>/<transcript_model>/<checkonly>/<genome_build
    # >/<liftover>" endpoint
    variant_description = "NC_000017.10%3Ag.48275363C%3EA"
    select_transcripts = 'NM_000093.4%7CNM_001278074.1%7CNM_000093.3'
    transcript_model = 'all'
    checkonly = False
    genome_build = 'GRCh38'
    liftover = False
    content_type = 'application/json'  # or 'text/xml'

    # Construct the URL
    url = f"/transcript-mapper/LOVD/{variant_description}/{transcript_model}/{liftover}/{genome_build}/{checkonly}/{select_transcripts}?content-type={content_type}"

    # Make a GET request
    response = client.get(url)

    # Assert the status code and response data structure
    assert response.status_code == 200
    assert 'application/json' in response.content_type
    data = response.get_json()
    # Check if the response data is as expected
    assert "MANE output" in data



def test_extraAnnotation_endpoint(client):
    # Example test for the "/<genomic_transcript>/<select_extraannotaion>" endpoint
    genomic_transcript = '9:g.22125504G>C'
    select_extraannotaion = 'vep'
    content_type = 'application/json'  # or 'text/xml'

    # Construct the URL
    url = f"/transcript-mapper/extraAnnotation/{genomic_transcript}/{select_extraannotaion}?content-type={content_type}"

    # Make a GET request
    response = client.get(url)

    # Assert the status code and response data structure
    assert response.status_code == 200
    assert 'application/json' in response.content_type
    data = response.get_json()
    # Check if the response data is as expected
    assert "VEP_annotations", "SPDI_annotations" in data
def test_extraAnnotation_endpoint(client):
    # Example test for the "/<genomic_transcript>/<select_extraannotaion>" endpoint
    genomic_transcript = 'ENST00000366667:c.803C>T'
    select_extraannotaion = 'spdi'
    content_type = 'application/json'  # or 'text/xml'

    # Construct the URL
    url = f"/transcript-mapper/extraAnnotation/{genomic_transcript}/{select_extraannotaion}?content-type={content_type}"

    # Make a GET request
    response = client.get(url)

    # Assert the status code and response data structure
    assert response.status_code == 200
    assert 'application/json' in response.content_type
    data = response.get_json()
    # Check if the response data is as expected
    assert "VEP_annotations", "SPDI_annotations" in data
