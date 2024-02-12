import requests
import json

def get_lovd_data(hgvs_variant, genome_build, select_transcripts=True):
    """
    Retrieves variant data from the Leiden Open Variation Database (LOVD) using the VariantValidator API.

    Args:
        hgvs_variant (str): HGVS variant description (e.g., "NC_000017.10:g.48275363C>A").
        genome_build (str): Genome build ("hg19" or "hg38").
        select_transcripts (bool, optional): Whether to select MANE Select transcripts (default is True).

    Returns:
        Prints the retrieved variant data in JSON format.
    """
    base_url = "https://rest.variantvalidator.org/LOVD/lovd/"
    endpoint = f"{genome_build}/{hgvs_variant}/all/{'mane_select' if select_transcripts else 'raw'}/True/True"

    try:
        response = requests.get(base_url + endpoint, headers={"Content-Type": "application/json"})
        response_json = response.json()

        # Print the entire response in JSON format
        print(json.dumps(response_json, indent=2))

    except requests.RequestException as e:
        print(f"Error fetching LOVD variant data: {e}")

# Example usage
hgvs_variant_description = "NC_000017.10:g.48275363C>A"
genome_build = "hg19"
select_transcripts = True
get_lovd_data(hgvs_variant_description, genome_build, select_transcripts)
