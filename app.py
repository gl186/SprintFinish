# -*- coding: UTF-8 -*-
"""
This module is the central module that will be used to call upon the other modules and logs its usage.
"""
from certifi.__main__ import args
# Import modules that will be called to complete requests from the Main.py API
from flask import Flask, make_response
from flask_restx import Api, Resource, reqparse
from Modules.module1_variantrecoder import ensembleMapper
import logging

# Determine logger format and create the file
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(level=logging.DEBUG,
                    format=LOG_FORMAT)
logger = logging.getLogger()

# Define the application as a Flask app with the name defined by __name__ (i.e. the name of the current module)
# Most tutorials define application as "app"
application: Flask = Flask(__name__)

# Define the API as api
api = Api(app=application)

# Define a name-space to be read Swagger UI which is built in to Flask-RESTX
# The first variable is the path of the namespace the second variable describes the space

# implemented the swagger UI and made the shape of API : Linda

VariantAnnotationToolNameSpace = api.namespace('transcript-mapper',
                                               description='Return a genomic, transcript and protein description')

# Create a RequestParser object to identify specific content-type requests in HTTP URLs
# The request parser allows us to specify arguments passed via a URL, in this case, ....?content-type=application/json
parser = reqparse.RequestParser()
parser.add_argument('content-type',
                    type=str,
                    help='Accepted:\n- application/json'
                         '\n- application/xml' )

# TODO: Support xml response type (done.....)


@api.representation('text/xml')
def application_xml(data, code, headers):
    resp = make_response(data, code, headers)
    resp.headers['Content-Type'] = 'text/xml'
    return resp
@api.representation('application/json')
def json(data, code, headers):
    resp = make_response(data, code, headers)
    resp.headers['Content-Type'] = 'application/json'
    return resp


# TODO: add select_transcript as route path (done)
@VariantAnnotationToolNameSpace.route("/<string:transcript_model>")
@api.param("select_transcripts", "***Return all possible transcripts***\n"
                                 ">select ensemble (with or without version number)\n"
                                 ">select refseq(must have version number)\n"
                                 ">   all (at the latest version for each transcript)\n"
          "\n***Accepted:***\n"
          ">   - refseq (return data for RefSeq transcript models)\n"
          ">   - ensembl (return data for ensembl transcript models)\n"
           )
@api.param("transcript_model",   "\n***ensemble example***\n"
                                 ">   ENST00000456328.2|ENST00000496771.5|ENST00000373020|ENSP00000362111\n"
                                 "\n***refseq example***\n"
                                 ">   NM_000093.4|NM_001278074.1|NM_000093.3")
@api.param("genome_build", "***Accepted:***\n"
                           ">   - GRCh37\n"
                           ">   - GRCh38\n"
                           ">   - hg19\n"
                           ">   - hg38")

class VariantAnnotationToolClass(Resource):
    @api.doc(parser=parser)
    def get(self, transcript_model, genome_build, select_transcripts):
        # call the module1_variantrecorder.ensembleMapper function
        # TODO: if..statement based on transcript_model
        # TODO: Also embed the logger within if condition (done)
        if "ENST" in transcript_model:
            hgvs_genomic = variantrecorder(hgvs_transcript, genome_build)
            logger.info("Map ensemble to HGVS transcript")
        if "NM" in transcript_model:
            hgvs_genomic = variantvalidator(hgvs_transcript, genome_build)
            logger.info("Map refseq to HGVS transcript")

        if transcript_model == 'None' or transcript_model == 'none':
            transcript_model = None
        if select_transcripts == 'None' or select_transcripts == 'none':
            select_transcripts = None


        hgvs_transcript = ensembleMapper(ensembletranscript, RefseqTranscript)
        return {"response is ": transcript_model}

        # Overrides the default response route so that the standard HTML URL can return any specified format
        if args['content-type'] == 'application/json':
            # example: http://127.0.0.1:5000.....bob?content-type=application/json
            return representations.application_json(content, 200, None)
        # example: http://127.0.0.1:5000.....?content-type=text/xml
        elif args['content-type'] == 'text/xml':
            return representations.xml(content, 200, None)
        else:
            # Return the api default output
            return content


if __name__ == "__main__":
    application.run(debug=True)
    application.run(host="127.0.0.1", port=5000)  # Specify a host and port for the app
