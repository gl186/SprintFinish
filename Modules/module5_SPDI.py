"""
Get SPDI using Variant Recorder
"""
# Import modules
import requests
import json

def get(self, hgvs, contextuals):
    """Retrieve variant data from the Leiden Open Variation Database (LOVD) using the VariantValidator API"""
    base_url = "https://api.ncbi.nlm.nih.gov/variation/v0/hgvs"
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