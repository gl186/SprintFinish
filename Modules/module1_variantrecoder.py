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
    print("response", response)
    return {"Genomic-HGVS": response.json()}


ensemblTranscript = "ENST00000366667:c.803C>T"  # Replace with your ensemblTranscript transcript ID
response = ensemblMapper(ensemblTranscript)

print(f"Genomic HGVS: {response}")
