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

# def get_genomic_info_from_transcript(transcript_id):
#     api_url = f"https://rest.variantvalidator.org/VariantValidator/tools/gene2transcripts_v2/COL1A1/{transcript_id}/refseq/all?content-type=application%2Fjson"
#     try:
#         response = requests.get(api_url)
#         response.raise_for_status()  # This will raise an exception for 4XX and 5XX status codes
#         return response.json()
#     except requests.exceptions.HTTPError:
#         print("Genomic information not found.")
#         return {"error": "Genomic information not found."}
#     except requests.exceptions.RequestException as e:
#         print(f"Error: {e}")
#         return {"error": str(e)}

# def get_genomic_info_from_transcript(transcript_id):
#     api_url = "https://rest.variantvalidator.org/VariantValidator/tools/gene2transcripts_v2/COL1A1/"+ transcript_id +"/refseq/all?content-type=application%2Fjson"
#     try:
#         response = requests.get(api_url)
#
#         if response.raise_for_status():
#             print("Genomic information not found.")
#             return {response: "Genomic information not found."}
#         else:
#             return response.json()
#     except requests.exceptions.RequestException as e:
#         print(f"Error: {e}")
#         return None, None



