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

# Test RefSeqTranscript API - Georgia and Christoph
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
import requests
import json

base_url = "https://rest.variantvalidator.org/LOVD/lovd/" #Part of the url that never changes plus LOVD endpoint
genome_build = "hg19"
hgvs_genomic_description = "NC_000017.10%3Ag.48275363C%3EA"
select_transcripts = True

# I have modified this part here to make the output print vertically - Nurhayu
ext_get_transcripts = f"{genome_build}/{hgvs_genomic_description}/all/{'mane_select' if select_transcripts else 'raw'}/False/True"

def make_request(base_url, ext_get_transcripts):
    url = base_url + ext_get_transcripts
    print("Querying rest API with URL: " + url)

 # I have added the try block here - Nurhayu
    try:
        response = requests.get(url, headers={'Content-Type': 'application/json'})
        response_json = response.json()  # Corrected this line - Copilot

        # Print the entire response in JSON format
        print(json.dumps(response_json, indent=2))

    except requests.RequestException as e:
        print(f"Error fetching LOVD variant data: {e}")

# Example usage
hgvs_genomic_description = "NC_000017.10%3Ag.48275363C%3EA"
genome_build = "hg19"
select_transcripts = True
make_request(base_url, ext_get_transcripts)