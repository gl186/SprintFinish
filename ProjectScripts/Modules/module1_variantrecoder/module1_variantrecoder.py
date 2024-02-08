"""
Simple rest interface for SprintFinish built using Flask Flask-RESTX and Swagger UI
"""
# Import modules
from flask import Flask, make_response
import requests
from flask_restx import Api, Resource, reqparse

# Define the application as a Flask app with the name defined by __name__ (i.e. the name of the current module)
# Most tutorials define application as "app"
application = Flask(__name__)

# Define the API as api
api = Api(app=application)


# Define a name-space to be read Swagger UI which is built in to Flask-RESTX
# The first variable is the path of the namespace the second variable describes the space

# implemented the swagger UI and made the shape of API : Linda

ensembleTranscriptNameSpace = api.namespace('ensemble-transcript',
                                            description='Return a genomic HGVS transcript')

# Create a RequestParser object to identify specific content-type requests in HTTP URLs
# The requestparser allows us to specify arguements passed via a URL, in this case, ....?content-type=application/json
parser = reqparse.RequestParser()
parser.add_argument('content-type',
                    type=str,
                    help='Accepted:\n- application/json')
@api.representation('application/json')
def json(data, code, headers):
    resp = make_response(data, code)
    resp.headers['Content-Type'] = 'application/json'
    return resp





@ensembleTranscriptNameSpace.route("/<string:ensembleTranscript>")
class NameClass(Resource):
    @api.doc(parser=parser)
    def get(self, ensembleTranscript):
        # Make a request to the curent VariantRecorder rest-API
        server = "https://rest.ensembl.org"
        ext = "/variant_recoder/human/" + ensembleTranscript

        response = requests.get(server + ext, headers={"Content-Type": "application/json"})
        return json({
            "Genomic-HGVS": response.json()
        }, 200, None)

# The second variable:
# Allows app to be run in debug mode
if __name__ == '__main__':
    application.debug = True  # Enable debugging mode
    application.run(host="127.0.0.1", port=5000)  # Specify a host and port fot the app