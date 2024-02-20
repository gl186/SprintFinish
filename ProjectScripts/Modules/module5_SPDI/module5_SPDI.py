"""
Get SPDI using Variant Recorder
"""
# Import modules
import requests
import json

# REMOVE Define the application as a Flask app with the name defined by __name__
# REMOVE app = Flask(__name__)

# REMOVE Define the Api as api
# REMOVE api = Api(app, title="Converting HGVS into module5_SPDI", description="Retrieve variant data from module5_SPDI via HGVS")

# REMOVE Request parser to identify specific content-type requests
# REMOVE parser = reqparse.RequestParser()
# REMOVE parser.add_argument('content-type', type=str, help='Accepted\napplication/json')

# REMOVE Define a namespace for variant data
# REMOVE va_space = api.namespace('module5_SPDI', description='module5_SPDI API Endpoints')

# REMOVE #print hello from georgia code if called correctly by main.py remove this if stops running when tested
# REMOVE def debug_import():
# REMOVE   print("Hello from Georgia code")

# REMOVE @va_space.route(
# REMOVE    "/hgvs/<string:hgvs>")
# REMOVE #"/hgvs/<string:hgvs>/<string:contextuals>") removed contextuals as essential required input
# REMOVE class VariantAnnotations(Resource):

# REMOVE    @api.doc(params={"hgvs": "HGVS format e.g NC_000017.10:g.48275363C>A",
# REMOVE                     "contextuals": "assembly"}, parser=parser)


    def get(self, hgvs, contextuals):
        """Retrieve variant data from the Leiden Open Variation Database (LOVD) using the VariantValidator API"""
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


# REMOVE if __name__ == "__main__":
# REMOVE    app.run(debug=True)