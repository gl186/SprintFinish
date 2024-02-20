# -*- coding: UTF-8 -*-
"""
This module is the central module that will be used to call upon the other modules and logs its usage.
"""

# Import modules that will be called to complete requests from the Main.py API
from flask import Flask, make_response
from flask_restx import Api, Resource, reqparse
from Modules.module1_variantrecoder import ensembleMapper
import Modules.module2_variantvalidator
import Modules.module5_SPDI
import logging

# Determine logger format and create the file
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(level=logging.DEBUG,
                    format=LOG_FORMAT)
logger = logging.getLogger()

# Define the application as a Flask app with the name defined by __name__ (i.e. the name of the current module)
# Most tutorials define application as "app"
application = Flask(__name__)

# Define the API as api
api = Api(app=application)

# Define a name-space to be read Swagger UI which is built in to Flask-RESTX
# The first variable is the path of the namespace the second variable describes the space

# implemented the swagger UI and made the shape of API : Linda

ensembleTranscriptMapperNameSpace = api.namespace('ensemble-transcript-mapper',
                                                  description='Return a genomic, transcript and protein description')

# Create a RequestParser object to identify specific content-type requests in HTTP URLs
# The request parser allows us to specify arguments passed via a URL, in this case, ....?content-type=application/json
parser = reqparse.RequestParser()
parser.add_argument('content-type',
                    type=str,
                    help='Accepted:\n- application/json')


@api.representation('application/json')
def json(data, code, headers):
    resp = make_response(data, code)
    resp.headers['Content-Type'] = 'application/json'
    return resp


@ensembleTranscriptMapperNameSpace.route("/<string:ensembleTranscript>")
class EnsembleTranscriptMapperClass(Resource):
    @api.doc(parser=parser)
    def get(self, ensembleTranscript):
        # call the module1_variantrecorder.ensembleMapper function
        logger.info("Map ensemble to HGVS transcript")
        genomicHGVS = ensembleMapper(ensembleTranscript)
        # TODO: use module2, then update the returned response
        # TODO: use module3, then update the returned response
        # TODO: use module4, then update the returned response
        # TODO: use module5, then update the returned response
        return genomicHGVS


if __name__ == "__main__":
    application.run(debug=True)
    application.run(host="127.0.0.1", port=5000)  # Specify a host and port for the app
