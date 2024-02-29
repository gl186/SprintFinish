"""
A Unit test for module2_variantvalidator.py
"""


import pytest
import requests
import requests_mock
from Modules.module2_variantvalidator import get_genomic_info_from_transcript
def test_get_genomic_info_from_transcript_success():
    transcript_id = "NM_000088.3"
    with requests_mock.Mocker() as m:
        m.get("https://rest.variantvalidator.org/VariantValidator/tools/gene2transcripts_v2/COL1A1/NM_000088.3/refseq/all?content-type=application%2Fjson",
              json={"success": True, "data": "example data"}, status_code=200)

        result = get_genomic_info_from_transcript(transcript_id)
        assert result == {"success": True, "data": "example data"}

def test_get_genomic_info_from_transcript_failure():
    transcript_id = "NM_invalid"
    with requests_mock.Mocker() as m:
        m.get("https://rest.variantvalidator.org/VariantValidator/tools/gene2transcripts_v2/COL1A1/NM_invalid/refseq/all?content-type=application%2Fjson",
              status_code=404)

        result = get_genomic_info_from_transcript(transcript_id)
        assert result == {"response": "Genomic information not found."}

def test_get_genomic_info_from_transcript_exception():
    transcript_id = "NM_exception"
    with requests_mock.Mocker() as m:
        m.get("https://rest.variantvalidator.org/VariantValidator/tools/gene2transcripts_v2/COL1A1/NM_exception/refseq/all?content-type=application%2Fjson",
              exc=requests.exceptions.ConnectTimeout)

        result = get_genomic_info_from_transcript(transcript_id)
        assert result is None



