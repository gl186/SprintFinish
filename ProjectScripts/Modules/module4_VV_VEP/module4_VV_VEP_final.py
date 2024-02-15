"""
A simple REST interface for retrieving variant annotations from the Ensembl VEP REST API for an HGVS variant.
This interface is implemented using Flask, Flask-RestX, and Swagger UI.
"""

# Import modules
from flask import Flask, jsonify
from flask_restx import Api, Resource
import requests

#  Define the application as a Flask app with the name defined by __name__
app = Flask(__name__)

# # Define the Api as api
api = Api(app, title="VEP Annotations API", description="Retrieve VEP annotations for HGVS variants")

# Define a namespace
VEP_ns = api.namespace("VEP", description="VEP Annotations")

# The example of HGVS variant i.e. NM_000138.5:c.356G>A was extensively studied in Unit 1 - Introduction to Clinical Genomics
# The variant interpretation report was formulated based on the variant annotations from Ensembl VEP and other relevant sources

# Define the VEP Annotations Endpoints
def get_vep_annotations(hgvs_variant, assembly="GRCh37"):
    # Define the VEP API endpoint for the specified assembly
    if assembly == "GRCh37":
        vep_url = "https://grch37.rest.ensembl.org/vep/human/hgvs/NM_000138.5:c.356G>A"
    elif assembly == "GRCh38":
        vep_url = "https://rest.ensembl.org/vep/human/hgvs/NM_000138.5:c.356G>A"

    # Set the headers for the request
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    # Prepare the payload with the HGVS variant
    payload = {
        "hgvs_notations": [hgvs_variant],
        "assembly_name": assembly,
    }

    try:
        # Make the GET request to the VEP API
        response = requests.get(vep_url, headers=headers, params=payload)

        # Check if the request was successful
        if response.status_code == 200:
            vep_data = response.json()
            return vep_data
        else:
            return {"error": f"Unable to retrieve VEP annotations. Status code: {response.status_code}"}
    except Exception as e:
        return {"error": f"{str(e)}"}

@VEP_ns.route("/annotations/<string:hgvs_variant>/<string:assembly>")
class VEPAnnotations(Resource):

    # Add decorators
    @api.doc(params={"hgvs_variant": "HGVS variant (e.g., NM_000138.5:c.356G>A)", "assembly": "Assembly (GRCh37 or GRCh38)"})

    def get(self, hgvs_variant, assembly):

        # Example usage for the specified assembly
        vep_annotations = get_vep_annotations(hgvs_variant, assembly=assembly)

        # Return the data in JSON format
        return jsonify({
            "variant": hgvs_variant,
            "assembly": assembly,
            "annotations": vep_annotations,
        })

if __name__ == "__main__":
    app.run(debug=True)

# The example of HGVS variant i.e. NM_000138.5:c.356G>A was extensively studied in Unit 1 - Introduction to Clinical Genomics
# The variant interpretation report was formulated based on the variant annotations from Ensembl VEP and other relevant sources



