"""
A simple REST interface for retrieving variant annotations from the GRCh37 Ensembl VEP REST API for an HGVS variant.
This interface is implemented using Flask, Flask-RestX, and Swagger UI.
"""

#Import modules
from flask import Flask
from flask_restx import Api, Resource, Namespace
import requests

# Define the app as a Flask app with the name defined by __name__
app = Flask(__name__)

# Define the Api as api
api = Api(app, title="Variant Effect Predictor API", description="Retrieve VEP annotations from the GRCh37 Ensembl REST API")

# Create a namespace
VEP_ns = Namespace("VEP", description="Variant Effect Predictor operations")

# Ensembl VEP API endpoint
vep_url = "https://grch37.rest.ensembl.org/vep/human/hgvs/NM_000138.4:c.356G>A"

@VEP_ns.route("/<string:variant_description>")
class VEP(Resource):
    @VEP_ns.doc(params={"variant_description": "HGVS format e.g NM_000138.4:c.356G>A", "assembly":"GRCh37"})
    def get(self, variant_description):
        variant_query = {
            "variant": variant_description,
            "content-type": "application/json",
            "canonical": "yes",
            "assembly": "GRCh37",
        }

        try:
            response = requests.get(vep_url, params=variant_query)
            response_json = response.json()

            # Return the entire JSON response
            return response_json,200

        except requests.RequestException as e:
            return {"error": f"Error fetching VEP data: {e}"}

# Add the namespace to the API
api.add_namespace(VEP_ns)

# Example usage
if __name__ == "__main__":
    variant_to_query = "NM_000138.4:c.356G>A"
    print("Fetching VEP data for variant:", variant_to_query)
    vep_response = VEP().get(variant_to_query)

# Run the Flask app
    app.run(debug=True)

