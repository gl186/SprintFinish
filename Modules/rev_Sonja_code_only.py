"""
Simple rest interface for Variant Validator with LOVD endpoints using Flask Flask-RestX and Swagger UI
"""

# Import modules
import requests
import json

#
def get(genome_build, variant_description, select_transcripts):
    """Retrieve varant data from the Leiden Open Variation Database (LOVD) using the VariantValidator API"""
    base_url = "https://rest.variantvalidator.org/LOVD/lovd/"
    ext_get_transcripts = f"{genome_build}/{variant_description}/all/{'mane_select' if select_transcripts else 'raw'}/False/False"

    try:
        url = base_url + ext_get_transcripts
        response = requests.get(url, headers={'Content-Type': 'application/json'})
        response_json = response.json()


        # Print the entire response in JSON format
        print(json.dumps(response_json, indent=2))

    except requests.RequestException as e:
        print(f"Error fetching LOVD variant data: {e}")

# Example usage
variant_description = "NC_000017.10:g.48275363C>A"
genome_build = "hg19"
select_transcripts = False
get(genome_build,variant_description,select_transcripts)




