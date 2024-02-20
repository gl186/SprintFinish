"""
Simple python script using HGVS genomic output from module1 or 2 for Variant Validator with LOVD endpoints
"""

# Import modules
import requests
import json
import module1_variantrecoder
import module2_variantvalidator

# Call Module 1 or 2 dependent on input being Ensembl transcript (starting ENST) or RefSeq (starting NM_)
#if "NM_" in input:
#    if transcript_id.startswith("NM_"):
#        genomic_hgvs = module2_variantvalidator(result)
#    elif transcript_id.startswith("ENST"):
#        genomic_hgvs = module1_variantrecoder.??
#    return genomic_hgvs

def get(genome_build, variant_description, select_transcripts):
    """Retrieve variant data from the Leiden Open Variation Database (LOVD) using the VariantValidator API"""
    base_url = "https://rest.variantvalidator.org/LOVD/lovd/"
    ext_get_transcripts = f"{genome_build}/{variant_description}/all/{'mane_select' if select_transcripts else 'raw'}/False/False"

    try:
        url = base_url + ext_get_transcripts
        response = requests.get(url, headers={'Content-Type': 'application/json'})

        response_dict = response.json() # returns python dict
        # Print the entire response in JSON format
        # print(json.dumps(response_json, indent=2))

    except requests.RequestException as e:
        print(f"Error fetching LOVD variant data: {e}")

#   return python dict from response_json than can be used/printed/filtered by main.py
    return response_dict

# Example usage
# variant_description = module2_variantvalidator.test_return_hgvs()
# genome_build = "hg19"
# select_transcripts = False
# dict_possible_variants = get(genome_build,variant_description,select_transcripts)
