# -*- coding: UTF-8 -*-
"""
This module is the central module that will be used to call upon the other modules and logs its usage.
"""

# Import modules that will be called to complete requests from the Main.py API
from flask import Flask, jsonify
from Modules import module1_variantrecoder
from Modules import module2_variantvalidator
from Modules import module3_VV_LOVD
from Modules import module4_VEP
from Modules import module5_SPDI
import logging


# Determine logger format and create the file
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(level=logging.DEBUG,
                    format=LOG_FORMAT)
logger = logging.getLogger("Main")

# Determine logger messages and arrange them by the 5 levels of severity
logger.info("This is an info message")
logging.debug("This is a debug message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")



# Routes for module functionality
def call_module1_function(transcript_model):
    if "ENST" in transcript_model:
        module1_output = module1_variantrecoder.ensemblMapper(transcript_model)
        return jsonify({
            "module1_output": module1_output,
            "ensembleTranscript": transcript_model
        })
    elif "NM_" in transcript_model:
        module2_output = module2_variantvalidator.get_genomic_info_from_transcript(transcript_model)
        return jsonify({
            "module2_output": module2_output,
            "transcript_id": transcript_model
        })
    else:
        return "Invalid input: transcript_id should contain 'ENST' or 'NM_'"


def call_module3_function(variant_description, transcript_model, genome_build, liftover, checkonly, select_transcripts):
    # Call module 3 function to get mane variant description
    dict_mane_variants = module3_VV_LOVD.get_genomic_transcript(variant_description, transcript_model,
                                                                genome_build, liftover, checkonly,
                                                                select_transcripts)

    logging.info("Module 3 MANE output:", dict_mane_variants)# logging.info module3 output
    return jsonify({"MANE output": dict_mane_variants})


def call_module4_function(genomic_transcript):
    # Call module 4 function to get VEP annotations for genomic_transcript
    dict_vep_annotation = module4_VEP.get_variant_annotation(genomic_transcript)

    logging.info(f"Module 4 VEP Output: {dict_vep_annotation}")  # logging.info module4 output
    return {"VEP_annotations": dict_vep_annotation}


#
def call_module5_function(genomic_transcript):
    # Call module 5 function to get SPDI annotations for genomic_transcript
    dict_spdi_annotation = module5_SPDI.get_variant_annotation2(genomic_transcript)
    logging.info(f"Module 5 SPDI Output: {dict_spdi_annotation}")  # logging.info module5 output
    return {"SPDI_annotations": dict_spdi_annotation}
