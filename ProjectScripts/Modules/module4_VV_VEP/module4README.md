## Written by Nurhayu
***
##  Variant Effect Predictor API 

The Variant Effect Predictor (VEP) API allows you to retrieve VEP annotations from the GRCh37 Ensembl REST API. It's a useful tool for analyzing genetic variants and understanding their impact on genes. 

### Usage 

### Requirements: 

    Make sure you have Python 3.12.1 , Flask and Flask-RestX installed. 

### Endpoints: 

    The API provides a single endpoint for querying VEP data based on variant descriptions in HGVS format.

    Retrieves GRCh37 Ensembl VEP annotations for the specified variant. 

    
### Parameters: 

    variant_description: HGVS format (e.g., NM_000138.4:c.356G>A) 

### Response: 

    The API returns a JSON response containing VEP annotations for the variant. 

    Error Handling: 

    If there's an issue fetching VEP data, an error message will be returned. 



Assuming you have the Flask app running locally, you can query the VEP data for a specific variant using the provided endpoint. 

--- 