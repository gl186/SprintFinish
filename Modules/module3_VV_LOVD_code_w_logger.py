"""
Simple rest interface for Variant Validator with LOVD endpoints using Flask Flask-RestX and Swagger UI
"""

# Import modules
import requests
import json
import logging
import logging.handlers as handlers

"""
Logging
"""
# Create logger

logging.basicConfig(filename="/home/ayurahman/SprintFinish/Modules/LOVD_module.log", level=logging.DEBUG)


logger = logging.getLogger('LOVD_module')
# We are setting 2 types of logging. To screen at the level DEBUG
logger.setLevel(logging.INFO)

# We will also log to a file
# Log with a rotating file-handler. This sets the maximum size of the log to 0.5Mb and allows two additional logs
# The logs are then deleted and replaced in rotation
logHandler = handlers.RotatingFileHandler('/home/ayurahman/SprintFinish/Modules/LOVD_module.log', maxBytes=500000, backupCount=2)
# We want to minimise the amount of information we log to capturing bugs
logHandler.setLevel(logging.ERROR)
logger.addHandler(logHandler)

"""
Register custom exceptions
"""
class RemoteConnectionError(Exception):
    code=504

# Retrieve the LOVD data for the HGVS variant
def get_LOVD_annotation(genome_build, variant_description, select_transcripts):
    """Retrieve varant data from the Leiden Open Variation Database (LOVD) using the VariantValidator API"""
    base_url = "https://rest.variantvalidator.org/LOVD/lovd/"
    ext_get_transcripts = f"{genome_build}/{variant_description}/all/{'mane_select' if select_transcripts else 'raw'}/False/False"

    try:
        url = base_url + ext_get_transcripts
        response = requests.get(url, headers={'Content-Type': 'application/json'})
        response_json = response.json()


        # Print the entire response in JSON format
        logger.info("LOVD annotation")
        print("LOVD annotation")
        print(json.dumps(response_json, indent=2))

    except requests.RequestException as e:
        logger.error("error retrieving LOVD annotation")
        print(f"Error fetching LOVD variant data: {e}")
        raise RemoteConnectionError
    else:
        logger.info("LOVD data retrieval successful")
        print("LOVD data retrieval successful")

# Example usage
variant_description = "NC_000017.10:g.48275363C>A"
genome_build = "hg19"
select_transcripts = False
get_LOVD_annotation(genome_build,variant_description,select_transcripts)




