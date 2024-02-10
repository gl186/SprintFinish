from flask import Flask, make_response
from flask_restx import Api, Resource, fields, reqparse
import requests

app = Flask(__name__)
api = Api(app, title="LOVD Variant API", description="Retrieve variant data from LOVD")

# Request parser to identify specific content-type requests
parser = reqparse.RequestParser()
parser.add_argument('content-type',
                    type=str,
                    help='Accepted\n-application/json')


@api.representation('application/json')
def json(data, code, headers):
    resp = make_response(data, code)
    resp.headers['Content-Type'] = 'application/json'
    return resp


# Define a namespace for variant data
va_space = api.namespace('LOVD', description= 'LOVD API Endpoints')

# Model for variant data
variant_model = api.model("Variant", {
    "Variant ID": fields.String,
    "Variant Type": fields.String,
    "mRNA Position": fields.String,
    "Genomic Position": fields.String,
    "Variant DNA": fields.String,
    "Variant DBID": fields.String,
    "Times Reported": fields.Integer,
})

@va_space.route("/lovd/<string:genome_build>/<string:variant_description>/<string:select_trancripts>/<string:checkonly>")
class VariantAnnotations(Resource):
    @api.doc(params={"genome_build": "GRCh38, GRCh37, hg38, hg19", "variant_description": "HGVS format e.g.NM_002225.3:c.157C>T", "select_trancripts":"mane_select",
                                                                         "checkonly":"True"},parser=parser)

    def get(self, genome_build, variant_description, select_trancripts, checkonly):
        """
        Retrieve variant data for a given variant description.
        """

    def retrieve_lovd_variant_data(variant_description):
        """
        Retrieves variant data from the LOVD API.

        Args:
            variant_description (str): The variant description (e.g., "NM_002225.3:c.860").

        Returns:
            dict: Variant information (e.g., variant ID, variant type, mRNA position, genomic position, etc.).
        """
        # LOVD API endpoint for variant validation
        validation_api_url = "https://api.lovd.nl/v1/checkHGVS"
        # LOVD API endpoint for variant data retrieval
        data_api_url = "https://databases.lovd.nl/shared/api/rest.php/variants"
        # LOVD API endpoint for checking if the API is alive
        hello_api_url = "https://api.lovd.nl/v1/hello"

        # Initialize an empty dictionary to store variant information
        variant_info = {}

        # Make a GET request to validate the variant
        validation_response = requests.get(validation_api_url, params={"variant": variant_description})

        if validation_response.status_code == 200:
            validation_data = validation_response.json()
            if "data" in validation_data:
                variant_info["Variant ID"] = validation_data["data"].get("variant_id", "Unknown")
                variant_info["Variant Type"] = validation_data["data"].get("variant_type", "Unknown")
            else:
                variant_info["Error"] = "No variant data found during validation."
        else:
            variant_info["Error"] = f"Error fetching validation data. Status code: {validation_response.status_code}"

        # Make a GET request to retrieve variant data
        data_response = requests.get(data_api_url, params={"variant": variant_description})

        if data_response.status_code == 200:
            data_data = data_response.json()
            if "data" in data_data:
                variant_info["mRNA Position"] = data_data["data"].get("position_mRNA", "Unknown")
                variant_info["Genomic Position"] = data_data["data"].get("position_genomic", "Unknown")
                variant_info["Variant DNA"] = data_data["data"].get("Variant/DNA", "Unknown")
                variant_info["Variant DBID"] = data_data["data"].get("Variant/DBID", "Unknown")
                variant_info["Times Reported"] = data_data["data"].get("Times_reported", "Unknown")
            else:
                variant_info["Error"] = "No variant data found during retrieval."
        else:
            variant_info["Error"] = f"Error fetching data. Status code: {data_response.status_code}"

        # Make a GET request to check if the API is alive
        hello_response = requests.get(hello_api_url)

        if hello_response.status_code == 200:
            hello_data = hello_response.json()
            if "messages" in hello_data:
                variant_info["API Status"] = hello_data["messages"][0]
            else:
                variant_info["API Status"] = "Unknown"
        else:
            variant_info["API Status"] = f"Error checking API status. Status code: {hello_response.status_code}"

        return variant_info

    # Example usage
    variant_description = "NM_002225.3:c.860"
    variant_data = retrieve_lovd_variant_data(variant_description)
    for key, value in variant_data.items():
        print(f"{key}: {value}")

# Allows app to be run in debug mode
if __name__ == '__main__':
    application.debug = True # Enable debugging mode
    application.run(host="127.0.0.1", port=5000) # Specify a host and port fot the app




