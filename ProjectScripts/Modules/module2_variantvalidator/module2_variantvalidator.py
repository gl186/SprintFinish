"""
A simple REST interface for retrieving genomic HGVS and genomic coordinates from Variant Validator from a RefSeq transcript ID.
Lisa
"""
#import modules
import requests
import json

def get_genomic_info_from_transcript(transcript_id):
    api_url = "https://rest.variantvalidator.org/VariantValidator/variantvalidator/GRCh38/transcript_id/Return%20all%20possible%20transcripts?content-type=application%2Fjson"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()

        genomic_hgvs = data.get('genomicHgvs')
        genomic_coordinates = data.get('genomicCoordinates')

        if genomic_hgvs and genomic_coordinates:
            return genomic_hgvs, genomic_coordinates
        else:
            print("Genomic information not found.")
            return None, None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None, None


# Example usage
transcript_id = input("Enter RefSeq transcript ID: ")   # Replace with your RefSeq transcript ID
genomic_hgvs, genomic_coordinates = get_genomic_info_from_transcript(transcript_id)

if genomic_hgvs and genomic_coordinates:
    print(f"Genomic HGVS: {genomic_hgvs}")
    print(f"Genomic Coordinates: {genomic_coordinates}")

