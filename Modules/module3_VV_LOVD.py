"""
Simple python script using HGVS genomic output from module1 or 2 for Variant Validator with LOVD endpoints
"""

# Import modules
import requests


def get_genomic_transcript(variant_description, transcript_model, genome_build, liftover, checkonly, select_transcripts):
    """Retrieve MANE variant data from the Leiden Open Variation Database (LOVD) using the VariantValidator API for genome build hg19/GRCh37"""
    base_url = "https://rest.variantvalidator.org/LOVD/lovd/"
    ext_get_transcripts = f"{genome_build}/{variant_description}/{transcript_model}/{select_transcripts}/{checkonly}/{liftover}"

    try:
        url = base_url + ext_get_transcripts
        response = requests.get(url, headers={'Content-Type': 'application/json'})

        response_dict = response.json()  # returns python dict
        # Additionally print the entire response in JSON format
        # print(json.dumps(response_dict, indent=2))

        #   return python dict from response_json than can be used/printed/filtered by main.py
        return response_dict

    except requests.RequestException as e:
        print(f"Error fetching LOVD variant data: {e}")