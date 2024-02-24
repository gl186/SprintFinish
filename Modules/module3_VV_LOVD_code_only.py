"""
Simple python script using HGVS genomic output from module1 or 2 for Variant Validator with LOVD endpoints
"""

# Import modules
import requests


def get_for_GRCh37(variant_description):
    """Retrieve MANE variant data from the Leiden Open Variation Database (LOVD) using the VariantValidator API for genome build hg19/GRCh37"""
    base_url = "https://rest.variantvalidator.org/LOVD/lovd/"
    ext_get_transcripts = f"GRCh37/{variant_description}/all/mane_select/False/False"

    try:
        url = base_url + ext_get_transcripts
        response = requests.get(url, headers={'Content-Type': 'application/json'})

        response_dict = response.json() # returns python dict
        # Additionally print the entire response in JSON format
        # print(json.dumps(response_dict, indent=2))


    except requests.RequestException as e:
        print(f"Error fetching LOVD variant data: {e}")

#   return python dict from response_json than can be used/printed/filtered by main.py
    return response_dict

def get_for_GRCh38(variant_description):
    """Retrieve MANE variant data from the Leiden Open Variation Database (LOVD) using the VariantValidator API for genome build hg38/GRCh38"""
    base_url = "https://rest.variantvalidator.org/LOVD/lovd/"
    ext_get_transcripts = f"GRCh38/{variant_description}/all/mane_select/False/False"

    try:
        url = base_url + ext_get_transcripts
        response = requests.get(url, headers={'Content-Type': 'application/json'})

        response_dict = response.json() # returns python dict
        # Additionally print the entire response in JSON format
        # print(json.dumps(response_dict, indent=2))


    except requests.RequestException as e:
        print(f"Error fetching LOVD variant data: {e}")

#   return python dict from response_json than can be used/printed/filtered by main.py
    return response_dict

# Example usage
# variant_description = module2_variantvalidator.test_return_hgvs()
# dict_possible_variants_GRCh37 = get_for_GRCh37(variant_description)
# dict_possible_variants_GRCh38 = get_for_GRCh38(variant_description)
#
# return_value = ({"variants_GRCh37": dict_possible_variants_GRCh37, "variants_GRCh38": dict_possible_variants_GRCh38})
# print(return_value)