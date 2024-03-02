"""
A simple REST interface for retrieving genomic HGVS and genomic coordinates from Variant Validator from a RefSeq transcript ID.
Lisa
"""
#import modules
import requests

def get_genomic_info_from_transcript(transcript_id):
    api_url = "https://rest.variantvalidator.org/VariantValidator/tools/gene2transcripts_v2/COL1A1/"+ transcript_id +"/refseq/all?content-type=application%2Fjson"
    try:
        response = requests.get(api_url)

        if response.status_code != 200:
            print("Genomic information not found.")
            return {"response": "Genomic information not found."}
        else:
            return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None
