"""
A simple REST interface for retrieving genomic HGVS and genomic coordinates from Variant Validator from a RefSeq transcript ID.
Lisa
"""
#import modules
import requests
import json

def get_genomic_info_from_transcript(transcript_id):
    api_url = "https://rest.variantvalidator.org/VariantValidator/tools/gene2transcripts_v2/COL1A1/"+ transcript_id +"/refseq/all?content-type=application%2Fjson"
    try:
        response = requests.get(api_url)

        if response.raise_for_status():
            print("Genomic information not found.")
            return {response: "Genomic information not found."}
        else:
            return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None, None


# def test_return_hgvs():
# return "NC_000017.10:g.48275363C>A"
'''
# Example usage
transcript_id = "NM_000088.4"  # Replace with your RefSeq transcript ID
genomic_hgvs, genomic_coordinates = get_genomic_info_from_transcript(transcript_id)

if genomic_hgvs and genomic_coordinates:
    print(f"Genomic HGVS: {genomic_hgvs}")
    print(f"Genomic Coordinates: {genomic_coordinates}")
'''
