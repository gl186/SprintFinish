"""
Get SPDI format for HGVS genomic data
"""
# Import modules
import requests
import json


def get(hgvs):
    """Retrieve SPDI format for HGVS genomic data using the NCBI Variation Services API"""
    base_url = "https://api.ncbi.nlm.nih.gov/variation/v0/hgvs"
    ext_get_transcripts = f"/{hgvs}/contextuals"

    try:
        url = base_url + ext_get_transcripts
        response = requests.get(url, headers={'Content-Type': 'application/json'})
        response_dict = response.json()
        print(json.dumps(response_dict, indent=2))
        return response_dict, 200

    except requests.RequestException as e:
        return {"error": f"Error fetching module5_SPDI variant data: {e}"}, 500

# example usage with test hgvs
# get('NC_000017.10:g.48275363C>A')
