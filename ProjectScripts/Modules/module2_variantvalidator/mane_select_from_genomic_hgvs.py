# A simple script that requests mane_select data from the VariantValidator REST API LOVD GET function
#Necessary modules: requests to use the function and json later to work on output in json
import requests,json


base_url = "https://rest.variantvalidator.org/LOVD/lovd/" #Part of the url that never changes plus LOVD endpoint
genome_build = "hg19"
hgvs_genomic_description = "NC_000017.10%3Ag.48275363C%3EA" #ToDo: Avoid problems when others Variants are entered to the URL (C>A)

#url from API: https://rest.variantvalidator.org/LOVD/lovd/hg19/NC_000017.10%3Ag.48275363C%3EA/all/mane_select/False/True?content-type=application%2Fjson
ext_get_transcripts = genome_build + "/" + hgvs_genomic_description + "/" + "all/mane_select/False/True"


#the complete request function:
def make_request(base_url, ext_get_transcripts):
    """GET mane_select output in python dictionary by request containing HGVS genomic transcript descriptions"""
    # Tell the User the full URL of their call to the rest API
    url = base_url + ext_get_transcripts
    print("Querying rest API with URL: " + url)

    # Make the request and pass to a response object that the function returns
    response = requests.get(url)
    return response


response = make_request(base_url, ext_get_transcripts)
print(response.status_code)
print(response.json)
#Todo: Filter values from response.json()
