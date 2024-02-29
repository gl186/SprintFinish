# -*- coding: UTF-8 -*-
"""
This module is the central module that will be used to call upon the other modules and logs its usage.
"""

# Import modules that will be called to complete requests from the Main.py API
from flask import Flask, jsonify
from Modules import module1_variantrecoder
from Modules import module2_variantvalidator
from Modules import module3_VV_LOVD_code_only
from Modules import module4_VEP_code_only
from Modules import module5_SPDI
import logging

app = Flask(__name__)

# Determine logger format and create the file
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="E:\\python\\Mainpy.log",
                    level=logging.DEBUG,
                    format=LOG_FORMAT)
logger = logging.getLogger()

# Determine logger messages and arrange them by the 5 levels of severity
logger.info("This is an info message")
logging.debug("This is a debug message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")

print(logger.level)


# Routes for module functionality
def call_module1_function(transcript_model):
    if "ENST" in transcript_model:
        module1_output = module1_variantrecoder.ensemblMapper(transcript_model)
        result = {
            "module1_output": module1_output,
            "ensembleTranscript": transcript_model
        }
    elif "NM_" in transcript_model:
        module2_output = module2_variantvalidator.get_genomic_info_from_transcript(transcript_model)
        result = {
            "module2_output": module2_output,
            "transcript_id": transcript_model
        }
    else:
        return "Invalid input: transcript_id should contain 'ENST' or 'NM_'"

    print("module1_output", result)
    return jsonify(result)


def call_module3_function(variant_description, transcript_model, genome_build, liftover, checkonly, select_transcripts):
    # Call module 3 function to get mane variant description
    dict_mane_variants = module3_VV_LOVD_code_only.get_genomic_transcript(variant_description, transcript_model,
                                                                          genome_build, liftover, checkonly,
                                                                          select_transcripts)

    print("Module 3 MANE output:", dict_mane_variants)  # Print module3 output
    return jsonify({"MANE output": dict_mane_variants})


def call_module4_function(genomic_transcript, select_extraannotaion):
    # Call module 4 function to get VEP annotations for genomic_transcript
    dict_vep_annotation = module4_VEP_code_only.get_variant_annotation(genomic_transcript, select_extraannotaion)

    print("Module 4 VEP Output:", dict_vep_annotation)  # Print module4 output
    return {"VEP_annotations": dict_vep_annotation}

#
# def call_module5_function(input_data):
#     if input_data is None:
#         return "Invalid input: JSON data not provided"
#
#     # Define hgvs based on module1_output or module2_output
#     if "module1_output" in input_data:
#         hgvs = input_data["module1_output"]
#     elif "module2_output" in input_data:
#         hgvs = input_data["module2_output"]
#     else:
#         return "Invalid input: module1_output or module2_output not provided"
#
#     # Call modules 5 functions to get SPDI format and descriptive detail
#     dict_spdi_format = module5_VR_SPDI_code.get_SPDI(hgvs)
#     dict_spdi_detail = module5_SPDI.get(hgvs)
#
#     print("Module 5 SPDI Output:", dict_spdi_format, dict_spdi_detail)  # Print module5 output
#     return jsonify({"SPDI_format": dict_spdi_format, "SPDI_detail": dict_spdi_detail})
