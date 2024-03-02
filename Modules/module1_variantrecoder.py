"""
A function maps the ensemble transcript to HGVS annotation using the variant recorder API
"""
# Import modules
import requests


def ensemblMapper(ensemblTranscript):
    # Make a request to the current VariantRecorder rest-API
    url = "https://rest.ensembl.org"
    path = "/variant_recoder/human/" + ensemblTranscript

    response = requests.get(url + path, headers={"Content-Type": "application/json"})
    if response.status_code != 200:
        # Handle non-200 responses without trying to parse JSON
        return {"Genomic-HGVS": []}
    try:
        print("response", response.json())
        return {"Genomic-HGVS": response.json()}
    except requests.exceptions.JSONDecodeError:
        # Handle cases where response is not in JSON format
        return {"Genomic-HGVS": []}


ensemblTranscript = "ENST00000366667:c.803C>T"  # Replace with your ensemblTranscript transcript ID
response = ensemblMapper(ensemblTranscript)

print(f"Genomic HGVS: {response}")
