import requests
import requests_mock
from Modules.module3_VV_LOVD import get_genomic_transcript


def test_get_genomic_transcript_success():
    with requests_mock.Mocker() as m:
        # Mock URL
        mock_url = 'https://rest.variantvalidator.org/LOVD/lovd/GRCh37/NM_000088.3:c.589G>T/NM_000088.3/refseq/false/hg38'
        # Define the mock response data you want to return
        mock_response_data = {
            'result': 'mocked result data'
        }
        # Setup mock
        m.get(mock_url, json=mock_response_data)

        # Call the function with test data
        response = get_genomic_transcript(
            variant_description='NM_000088.3:c.589G>T',
            transcript_model='NM_000088.3',
            genome_build='GRCh37',
            liftover='hg38',
            checkonly='false',
            select_transcripts='refseq'
        )

        # Verify the response matches the mock data
        assert response == mock_response_data


def test_get_genomic_transcript_failure():
    transcript_id = "NM_invalid"
    with requests_mock.Mocker() as m:
        m.get("https://rest.variantvalidator.org/LOVD/lovd/GRCh37/NM_invalid/NM_000088.3/refseq/false/hg38",
              status_code=404)

        # Call the function with test data
        result = get_genomic_transcript(
            variant_description='NM_invalid',
            transcript_model='NM_000088.3',
            genome_build='GRCh37',
            liftover='hg38',
            checkonly='false',
            select_transcripts='refseq'
        )
        assert result == None


def test_get_genomic_transcript_exception():
    transcript_id = "NM_exception"
    with requests_mock.Mocker() as m:
        m.get("https://rest.variantvalidator.org/LOVD/lovd/GRCh37/NM_exception/NM_000088.3/refseq/false/hg38",
              exc=requests.exceptions.ConnectTimeout)

        # Call the function with test data
        result = get_genomic_transcript(
            variant_description=transcript_id,
            transcript_model='NM_000088.3',
            genome_build='GRCh37',
            liftover='hg38',
            checkonly='false',
            select_transcripts='refseq'
        )
        assert result is None
