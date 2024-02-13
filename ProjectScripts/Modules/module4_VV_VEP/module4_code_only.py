import requests
import json

def get_variant_data():
    base_url = "http://rest.variantvalidator.org"
    endpoint = "/VariantValidator/variantvalidator/{genome_build}/{variant_description}/{select_transcripts}"
    genome_build = "GRCh37"  # You can choose GRCh38 or other genome builds
    variant_description = "NM_001005484.2:c.274G>A"  # Example variant description
    select_transcripts = "mane_select"  # You can specify specific transcripts if needed

    url = f"{base_url}{endpoint}".format(
        genome_build=genome_build,
        variant_description=variant_description,
        select_transcripts=select_transcripts
    )

    try:
        response = requests.get(url)
        response_data = response.json()
        print(json.dumps(response_data, indent=4))

        # Now let's retrieve VEP data from Ensembl REST API
        vep_url = "https://rest.ensembl.org/vep/human/hgvs/{variant_description}?content_type=application/json"
        vep_response = requests.get(vep_url.format(variant_description=variant_description))
        vep_data = vep_response.json()
        print(json.dumps(vep_data, indent=4))
    except requests.RequestException as e:
        print(f"Error fetching variant data: {e}")

if __name__ == "__main__":
    get_variant_data()
