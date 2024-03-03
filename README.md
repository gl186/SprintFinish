## SprintFinish

SprintFinish is a Flask-based RESTful API that performs genomic data retrieval and analysis, including Ensembl or RefSeq transcripts, LOVD variant annotations, and VEP variant data.

Developed by Group 1 in Module 3 for the PGCert Clinical Bioinformatics Introduction to Programming.

## Overview

This README provides an overview of the SprintFinish RESTful API, installation instructions, usage guidelines, testing procedures, contribution guidelines, and license information.

This Python API integration accepts GEL variant descriptions (e.g., c.4375C>T) and provides valid and accurate genome, transcript, and protein variant descriptions.

## Installation

Ensure Anaconda or Miniconda is installed on your machine along with a Linux or Mac OS X operating system. Create the conda environment using the provided `environment.yml` file:
```bash
conda env create -f environment.yml
```

Activate the environment:
```
conda activate SprintFinish
```
Install the requirements:

```
pip install -r requirements.txt
```
Navigate to the directory containing Varan.py and run:
```
flask --app Varan --debug run
```

## For detailed installation instructions, see:
SprintFinish_Installation.md.

## About Rest Variant Validator
SprintFinish utilizes Rest Variant Validator, a RESTful API web interface for VariantValidator.

## About VariantValidator
VariantValidator is a user-friendly tool designed to validate the syntax and parameters of DNA variant descriptions according to the HGVS Sequence Variant Nomenclature. It interconverts between transcript variant descriptions and genomic variant descriptions in HGVS and Variant Call Format (VCF).

VariantValidator interfaces with the hgvs package to parse, format, and manipulate biological sequence variants. Visit the VariantValidator GitHub repository for details.

## Accepted Inputs
SprintFinish accepts variant descriptions in various formats, including Ensembl transcript descriptions with or without version numbers. Examples include:

NM_000088.3:c.589G>T
NC_000017.10:g.48275363C>A
NG_007400.1:g.8638G>T
LRG_1:g.8638G>T
LRG_1t1:c.589G>T
17-50198002-C-A
chr17:50198002C>A
Usage
Ensure Flask is installed and your environment is running correctly. Once set up, run the Flask application to host the API locally.

## Endpoints
Ensemble Transcript

/ensemble-transcript/<ensemble_transcript>
Returns a genomic HGVS transcript.
RefSeq Transcript

/RefSeq Release Version 222/variantvalidator/<genome_build>/<variant_description>/<select_transcripts>
Returns genomic HGVS transcript and genome coordinate.
LOVD

/lovd/<genome_build>/<variant_description>/<select_transcripts>/<checkonly>
Returns variant data from the Leiden Open Variation Database (LOVD) using the VariantValidator API.
VEP

/VEP/<genome_build>/<variant_description>/<select_transcripts>
Returns VEP variant data from the Ensembl REST API.
Response Formats
SprintFinish supports JSON and XML response formats. Specify the desired format using the content-type parameter in your request.

## Testing
Run the provided pytest test scripts to validate the functionality of the API endpoints.

## Logging
Errors and exceptions are logged to Mainpy.log.

## Contributing
Fork the repository.
Create a new branch.
Make your changes and commit them.
Push to your fork and submit a pull request.
Operation and Configuration
Refer to SprintFinish_UserGuide.md for detailed operational and configuration information.

## License
This project is licensed under the LICENSE.

## Contributors
Christoph
Georgia
Linda
Lisa
Nurhayu
Sonja

## Contact Information
For inquiries, contact christoph.johnson@postgrad.manchester.ac.uk
