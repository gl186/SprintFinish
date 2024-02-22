"""
Get SPDI using Variant Recorder
"""
# Import modules
import requests
import json

def get_SPDI(hgvs):
    server = "https://rest.ensembl.org/"
    ext = f"/variant_recoder/human/{hgvs}?fields=spdi"

    try:
        r = requests.get(server + ext, headers={"Content-Type": "application/json"})
        r.raise_for_status()  # Raise an exception if the response status is not OK
        decoded = r.json()
        return decoded
    except requests.RequestException as e:
        print(f"An error occurred: {e}")


# Example usage:
variant_hgvs = "NM_000138.5:c.356G>A"
result = get_SPDI(variant_hgvs)
print("Get SPDI:")
print(json.dumps(result, indent=2))  # Print the decoded data as a Python dictionary
