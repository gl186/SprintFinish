
"""
"""

# Import modules
from flask import Flask, make_response
from flask_restx import Api, Resource
import requests

# Define the application as a Flask app with the name defined by __name__ (i.e. the name of the current module)
application = Flask(__name__)

# Define the API as api
api = Api(app = application)

# Define a name-space to be read Swagger UI which is built in to Flask-RESTX
# The first variable is the path of the namespace the second variable describes the space

# Note: 'rst' stands for RefSeqTranscript
rst_space = api.namespace('RefSeqTranscript', description = 'Return a genomic HGVS transcript and genome coordinate')

@rst_space.route("/variantvalidator/<string:genome_build>/<string:variant_description>/<string:select_transcripts>")
class RefSeqTranscriptClass(Resource):
    def get(self, genome_build, variant_description, select_transcripts):

        #Make a request to the current variantvalidator rest-api
        url ='/'.join(["https://rest.variantvalidator.org/variantvalidator,genome_build, variant_description, select_trasncripts"])
        validation = request.get(url)
        content =validation.json()
        return content


# allows app to be run in debug mode
if __name__ == '__main__':
    application.debug = True #enable debugging mode
    application.run(host="127.0.0.1", port=5000) # specify a host and port for the app
