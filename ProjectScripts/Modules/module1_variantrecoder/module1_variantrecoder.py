"""
Simple rest interface for SprintFinish built using Flask Flask-RESTX and Swagger UI
"""

# Import modules
from flask import Flask
from flask_restx import Api, Resource

# Define the application as a Flask app with the name defined by __name__ (i.e. the name of the current module)
# Most tutorials define application as "app"
application = Flask(__name__)

# Define the API as api
api = Api(app = application)

# Define a name-space to be read Swagger UI which is built in to Flask-RESTX
# The first variable is the path of the namespace the second variable describes the space

# implemented the swagger UI and made the shape of API : Linda

ensembleTranscriptNameSpace = api.namespace('ensemble-transcript',
                           description='Return a genomic HGVS transcript')
@ensembleTranscriptNameSpace.route("/<string:ensembleTranscript>")
class NameClass(Resource):
    def get(self, ensembleTranscript):
        # TODO: Add VariantRecorder mapping, just a placeholder
        return {
            "genome": ensembleTranscript
        }



# The second variable:
# Allows app to be run in debug mode
if __name__ == '__main__':
	application.debug = True # Enable debugging mode
	application.run(host="127.0.0.1", port=5000) # Specify a host and port fot the app

#Testing the rest interface defined above utilising the requests library. This will make HTTP requests to our API engpoints.
import requests

#need flask to be running but already running from lines 6-7 of this script

# Define base URL of the API
BASE_URL = 'http://127.0.0.1:5000'

# Provide example ensembl transcript to test. This can be changed to test different transcripts
ensemble_transcript = 'ENST00000269305'

# Define the endpoint URL
endpoint_url = f'{BASE_URL}/ensemble-transcript/{ensemble_transcript}'

# Send GET request to the endpoint
response = requests.get(endpoint_url)

# Print the response status code and content
print('Response Status Code:', response.status_code)
print('Response Content:', response.json())
