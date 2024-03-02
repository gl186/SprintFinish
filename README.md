# SprintFinish

SprintFinish is a cutting-edge Flask-based RESTful API designed to revolutionize the way genomic data is retrieved and analyzed. Developed as the capstone project for Group 1 in the Module 3 PGCert Clinical Bioinformatics Introduction to Programming, SprintFinish stands out as a comprehensive solution for bioinformatics professionals and researchers seeking fast, reliable access to a wide array of genomic information.
At its core, SprintFinish specializes in the precise interpretation and conversion of GEL variant descriptions (e.g., c. 4375C>T) into valid and accurate genome, transcript, and protein variant descriptions. By leveraging the power of the Variant Validator REST API, SprintFinish not only simplifies the process of genomic data retrieval but also ensures that the information provided is both accurate and up-to-date, presented in an easily consumable Python dictionary format.
Whether you're analyzing ensemble transcripts, RefSeq transcripts, exploring LOVD variant annotations, or delving into VEP variant data, SprintFinish offers a seamless and efficient API solution tailored to meet the demanding needs of the bioinformatics community.
This README serves as your comprehensive guide to the SprintFinish RESTful API, including detailed installation instructions, user-friendly usage guidelines, straightforward testing procedures, and more. Join us in our journey to empower genomic research and exploration through state-of-the-art technology and innovation.


# Installation Instructions:

To get SprintFinish up and running on your system, follow these simple steps:
Prerequisites:
    Anaconda or Miniconda installed on your machine.

Setting Up the Environment:
* Create the Conda Environment: Start by creating a new conda environment using the provided environment file. Open your terminal or command prompt and navigate to the directory containing the environment.yml file. Then, execute the following command:

```commandline
conda env create -f environment.yml
```
This command will create a new conda environment named SprintFinish and install the necessary packages from the conda-forge and bioconda channels, including Python 3.12.1.

* Activate the Environment: Once the environment setup is complete, you can activate it by running:

```commandline
conda activate SprintFinish
```

* Install Additional Requirements: With the environment activated, install the additional requirements using the requirements.txt file provided in the project.
* Ensure you're in the project directory and execute:

```commandline
pip install -r requirements.txt
```
This will install specific versions of dicttoxml, Flask, flask_restx, pytest, requests, and requests_mock essential for the API to function correctly.

* Verifying the Installation:
- To verify that the installation was successful, you can start the Flask application and ensure it runs without errors.
- Navigate to the directory containing the app.py file (or the main Flask application script) and execute:
```commandline
 flask --app Varan --debug run
```
If everything is set up correctly, you should see Flask starting up the server, indicating the API is now running and accessible.
## Pre-requisites

SprintFinish will work on Mac OS X or Linux operating systems.
Required software:

* Anaconda or Miniconda installed on your machine.
* python=3.12.1

For further information about installation instructions please see [SprintFinish_Installation.md](./SprintFinish_Installation.md)


# Usage Guidelines
Getting Started

To utilize the SprintFinish API, ensure you have Flask installed and your environment is properly set up as detailed in the Installation Instructions. Once the setup is complete, you can start the Flask application by running the provided script. This will host the API on your local server, typically accessible via http://127.0.0.1:5000.
Endpoints and Operations

SprintFinish provides several endpoints, each tailored to specific genomic data retrieval and processing needs:
### Transcript Mapper

    Endpoint: /HGVS/<select_transcripts>/<transcript_model>/<genome_build>
    Method: GET
    Description: Retrieves genomic, transcript, and protein descriptions based on the specified parameters.
    Parameters:
        select_transcripts: Choose between ensembl or refseq, or specify all for the latest version of each transcript.
        transcript_model: Provide the transcript model ID (e.g., ENST00000366667:c.803C>T for ensembl or NM_000093.4 for refseq).
        genome_build: Specify the genome build (GRCh37, GRCh38, hg19, or hg38).

### Genomic Annotator

    Endpoint: /LOVD/<variant_description>/<transcript_model>/<liftover>/<genome_build>/<checkonly>/<select_transcripts>
    Method: GET
    Description: Offers detailed variant descriptions and annotations.
    Parameters:
        variant_description, transcript_model, liftover, genome_build, checkonly, select_transcripts: Detailed parameters for LOVD variant annotations, including genomic HGVSg, transcript model selection, and genome build.

### Extra Annotations

    Endpoint: /extraAnnotation/<genomic_transcript>/<select_extraannotation>
    Method: GET
    Description: Provides additional annotations using SPDI or VEP based on the given genomic transcript.
    Parameters:
        genomic_transcript: The genomic transcript for which additional annotations are needed.
        select_extraannotation: Choose between SPDI and VEP for the type of annotation.

#### Response Formats

SprintFinish supports responses in both JSON and XML formats. 
You can specify the desired format by including the content-type parameter in your request with either application/json or text/xml.
Examples

To retrieve ensembl transcript data for a specific model in JSON format:

bash

GET /HGVS/ensembl/ENST00000366667:c.803C>T/GRCh38?content-type=application/json

For XML response:

bash

GET /HGVS/ensembl/ENST00000366667:c.803C>T/GRCh38?content-type=text/xml

To explore more about using the SprintFinish API, refer to the detailed API documentation accessible via Swagger UI once the Flask app is running.
# Testing Procedures
This document outlines the procedures for testing the various components and functionalities within the project. The project is tested through a combination of unit tests for individual modules and functional tests for API endpoints.

### Unit Testing 
Unit tests are designed to test individual parts of the codebase in isolation, ensuring that each function behaves as expected.
#### Running Unit Tests
To run the unit tests, navigate to the root directory of the project and use the following command:
```commandline
pytest Tests/unit name that you want to test/
```
Test Cases

    Module 1 Variant Recoder Tests:
        Success case: Test if the ensemblMapper function returns the correct mapping for a known input.
        Failure case: Test how the function handles an invalid input or when the external service is unavailable.

    Module 2 Variant Validator Tests:
        Success and failure cases for fetching genomic information based on transcript IDs.

    Module 3 LOVD Integration Tests:
        Tests for successful and unsuccessful retrieval of genomic transcript information.

    Module 4 VEP Annotation Tests:
        Ensures that variant annotations are correctly fetched or handled during failures.

    Module 5 SPDI Query Tests:
        Verifies the handling of SPDI queries, including success, failure, and exception scenarios.


### Functional Testing
Functional tests verify the application's behavior as a whole, ensuring that the API endpoints function correctly when integrated.
#### Running Functional Tests
To run the functional tests, use the following command:
```commandline
pytest Tests/test_varan.py
```
This will execute all tests within the tests/functional/ directory, testing the API's response to various requests.
Test Endpoints

    HGVS Endpoint Test:
    Tests the response for fetching transcript mapping based on HGVS notation.

    LOVD Endpoint Test:
    Verifies the integration with LOVD for variant descriptions.

    Extra Annotation Endpoint Test:
    Checks additional annotation functionalities, ensuring both VEP and SPDI annotations are retrievable.
To run all the tests run the following command:
```commandline 
pytest Tests/
```


### Reporting Issues

If you encounter any issues or failed tests, please report them on the project's issues page with detailed steps to reproduce the issue and any relevant error messages or stack traces.




## Logging

Errors and exceptions are logged to `rest_api.log`.

## Contributing

1. Fork the repository.
2. Create a new branch.
3. Make your changes and commit them.
4. Push to your fork and submit a pull request.

## Operation and configuration

Please see [SprintFinish_UserGuide.md](SprintFinish_UserGuide.md)

## License

Please see [LICENSE](LICENSE)

## Contact Information:
Please reach out for any support or to contribute via email address: (linda.alhasanalnsour@postgrad.manchester.ac.uk) 
## Acknowledgments:
Credits to all of my team contributors (Christoph, Georgia, Sonja, Lisa and Nurhayu) and our sources of inspiration Prof.Peter Freeman
