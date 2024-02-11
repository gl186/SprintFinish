import requests
import json

base_url = "https://rest.variantvalidator.org/LOVD/lovd/" #Part of the url that never changes plus LOVD endpoint
genome_build = "hg19"
hgvs_genomic_description = "NC_000017.10%3Ag.48275363C%3EA"
select_transcripts = True

# I have modified this part here to make the output print vertically - Nurhayu
ext_get_transcripts = f"{genome_build}/{hgvs_genomic_description}/all/{'mane_select' if select_transcripts else 'raw'}/False/True"

def make_request(base_url, ext_get_transcripts):
    url = base_url + ext_get_transcripts
    print("Querying rest API with URL: " + url)

 # I have added the try block here - Nurhayu
    try:
        response = requests.get(url, headers={'Content-Type': 'application/json'})
        response_json = response.json()  # Corrected this line - Copilot

        # Print the entire response in JSON format
        print(json.dumps(response_json, indent=2))

    except requests.RequestException as e:
        print(f"Error fetching LOVD variant data: {e}")

# Example usage
hgvs_genomic_description = "NC_000017.10%3Ag.48275363C%3EA"
genome_build = "hg19"
select_transcripts = True
make_request(base_url, ext_get_transcripts)
