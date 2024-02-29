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
    else:
        print("Data retrieval successful!")


# Example usage
genomic_transcript = "9:g.22125504G>C"


# The variant NM_000138.5:c.356G>A was extensively studied in Unit 1: Introduction to Clinical Bioinformatics and Genomics
# The variant interpretation report produced was based on Ensembl VEP annotations and other relevant sources
