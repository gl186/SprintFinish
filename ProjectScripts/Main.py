#code reviewed in team meeting. this code is not to be used. conflict with main branch due to incorrect push/pull reqyest. GL and CT copying code over onto main. 

from flask import Flask, request
from flask_restx import Api, Resource, reqparse
import requests
import logging
import logging.handlers as handlers

# Logging configuration
logger = logging.getLogger('rest_api')
logger.setLevel(logging.INFO)
logHandler = handlers.RotatingFileHandler('rest_api.log', maxBytes=500000, backupCount=2)
logHandler.setLevel(logging.ERROR)
logger.addHandler(logHandler)

# Define the Flask application and API
application = Flask(__name__)
api = Api(application)

# Define the request parser
parser = reqparse.RequestParser()
parser.add_argument('content-type', type=str, help='Accepted:\n- application/json\n- text/xml')

# Define namespaces
ensembleTranscriptNameSpace = api.namespace('ensemble-transcript', description='Return a genomic HGVS transcript')
rst_space = api.namespace('RefSeqTranscript', description='Return a genomic HGVS transcript and genome coordinate')
va_space = api.namespace('LOVD', description='LOVD API Endpoints')
vep_space = api.namespace('VEP', description='VEP API Endpoints')

# Define resource classes
class EnsembleTranscript(Resource):
    def get(self, ensembleTranscript):
        return {"genome": ensembleTranscript}

class RefSeqTranscript(Resource):
    def get(self, genome_build, variant_description, select_transcripts):
        url = f"https://rest.variantvalidator.org/variantvalidator/{genome_build}/{variant_description}/{select_transcripts}"
        try:
            validation = requests.get(url)
            content = validation.json()
            return content
        except requests.RequestException as e:
            logger.error(f"Error fetching RefSeq transcript: {e}")
            return {"error": f"Error fetching RefSeq transcript: {e}"}, 500

class VariantAnnotations(Resource):
    def get(self, genome_build, variant_description, select_transcripts, checkonly):
        base_url = "https://rest.variantvalidator.org/LOVD/lovd/"
        ext_get_transcripts = f"{genome_build}/{variant_description}/all/{'mane_select' if select_transcripts else 'raw'}/True/True{checkonly}"
        url = base_url + ext_get_transcripts
        try:
            response = requests.get(url, headers={'Content-Type': 'application/json'})
            response_json = response.json()
            return response_json, 200
        except requests.RequestException as e:
            logger.error(f"Error fetching LOVD variant data: {e}")
            return {"error": f"Error fetching LOVD variant data: {e}"}, 500

class VariantVEPResource(Resource):
    def get(self, genome_build, variant_description, select_transcripts):
        base_url = "http://rest.variantvalidator.org"
        endpoint = f"/VariantValidator/variantvalidator/{genome_build}/{variant_description}/{select_transcripts}"
        url = f"{base_url}{endpoint}"
        try:
            response = requests.get(url)
            response_data = response.json()
            return response_data, 200
        except requests.RequestException as e:
            logger.error(f"Error fetching variant data: {e}")
            return {"error": f"Error fetching variant data: {e}"}, 500

# Add resources to namespaces
ensembleTranscriptNameSpace.add_resource(EnsembleTranscript, '/<string:ensembleTranscript>')
rst_space.add_resource(RefSeqTranscript, '/<string:genome_build>/<string:variant_description>/<string:select_transcripts>')
va_space.add_resource(VariantAnnotations, '/lovd/<string:genome_build>/<string:variant_description>/<string:select_transcripts>/<string:checkonly>')
vep_space.add_resource(VariantVEPResource, '/VEP/<string:genome_build>/<string:variant_description>/<string:select_transcripts>')

# Run the application
if __name__ == "__main__":
    application.run(debug=True)
