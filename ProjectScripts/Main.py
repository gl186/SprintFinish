#import flask framework and the request module which handles attp request
from flask import Flask, request
from flask_restx import Api, Resource
import requests

#create flaska pplication instance and the flask rest x api extension to support api building
application = Flask(__name__)
api = Api(application)

#define namespace for ensembl transcript api endpoint
ensembleTranscriptNameSpace = api.namespace('ensemble-transcript', description='Return a genomic HGVS transcript')

@ensembleTranscriptNameSpace.route("/<string:ensembleTranscript>")
class EnsembleTranscript(Resource):
    def get(self, ensembleTranscript):
        return {"genome": ensembleTranscript}

#define namespace for redseq transcript api endpoint
rst_space = api.namespace('RefSeq Release Version 222', description='Return a genomic HGVS transcript and genome coordinate')

@rst_space.route("/variantvalidator/<string:genome_build>/<string:variant_description>/<string:select_transcripts>")
class RefSeqTranscript(Resource):
    def get(self, genome_build, variant_description, select_transcripts):
        url = f"https://rest.variantvalidator.org/variantvalidator/{genome_build}/{variant_description}/{select_transcripts}"
        validation = requests.get(url)
        content = validation.json()
        return content

#define namespace for LOVD api endpoint
va_space = api.namespace('LOVD', description='LOVD API Endpoints')

#define class to handle http get request to retriueve variant data and annotations using VEP
@va_space.route("/lovd/<string:genome_build>/<string:variant_description>/<string:select_transcripts>/<string:checkonly>")
class VariantAnnotations(Resource):
    def get(self, genome_build, variant_description, select_transcripts, checkonly):
        base_url = "https://rest.variantvalidator.org/LOVD/lovd/"
        ext_get_transcripts = f"{genome_build}/{variant_description}/all/{'mane_select' if select_transcripts else 'raw'}/True/True{checkonly}"
        url = base_url + ext_get_transcripts
#error handling to catch exceptions during http requests
        try:
            response = requests.get(url, headers={'Content-Type': 'application/json'})
            response_json = response.json()
            return response_json, 200
        except requests.RequestException as e:
            return {"error": f"Error fetching LOVD variant data: {e}"}, 500

vep_space = api.namespace('VEP', description='VEP API Endpoints')

@vep_space.route("/VEP/<string:genome_build>/<string:variant_description>/<string:select_transcripts>")
class VariantVEPResource(Resource):
    def get(self, genome_build, variant_description, select_transcripts):
        base_url = "http://rest.variantvalidator.org"
        endpoint = f"/VariantValidator/variantvalidator/{genome_build}/{variant_description}/{select_transcripts}"
        url = f"{base_url}{endpoint}"
#error handling to catch exceptios during http requests
        try:
            response = requests.get(url)
            response_data = response.json()
            return response_data, 200
        except requests.RequestException as e:
            return {"error": f"Error fetching variant data: {e}"}, 500

#ensures flask application is run if the script is executed directly not when imported as module so allowed automatic reloading on code changed and displatys detailed error message in browser
if __name__ == "__main__":
    application.run(debug=True)