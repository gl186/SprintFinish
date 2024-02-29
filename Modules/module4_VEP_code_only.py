"""
Simple code that input genomic annotation and retrieve data from SPDI annotater API
"""
import requests
import sys
import json


def get_variant_annotation(select_extraannotaion, genomic_transcript):
    base_url = "https://rest.ensembl.org"
    ext = f"/{genomic_transcript}/human/hgvs/{select_extraannotaion}"

    try:
        # Define the Ensembl VEP REST API endpoints

        url = base_url + ext

        r = requests.get(url, headers={"Content-Type": "application/json"})

        if not r.ok:
            r.raise_for_status()
            sys.exit()

        decoded = r.json()
        print(repr(decoded))
        return decoded

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")



# Example usage
# genomic_transcript = "9:g.22125504G>C"

