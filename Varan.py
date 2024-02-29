# -*- coding: UTF-8 -*-
"""
This module is the central module that will be used to call upon the other modules and logs its usage.
"""
# Import modules that will be called to complete requests from the Main.py API
from flask import Flask, make_response
from flask_restx import Api, Resource, reqparse, fields
from dicttoxml import dicttoxml
import logging

from Modules import Main

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
                    help='Accepts:\n- application/json'
                         '\n- application/xml')


# Support both xml and json response type
@api.representation('text/xml')
def xml(data, code, headers):
    data = dicttoxml(data)
    resp = make_response(data, code, headers)
    resp.headers['Content-Type'] = 'text/xml'
    return resp


@api.representation('application/json')
def json(data, code, headers):
    resp = make_response(data, code, headers)
    resp.headers['Content-Type'] = 'application/json'
    return resp


@VariantAnnotationToolNameSpace.route("HGVS/<string:select_transcripts>/<string:transcript_model>/<string:genome_build>")
@api.param("select_transcripts", "***Return all possible transcripts***\n"
                                 ">select ensembl (with or without version number)\n"
                                 ">select refseq(must have version number)\n"
                                 ">   all (at the latest version for each transcript)\n"
                                 "\n***Accepts:***\n"
                                 ">   - refseq (return data for RefSeq transcript models)\n"
                                 ">   - ensembl (return data for ensembl transcript models)\n"
           )
@api.param("transcript_model", "\n***ensembl example***\n"
                               ">\n   ENST00000366667:c.803C>T\n"
                               "\n***refseq example***\n"
                               ">   NM_000093.4\n NM_001278074.1\n NM_000093.3")
@api.param("genome_build", "***Accepts:***\n"
                           ">   - GRCh37\n"
                           ">   - GRCh38\n"
                           ">   - hg19\n"
                           ">   - hg38")
class VariantAnnotationToolClass(Resource):
    @api.doc(parser=parser)
    def get(self, select_transcripts, transcript_model, genome_build):
        hgvs_genomic = {"results": "Genomic information not found"}
        args = parser.parse_args()
        # Remove all whitespace
        select_transcripts = select_transcripts.replace(" ", "")
        transcript_model = transcript_model.replace(" ", "")
        genome_build = genome_build.replace(" ", "")
        # Call modules/functions from Main module
        # Depends on the selected transcript parameter
        if select_transcripts == "ensembl":
            hgvs_genomic = Main.call_module1_function(transcript_model)
            logger.info("Map ensembl to HGVS transcript")
        if select_transcripts == "refseq":
            hgvs_genomic = Main.module2_variantvalidator.get_genomic_info_from_transcript(transcript_model)
            logger.info("Map refseq to HGVS transcript")

        # Overrides the default response route so that the standard HTML URL can return any specified format
        content = hgvs_genomic
        if args['content-type'] == 'application/json':
            # example: http://127.0.0.1:5000.....bob?content-type=application/json
            return json(content, 200, None)
        # example: http://127.0.0.1:5000.....?content-type=text/xml
        elif args['content-type'] == 'text/xml':
            return xml(content, 200, None)
        else:
            # Return the api default output
            return content


@VariantAnnotationToolNameSpace.route("LOVD/<string:variant_description>/<string:transcript_model>/<string:liftover>/<string:genome_build>/<string:checkonly>/<string:select_transcripts>")
@api.param("variant_description", "***Genomic HGVSg***\n"
                                 ">NC_000001.11:g.230710021G>A\n"
                                 ">NC_000017.10:g.48275363C>A\n"
                                 "\n Notes\n"
                                 "pVCF, multiple comma separated ALTs are supported\n"
                                 "Multiple variants can be submitted, separated by the pipe '|' character\n"
                                 "Recommended maximum is 10 variants per submission\n")


@api.param("transcript_model", "\n***Accepts***\n"
                               ">\n refseq (return data for RefSeq transcript models)\n"
                               ">\n ensembl (return data for ensembl transcript models)\n"
                               ">\n all \n")

@api.param("liftover", "\n***Accepts***\n"
                               ">\n True - (liftover to all genomic loci)\n"
                               ">\n primary - (lift to primary assembly only)\n"
                               ">\n False \n")

@api.param("checkonly", "\n***Accepts***\n"
                               ">\n True (return ONLY the genomic variant descriptions\n"
                               ">\n False\n")

@api.param("genome_build", "***Accepts:***\n"
                           ">   - GRCh37\n"
                           ">   - GRCh38\n"
                           ">   - hg19\n"
                           ">   - hg38")

@api.param("select_transcripts", "\n***Return all possible transcripts***\n"
                               ">\n None or all (all transcripts at the latest versions)"
                                "\nraw (all transcripts all version)"
                                "\nselect (select transcripts)"
                                "\n mane (MANE select transcripts) "
                                "\nmane_select (MANE select and MANE Plus Clinical transcripts)\n"
                               "\n***Single***\n"
                               ">\n NM_000093.4 \n"
                               "\n***Multiple***\n"
                               ">\n NM_000093.4|NM_001278074.1|NM_000093.3 \n")

class GenomicAnnotaterTool(Resource):
    @api.doc(parser=parser)
    def get(self, variant_description, transcript_model, genome_build, liftover, checkonly, select_transcripts):
        args = parser.parse_args()
        genomic_transcript = Main.call_module3_function(variant_description, transcript_model, genome_build, liftover, checkonly, select_transcripts)

        content = genomic_transcript
        if args['content-type'] == 'application/json':
            # example: http://127.0.0.1:5000.....bob?content-type=application/json
            return json(content, 200, None)
        # example: http://127.0.0.1:5000.....?content-type=text/xml
        elif args['content-type'] == 'text/xml':
            return xml(content, 200, None)
        else:
            # Return the api default output
            return content


# Define a namespace rout for both modules 4&5


@VariantAnnotationToolNameSpace.route("VEP/SPDI<string:genomic_transcript>/<string:select_extraannotaion>")
@api.param("select_extraannotaion", enum=["SPDI", "VEP"])
class ExtraAnnotations(Resource):
    @api.doc(parser=parser)
    def get(self, genomic_transcript, select_extraannotaion):
        extra_annotation = None
        args = parser.parse_args()

        select_extraannotaion = select_extraannotaion.lower()
        if select_extraannotaion == "vep":
            extra_annotation = Main.call_module4_function(genomic_transcript, select_extraannotaion)
            logger.info("VEP annotation form")
        if select_extraannotaion == "spdi":
            extra_annotation = Main.call_module5_function(genomic_transcript)
            logger.info("SPDI annotation form")
        # Overrides the default response route so that the standard HTML URL can return any specified format
        if args['content-type'] == 'application/json':
            # example: http://127.0.0.1:5000.....bob?content-type=application/json
            return json(extra_annotation, 200, None)
        # example: http://127.0.0.1:5000.....?content-type=text/xml
        elif args['content-type'] == 'text/xml':
            return xml(extra_annotation, 200, None)
        else:
            # Return the api default output
            return extra_annotation


if __name__ == "__main__":
    application.run(debug=True)
    application.run(host="127.0.0.1", port=5000)  # Specify a host and port for the app
