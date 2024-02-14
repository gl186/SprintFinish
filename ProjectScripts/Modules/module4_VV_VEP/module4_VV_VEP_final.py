"""
Simple rest interface for Variant Validator with Ensemble endpoints using Flask Flask-RestX and Swagger UI
"""

# Import modules
from flask import Flask
from flask_restx import Api, Resource, reqparse
import requests

# Define the application as a Flask app with the name defined by __name__
app = Flask(__name__)

# Define the Api as api
api = Api(app, version='1.0', title='Variant Validator_VEP API',
          description='Retrieve variant data and Ensembl VEP annotations')

# Request parser to identify specific content-type requests
parser = reqparse.RequestParser()
parser.add_argument('content-type', type=str, help='Accepted\n-application/json')

# Define a namespace for VEP variant data
vep_space = api.namespace('VEP', description='VEP API Endpoints')


@vep_space.route("/VEP/<string:genome_build>/<string:variant_description>/<string:select_transcripts>")
class VariantVEPResource(Resource):

    # Add documentation about the parser

    @api.doc(params={"genome_build": "GRCh38, GRCh37, hg38, hg19",
                     "variant_description": "HGVS format NM_001005484.2:c.274G>A", "select_transcripts": "mane_select"
                     }, parser=parser)
    def get(self, genome_build, variant_description, select_transcripts):
        base_url = "http://rest.variantvalidator.org"
        endpoint = "/VariantValidator/variantvalidator/{genome_build}/{variant_description}/{select_transcripts}"

        url = f"{base_url}{endpoint}".format(
            genome_build=genome_build,
            variant_description=variant_description,
            select_transcripts=select_transcripts
        )
        try:
            # Lets retrieve variant data from Variant Validator REST API
            response = requests.get(url)
            response_data = response.json()
            return response_data, 200

            # Then we retrieve VEP data from Ensembl REST API
            vep_url = "https://rest.ensembl.org/vep/human/hgvs/{variant_description}?content_type=application/json"
            vep_response = requests.get(vep_url.format(variant_description=variant_description))
            vep_data = vep_response.json()
            return vep_data, 200

        except requests.RequestException as e:
            print(f"Error fetching variant data: {e}")


if __name__ == "__main__":
    app.run(debug=True)
    app.run(host="127.0.0.1", port=5000)  # Specify a host and port fot the app
