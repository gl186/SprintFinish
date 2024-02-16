# Import modules
from flask import Flask, jsonify
from flask_restx import Api, Resource
import requests

"""
Logging
"""

import logging
import logging.handlers as handlers
import time

# Create logger
logging.basicConfig(filename="/home/ayurahman/SprintFinish/ProjectScripts/Modules/module4_VV_VEP/VEP_rest_api.log", level=logging.DEBUG)


logger = logging.getLogger('VEP_rest_api')
# We are setting 2 types of logging. To screen at the level DEBUG
logger.setLevel(logging.INFO)

# We will also log to a file
# Log with a rotating file-handler. This sets the maximum size of the log to 0.5Mb and allows two additional logs
# The logs are then deleted and replaced in rotation
logHandler = handlers.RotatingFileHandler('VEP_rest_api.log', maxBytes=500000, backupCount=2)
# We want to minimise the amount of information we log to capturing bugs
logHandler.setLevel(logging.ERROR)
logger.addHandler(logHandler)


#  Define the application as a Flask app with the name defined by __name__
app = Flask(__name__)

# # Define the Api as api
api = Api(app, title="VEP Annotations API", description="Retrieve VEP annotations for HGVS variants")

"""
Register custom exceptions
"""
class RemoteConnectionError(Exception):
    code=504

# Define a namespace
VEP_ns = api.namespace("VEP", description="VEP Annotations")

# The example of HGVS variant i.e. NM_000138.5:c.356G>A was extensively studied in Unit 1 - Introduction to Clinical Genomics
# The variant interpretation report was formulated based on the variant annotations from Ensembl VEP and other relevant sources

# Define the VEP Annotations Endpoints
def get_vep_annotations(hgvs_variant, assembly="GRCh37"):
    # Define the VEP API endpoint for the specified assembly
    if assembly == "GRCh37":
        vep_url = "https://grch37.rest.ensembl.org/vep/human/hgvs/NM_000138.5:c.356G>A"
    elif assembly == "GRCh38":
        vep_url = "https://rest.ensembl.org/vep/human/hgvs/NM_000138.5:c.356G>A"

    # Set the headers for the request
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    # Prepare the payload with the HGVS variant
    payload = {
        "hgvs_notations": [hgvs_variant],
        "assembly_name": assembly,
    }

    try:
        # Make the GET request to the VEP API
        response = requests.get(vep_url, headers=headers, params=payload)

        # Check if the request was successful
        if response.status_code == 200:
            vep_data = response.json()
            return vep_data
        else:
            return {"error": f"Unable to retrieve VEP annotations. Status code: {response.status_code}"}
    except Exception as e:
        return {"error": f"{str(e)}"}

@VEP_ns.route("/annotations/<string:hgvs_variant>/<string:assembly>")
class VEPAnnotations(Resource):

    # Add decorators
    @api.doc(params={"hgvs_variant": "HGVS variant (e.g., NM_000138.5:c.356G>A)", "assembly": "Assembly (GRCh37 or GRCh38)"})
    def get(self, hgvs_variant, assembly):

        # Example usage for the specified assembly
        vep_annotations = get_vep_annotations(hgvs_variant, assembly=assembly)

        # Return the data in JSON format
        return jsonify({
            "variant": hgvs_variant,
            "assembly": assembly,
            "annotations": vep_annotations,
        })

"""
Error Handlers
"""
# Simple function that creates an error message that we will log
def log_exception(type):
    # We want to know the arguments passed and the path so we can replicate the error
    params = dict(request.args)
    params['path'] = request.path
    # Create the message and log
    message = '%s occurred at %s with params=%s' % (type, time.ctime(), params)
    logger.exception(message, exc_info=True)

@app.errorhandler(RemoteConnectionError)
def remote_connection_error_handler(e):
    # Add the Exception to the log ensuring that exc_info is True so that a traceback is also logged
    log_exception('RemoteConnectionError')

    # Collect Arguments
    args = parser.parse_args()
    if args['content-type'] != 'text/xml':
        return json({'message': str(e)},
                                504,
                                None)
    else:
        return xml({'message': str(e)},
                   504,
                   None)

@app.errorhandler(404)
def not_found_error_handler(e):
    # Collect Arguments
    args = parser.parse_args()
    if args['content-type'] != 'text/xml':
        return json({'message': 'Requested Endpoint not found'},
                                404,
                                None)
    else:
        return xml({'message': 'Requested Endpoint not found'},
                   404,
                   None)

@app.errorhandler(500)
def default_error_handler(e):
    # Add the Exception to the log ensuring that exc_info is True so that a traceback is also logged
    log_exception('RemoteConnectionError')

    # Collect Arguments
    args = parser.parse_args()
    if args['content-type'] != 'text/xml':
        return json({'message': 'unhandled error: contact https://variantvalidator.org/contact_admin/'},
                                500,
                                None)
    else:
        return xml({'message': 'unhandled error: contact https://variantvalidator.org/contact_admin/'},
                   500,
                   None)


if __name__ == "__main__":
    app.run(debug=True)


