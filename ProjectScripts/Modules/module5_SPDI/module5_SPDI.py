#import requests to allow python to send http request
import requests

#use get variant data function to take hgvs paramter
def get_variant_data(hgvs):
    #docstring describing what get variant data function is doing
    """Retrieve variant data from module5_SPDI via HGVS."""
    base_url = "https://api.ncbi.nlm.nih.gov/variation/v0/hgvs"
    #construct endpoint url appending hgvs and contextuals
    ext_get_transcripts = f"/{hgvs}/raw"  # Assuming 'raw' as the default for contextuals

#exception handling
    try:
        #links base url and end point url for final request url
        url = base_url + ext_get_transcripts
        #use request get function to send get request to final request url
        response = requests.get(url, headers={'Content-Type': 'application/json'})
        #check if response status code indicates an error and raised an exception if there is an error
        response.raise_for_status()
        #if no error, returns the variant data in a json
        return response.json()
    except requests.RequestException as e:
        #if error occurs during the request, returns dictionary with error message
        return {"error": f"Error fetching module5_SPDI variant data: {e}"}

if __name__ == "__main__":
    #prompt user to use hgvs input
    hgvs_input = input("Enter HGVS format (e.g., NC_000017.10:g.48275363C>A): ")
    #uses the hgvs notation from user as an argument
    variant_data = get_variant_data(hgvs_input)
    #prints variant data retrieved
    print(variant_data)