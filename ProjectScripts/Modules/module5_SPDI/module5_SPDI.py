
# Import modules
from flask import Flask, make_response
from flask_restx import Api, Resource, fields, reqparse
import requests

# Define the application as a Flask app with the name defined by __name__
app = Flask(__name__)

# Define the Api as api
api = Api(app, title="Converting HGVS into module5_SPDI", description="Retrieve variant data from module5_SPDI via HGVS")

# Request parser to identify specific content-type requests
parser = reqparse.RequestParser()
#parser.add_argument('content-type', type=str, help='Accepted\napplication/json')

# Define a namespace for variant data
va_space = api.namespace('module5_SPDI', description='module5_SPDI API Endpoints')


@va_space.route(
    "/hgvs/<string:hgvs>")
#"/hgvs/<string:hgvs>/<string:contextuals>") removed contextuals as essential required input
class VariantAnnotations(Resource):

    @api.doc(params={"hgvs": "HGVS format e.g NC_000017.10:g.48275363C>A",
                     "contextuals": "assembly"}, parser=parser)


    def get(self, hgvs, contextuals):
        """Retrieve varant data from the Leiden Open Variation Database (LOVD) using the VariantValidator API"""
        base_url = "https://api.ncbi.nlm.nih.gov/variation/v0/hgvs"
        #base_url = "https://api.ncbi.nlm.nih.gov/variation/v0/hgvs/NC_000001.10%3Ag.12345T%3EA/contextuals" from NLM website
        ext_get_transcripts = f"/{hgvs}/{'assembly' if assembly else 'raw'}"

        try:
            url = base_url + ext_get_transcripts
            response = requests.get(url, headers={'Content-Type': 'application/json'})
            response_json = response.json()
            return response_json, 200

        except requests.RequestException as e:
            return {"error": f"Error fetching module5_SPDI variant data: {e}"}, 500


if __name__ == "__main__":
    app.run(debug=True)