# SprintFinish
Sprint 2 and final assessment project for Group 1 (Module 3 PGCert Clinical Bioinformatics Intro to Programming)
SprintFinish is a Flask-based RESTful API for retrieving genomic data, including ensemble transcripts, RefSeq transcripts, LOVD variant annotations, and VEP variant data.

This README provides an overview of the SprintFinish RESTful API, installation instructions, usage guidelines, testing procedures, contribution guidelines, and license information

This python API integration will accept GEL variant descriptions (ie. c. 4375C>T) and provide valid and accurate genome, transcript and protein variant descriptions.
This product will gather the information from Variant Validator REST aPI and return the data as a Python dictionary.

# About rest_variantValidator

This project utilises rest_variantValidator, a RESTful API web interface for VariantValidator

# About VariantValidator

VariantValidator is a user-friendly software tool designed to validate the syntax and 
parameters of DNA variant descriptions according to the HGVS Sequence Variant 
Nomenclature. 

VariantValidator ensures that users are guided through the intricacies of the HGVS 
nomenclature, e.g. if the user makes a mistake, VariantValidator automatically corrects 
the mistake if it can, or provides helpful guidance if it cannot. In addition, 
VariantValidator accurately interconverts between transcript variant descriptions and 
genomic variant descriptions in HGVS and Variant Call Format (VCF)

VariantValidator interfaces with the hgvs package to parse, format, and manipulate 
biological sequence variants.  See https://github.com/biocommons/hgvs/ for details of the
hgvs package

VariantValidator is a highly functional platform enabling high-throughput and embeddable
utilisation of functionality of https://variantvalidator.org/

# Accepted Inputs

Input: Variant description as an Ensembl transcript description with or without version number

#The accepted format for variants include:

NM_000088.3:c.589G>T
NC_000017.10:g.48275363C>A
NG_007400.1:g.8638G>T
LRG_1:g.8638G>T
LRG_1t1:c.589G>T
17-50198002-C-A  # Note this variant is in the context of GRCh38
chr17:50198002C>A  # Note this variant is in the context of GRCh38

The output received by the client is: Genomic, transcript and protein descriptions with genome annotations.

## Pre-requisites

SprintFinish will work on Mac OS X or Linux operating systems.

Required software:
* MySQL
* Python 2.7
* SQLite version 3.8.0 or above

For installation instructions please see [SprintFinish_Installation.md]()

## Endpoints

Below are the available endpoints:

- **Ensemble Transcript**
  - `/ensemble-transcript/<ensemble_transcript>`
    - Returns a genomic HGVS transcript.

- **RefSeqTranscript - Georgia and Christoph**
  - `/RefSeq Release Version 222/variantvalidator/<genome_build>/<variant_description>/<select_transcripts>`
    - Returns a genomic HGVS transcript and genome coordinate.

- **LOVD**
  - `/lovd/<genome_build>/<variant_description>/<select_transcripts>/<checkonly>`
    - Returns variant data from the Leiden Open Variation Database (LOVD) using the VariantValidator API.

- **VEP**
  - `/VEP/<genome_build>/<variant_description>/<select_transcripts>`
    - Returns VEP variant data from the Ensembl REST API.

## Testing

Run the provided test scripts to validate the functionality of the API endpoints.

## Logging

Errors and exceptions are logged to `rest_api.log`.

## Contributing

1. Fork the repository.
2. Create a new branch.
3. Make your changes and commit them.
4. Push to your fork and submit a pull request.

## Operation and configuration

Please see [SprintFinish_UserGuide.md]()

## License

Please see [LICENSE]()

## Contributions in alphabetical order by team members:

Christoph
Georgia
Linda
Lisa
Nurhayu
Sonja
