"""
Simple rest api that input HGVS variant and retrieve data from Ensembl VEP GRCh38 and GRCh37 - Nurhayu
"""
import requests
import json

def get_variant_annotation(hgvs_variant):


    try:
        # Define the Ensembl VEP REST API endpoints for GRCh37 and GRCh38
        vep_url_grch37 = "https://grch37.rest.ensembl.org/vep/human/hgvs/" + hgvs_variant
        vep_url_grch38 = "https://rest.ensembl.org/vep/human/hgvs/" + hgvs_variant

        # Set the headers for the API request
        headers = {"Content-Type": "application/json"}

        # Retrieve annotation data for GRCh37
        response_grch37 = requests.get(vep_url_grch37, headers=headers)
        response_grch37.raise_for_status()
        annotation_grch37 = response_grch37.json()

        # Retrieve annotation data for GRCh38
        response_grch38 = requests.get(vep_url_grch38, headers=headers)
        response_grch38.raise_for_status()
        annotation_grch38 = response_grch38.json()

        # Print the annotation data in JSON format
        print("Annotation data for GRCh37:")
        print(json.dumps(annotation_grch37, indent=2))


        print("\nAnnotation data for GRCh38:")
        print(json.dumps(annotation_grch38, indent=2))

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
    else:
        print("Data retrieval successful!")


# Example usage
hgvs_variant = "NM_000138.5:c.356G>A"
get_variant_annotation(hgvs_variant)

# The variant NM_000138.5:c.356G>A was extensively studied in Unit 1: Introduction to Clinical Bioinformatics and Genomics
# The variant interpretation report produced was based on Ensembl VEP annotations and other relevant sources
