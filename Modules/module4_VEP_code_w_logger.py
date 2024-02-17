"""
Simple rest api that input HGVS variant and retrieve data from Ensembl VEP GRCh38 and GRCh37 - Nurhayu
"""
import requests
import json
import logging
import logging.handlers as handlers
import time

"""
Logging
"""
# Create logger

logging.basicConfig(filename="/home/ayurahman/SprintFinish/Modules/VEP_module.log", level=logging.DEBUG)


logger = logging.getLogger('VEP_module')
# We are setting 2 types of logging. To screen at the level DEBUG
logger.setLevel(logging.INFO)

# We will also log to a file
# Log with a rotating file-handler. This sets the maximum size of the log to 0.5Mb and allows two additional logs
# The logs are then deleted and replaced in rotation
logHandler = handlers.RotatingFileHandler('/home/ayurahman/SprintFinish/Modules/VEP_module.log', maxBytes=500000, backupCount=2)
# We want to minimise the amount of information we log to capturing bugs
logHandler.setLevel(logging.ERROR)
logger.addHandler(logHandler)

"""
Register custom exceptions
"""
class RemoteConnectionError(Exception):
    code=504
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
        logger.info("Annotation data for GRCh37:")
        print("Annotation data for GRCh37:")
        print(json.dumps(annotation_grch37, indent=2))

        logger.info("\nAnnotation data for GRCh38:")
        print("\nAnnotation data for GRCh38:")
        print(json.dumps(annotation_grch38, indent=2))

    except requests.RequestException as e:
        logger.error(f"Error fetching data: {e}")
    else:
        logger.info("VEP Data retrieval successful!")
        print("VEP data retrieval successful!")


# Example usage
hgvs_variant = "NM_000138.5:c.356G>A"
get_variant_annotation(hgvs_variant)

# The variant NM_000138.5:c.356G>A was extensively studied in Unit 1: Introduction to Clinical Bioinformatics and Genomics
# The variant interpretation report produced was based on Ensembl VEP annotations and other relevant sources
