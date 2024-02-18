"""
A function maps the ensemble transcript to HGVS annotation using the variant recorder API
"""
# Import modules
import requests
from flask import make_response, jsonify


def ensembleMapper(ensembleTranscript):
    # Make a request to the current VariantRecorder rest-API
    url = "https://rest.ensembl.org"
    path = "/variant_recoder/human/" + ensembleTranscript

    response = requests.get(url + path, headers={"Content-Type": "application/json"})
    return make_response(jsonify({"Genomic-HGVS": response.json()}), 200)

