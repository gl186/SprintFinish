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

# Define the namespace for RefSeqTranscript
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

# Test Ensemble Transcript API
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

# Test RefSeqTranscript API
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


