# SprintFinish User Guide

Welcome to the user guide for SprintFinish! This guide will demonstrate how to configure, install and run the SprintFinish code.
If you encounter any issues or have questions, don't hesitate to contact our support team.

## Introduction
SprintFinish is a Flask-based RESTful API created to retrieve genomic data from an Ensembl or RefSeq transcript description and return genomic HGVS, genomic coordinates, LOVD variant annotations and VEP variant data.

This project utilises the Variant Validator, variant recorder and ensemble API.
This GitHub repository contains all the necessary files and resources to get started.

## Prerequisites
Before you begin, ensure you have the following installed:
Python 3.11 or above.
All other dependencies are listed in requirements.txt file.

## Installation
To install SprintFinish, follow instructions as stated in SprintFinish_Installation.md file. 

## Configuration
To configure SprintFinish, follow these steps:
1. Clone the SprintFinish source code, as described in SprintFinish_Installation.md.
2. Install dependencies ("pip install -r requirements.txt").
3. Configure virtual environment, as described in SprintFinish_Installation.md.
4. Customise configuration files. Edit any configuration files as needed and modify settings in files such as 'gitignore', based on your requirements. 
5. Read through all documentation files (SprintFinish_Installation, UserGuide and README.md).

## Usage
Once SprintFinish is installed and configured, you can start using it:

The accepted format for variants include:

NM_000088.3:c.589G>T
NC_000017.10:g.48275363C>A
NG_007400.1:g.8638G>T
LRG_1:g.8638G>T
LRG_1t1:c.589G>T
17-50198002-C-A  # Note this variant is in the context of GRCh38
chr17:50198002C>A  # Note this variant is in the context of GRCh38

## Contributing
We welcome contributions from the community! If you'd like to contribute to ProjectName, please follow these guidelines:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new pull request.

## License
See License.txt

---
Thank you for using SprintFinish! If you have any feedback or suggestions, please [contact us](mailto:supprt@psprintfinish.com).
