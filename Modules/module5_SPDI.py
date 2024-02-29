"""
Translate a variant identifier, HGVS notation or genomic SPDI notation to all possible variant IDs, HGVS and genomic SPDI
"""
# Import modules
import requests
import json
import sys


def get_variant_annotation2(genomic_transcript):
    base_url = "https://rest.ensembl.org"
    ext = f"/variant_recoder/human/{genomic_transcript}?"
    try:
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

# example usage
# genomic_transcript = ('rs56116432', 'ENST00000366667:c.803C>T')
