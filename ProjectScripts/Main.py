# This is the main py script from SprintFinish group
# Press Shift+F10 to execute it

#import necessary modules, flask imported to create the web application
#api and resource from flask_restx are imported to define the restful api endpoints
#requests is imported to sent http requests for testing the api
from flask import Flask
from flask_restx import Api, Resource
import requests

# Define the application as a Flask app with the name defined by __name__ (i.e. the name of the current module)
# Most tutorials define application as "app"
application = Flask(__name__)

# Define the API as api ie. create the RESTful API
api = Api(app=application)

# Define a name-space to be read Swagger UI which is built into Flask-RESTX
# The first variable is the path of the namespace and the second variable describes the space

# implemented the Swagger UI and made the shape of API: Linda

ensembleTranscriptNameSpace = api.namespace('ensemble-transcript',
                                           description='Return a genomic HGVS transcript')

#Define the endpoint which is the ensemble transcript associated with name class. Define the get command to handle HTTP get request
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
    application.debug = True  # Enable debugging mode
    application.run(host="127.0.0.1", port=5000)  # Specify a host and port for the app

# Testing the REST interface defined above utilizing the requests library. This will make HTTP requests to our API endpoints. Georgia

# Define base URL of the API
BASE_URL = 'http://127.0.0.1:5000'

# Provide example ensembl transcript to test. This can be changed to test different transcripts
ensemble_transcript = 'ENST00000269305'

# Define the endpoint URL using base URL and an example transcript
endpoint_url = f'{BASE_URL}/ensemble-transcript/{ensemble_transcript}'

# Send GET request to the endpoint
response = requests.get(endpoint_url)

# Print the response status code and content
print('Response Status Code:', response.status_code)
print('Response Content:', response.json())