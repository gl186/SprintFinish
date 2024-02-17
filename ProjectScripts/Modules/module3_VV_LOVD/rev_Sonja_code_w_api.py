"""
Simple rest interface for Variant Validator with LOVD endpoints using Flask Flask-RestX and Swagger UI
"""

# Import modules
from flask import Flask, make_response
from flask_restx import Api, Resource, fields, reqparse
import requests

# Define the application as a Flask app with the name defined by __name__
app = Flask(__name__)

# Define the Api as api
api = Api(app, title="LOVD Variant API", description="Retrieve variant data from LOVD")

# Request parser to identify specific content-type requests
parser = reqparse.RequestParser()
parser.add_argument('content-type', type=str, help='Accepted\napplication/json')

# Define a namespace for variant data
va_space = api.namespace('LOVD', description='LOVD API Endpoints')


@va_space.route(
    "/lovd/<string:genome_build>/<string:variant_description>/<string:select_transcripts>")
class VariantAnnotations(Resource):

    @api.doc(params={"genome_build": "GRCh38, GRCh37, hg38, hg19",
                     "variant_description": "HGVS format e.g NC_000017.10:g.48275363C>A",
                     "select_transcripts": "mane_select"}, parser=parser)

    def get(self, genome_build, variant_description, select_transcripts):
        """Retrieve varant data from the Leiden Open Variation Database (LOVD) using the VariantValidator API"""
        base_url = "https://rest.variantvalidator.org/LOVD/lovd/"
        ext_get_transcripts = f"{genome_build}/{variant_description}/all/{'mane_select' if select_transcripts else 'raw'}/False/False"

        try:
            url = base_url + ext_get_transcripts
            response = requests.get(url, headers={'Content-Type': 'application/json'})
            response_json = response.json()
            return response_json, 200

        except requests.RequestException as e:
            return {"error": f"Error fetching LOVD variant data: {e}"}, 500


if __name__ == "__main__":
    app.run(debug=True)



