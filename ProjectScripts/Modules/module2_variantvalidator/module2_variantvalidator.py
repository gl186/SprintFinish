# Define a name-space to be read Swagger UI which is built in to Flask-RESTX
# The first variable is the path of the namespace the second variable describes the space

#import necessary modules, flask imported to create the web application
#api and resource from flask_restx are imported to define the restful api endpoints
#requests is imported to sent http requests for testing the api
from flask import Flask
from flask_restx import Api, Resource
import requests

# Define the Flask application
application = Flask(__name__)
api = Api(application)

# Note: 'rst' stands for RefSeqTranscript
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

#test module 2 code API
#requests module already imported

base_url = 'http://127.0.0.1:5000'

#define sample parameters
genome_build = 'GRCh38'
variant_description = 'NM_001123.3:c.345G>T'
select_transcripts = 'NM+001123.3'

#define the end point URL
endpoint_url = f'{http://127.0.0.1:5000}/RefSeqTranscript/variantValidator/{genome_build}/{variant_description}/{select_transcripts}'

#Send GET request to the endpoint
response = requests.get(endpoint_url)

#Print the responses content
print("Response Content:")
print(response.content.decode('utf-8'))

#check the responses status code ie. 200 sucessful
if response.status_code == 200:
    print("Request successful!")
else:
    print("Request failed with status code", response.status_code)

