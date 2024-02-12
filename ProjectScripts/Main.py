# This is the main py script from SprintFinish group
# Press Shift+F10 to execute it

#import necessary modules, flask imported to create the web application
#api and resource from flask_restx are imported to define the restful api endpoints
#requests is imported to sent http requests for testing the api
from flask import Flask
from flask_restx import Api, Resource
import requests

# Define the Flask application
application = Flask(__name__)
api = Api(application)

# Define the namespace for Ensemble Transcript
ensembleTranscriptNameSpace = api.namespace('ensemble-transcript',
                                           description='Return a genomic HGVS transcript')

@ensembleTranscriptNameSpace.route("/<string:ensembleTranscript>")
class NameClass(Resource):
    def get(self, ensembleTranscript):
        # Placeholder response
        return {
            "genome": ensembleTranscript
        }

# Define the namespace for RefSeqTranscript - Georgia and Christoph
rst_space = api.namespace('RefSeqTranscript', description='Return a genomic HGVS transcript and genome coordinate')

@rst_space.route("/variantvalidator/<string:genome_build>/<string:variant_description>/<string:select_transcripts>")
class RefSeqTranscriptClass(Resource):
    def get(self, genome_build, variant_description, select_transcripts):
        # Make a request to the current variantvalidator rest-api
        url = f'https://rest.variantvalidator.org/variantvalidator/{genome_build}/{variant_description}/{select_transcripts}'
        validation = requests.get(url)
        content = validation.json()
        return content

# Allow app to be run in debug mode
if __name__ == '__main__':
    application.debug = True
    application.run(host="127.0.0.1", port=5000)

# Test Ensemble Transcript API - Georgia
BASE_URL = 'http://127.0.0.1:5000'
ensemble_transcript = 'ENST00000269305'
ensemble_transcript_endpoint = f'{BASE_URL}/ensemble-transcript/{ensemble_transcript}'
ensemble_transcript_response = requests.get(ensemble_transcript_endpoint)
print("Ensemble Transcript API Response Content:")
print(ensemble_transcript_response.content.decode('utf-8'))
if ensemble_transcript_response.status_code == 200:
    print("Ensemble Transcript API Request successful!")
else:
    print("Ensemble Transcript API Request failed with status code:", ensemble_transcript_response.status_code)

# Test RefSeqTranscript API - Georgia
genome_build = 'GRCh38'
variant_description = 'NM_001123.3:c.345G>T'
select_transcripts = 'NM_001123.3'
refseq_transcript_endpoint = f'{BASE_URL}/RefSeqTranscript/variantvalidator/{genome_build}/{variant_description}/{select_transcripts}'
refseq_transcript_response = requests.get(refseq_transcript_endpoint)
print("\nRefSeqTranscript API Response Content:")
print(refseq_transcript_response.content.decode('utf-8'))
if refseq_transcript_response.status_code == 200:
    print("RefSeqTranscript API Request successful!")
else:
    print("RefSeqTranscript API Request failed with status code:", refseq_transcript_response.status_code)


#Merged Module 3 Variant Variant Validator into Main.py - Christoph and Georgia
# Import modules
from flask import Flask, make_response
from flask_restx import Api, Resource, fields, reqparse
import requests

# Define the application as a Flask app with the name defined by __name__
app = Flask(__name__)

# Define the Api as api
api = Api(app, title="LOVD Variant API", description="Retrieve variant data from LOVD")

# Request parser to identify specific content-type requests
parser = reqparse.RequestParser()
parser.add_argument('content-type', type=str, help='Accepted\n-application/json')

# Define a namespace for variant data
va_space = api.namespace('LOVD', description='LOVD API Endpoints')


@va_space.route(
    "/lovd/<string:genome_build>/<string:variant_description>/<string:select_transcripts>/<string:checkonly>")
class VariantAnnotations(Resource):

    # Add documentation about the parser
    @api.doc(params={"genome_build": "GRCh38, GRCh37, hg38, hg19",
                     "variant_description": "HGVS format e.g NC_000017.10:g.48275363C>A",
                     "select_transcripts": "mane_select",
                     "checkonly": "True"}, parser=parser)
    # Retrieves variant data from the Leiden Open Variation Database (LOVD) using the VariantValidator API.
    def get(self, genome_build, variant_description, select_transcripts, checkonly):
        base_url = "https://rest.variantvalidator.org/LOVD/lovd/"
        ext_get_transcripts = f"{genome_build}/{variant_description}/all/{'mane_select' if select_transcripts else 'raw'}/True/True{checkonly}"

        try:
            url = base_url + ext_get_transcripts
            response = requests.get(url, headers={'Content-Type': 'application/json'})
            response_json = response.json()
            return response_json, 200

        except requests.RequestException as e:
            return {"error": f"Error fetching LOVD variant data: {e}"}, 500


if __name__ == "__main__":
    app.run(debug=True)


#Added VEP Module 4 support - Christoph
# Import modules
from flask import Flask
from flask_restx import Api, Resource, reqparse
import requests

# Define the application as a Flask app with the name defined by __name__
app = Flask(__name__)

# Define the Api as api
api = Api(app, version='1.0', title='Variant Validator_VEP API',
          description='Retrieve variant data and Ensembl VEP annotations')

# Request parser to identify specific content-type requests
parser = reqparse.RequestParser()
parser.add_argument('content-type', type=str, help='Accepted\n-application/json')

# Define a namespace for VEP variant data
vep_space = api.namespace('VEP', description='VEP API Endpoints')


@vep_space.route("/VEP/<string:genome_build>/<string:variant_description>/<string:select_transcripts>")
class VariantVEPResource(Resource):

    # Add documentation about the parser

    @api.doc(params={"genome_build": "GRCh38, GRCh37, hg38, hg19",
                     "variant_description": "HGVS format NM_001005484.2:c.274G>A", "select_transcripts": "mane_select"
                     }, parser=parser)
    def get(self, genome_build, variant_description, select_transcripts):
        base_url = "http://rest.variantvalidator.org"
        endpoint = "/VariantValidator/variantvalidator/{genome_build}/{variant_description}/{select_transcripts}"

        url = f"{base_url}{endpoint}".format(
            genome_build=genome_build,
            variant_description=variant_description,
            select_transcripts=select_transcripts
        )
        try:
            # Lets retrieve variant data from Variant Validator REST API
            response = requests.get(url)
            response_data = response.json()
            return response_data, 200

            # Then we retrieve VEP data from Ensembl REST API
            vep_url = "https://rest.ensembl.org/vep/human/hgvs/{variant_description}?content_type=application/json"
            vep_response = requests.get(vep_url.format(variant_description=variant_description))
            vep_data = vep_response.json()
            return vep_data, 200

        except requests.RequestException as e:
            print(f"Error fetching variant data: {e}")


if __name__ == "__main__":
    app.run(debug=True)
    app.run(host="127.0.0.1", port=5000)  # Specify a host and port for the app