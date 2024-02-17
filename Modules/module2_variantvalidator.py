"""
A simple REST interface for retrieving variant validator information from the Variant Validator REST API for an RefSeq transcript.
This interface is implemented using Flask, Flask-RestX, and Swagger UI.
"""

# Import modules
from flask import Flask, make_response
from flask_restx import Api, Resource
import requests

# Define the application as a Flask app with the name defined by __name__ (i.e. the name of the current module)
application = Flask(__name__)

# Define the API as api
api = Api(app=application)

# Define a name-space to be read Swagger UI which is built into Flask-RESTX
# The first variable is the path of the namespace, and the second variable describes the space

# Note: 'rst' stands for RefSeqTranscript
rst_space = api.namespace('RefSeqTranscript', description='Return a genomic HGVS transcript and genome coordinate')

@rst_space.route("/variantvalidator/<string:genome_build>/<string:variant_description>/<string:select_transcripts>")
class RefSeqTranscriptClass(Resource):
    def get(self, genome_build, variant_description, select_transcripts):

        # Make a request to the current variantvalidator rest-api
        url = '/'.join(["https://rest.variantvalidator.org/variantvalidator", genome_build, variant_description, select_transcripts])
        validation = requests.get(url)
        content = validation.json()
        return content

# Allows the app to be run in debug mode
if __name__ == '__main__':
    application.debug = True  # enable debugging mode
    application.run()
