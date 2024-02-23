# -*- coding: UTF-8 -*-
"""
This module is the central module that will be used to call upon the other modules and logs its usage.
"""

# Import modules that will be called to complete requests from the Main.py API
from flask import Flask, request, jsonify
import module1_variantrecoder
import module2_variantvalidator
import module3_VV_LOVD_code_only
import module4_VEP_code_only
import module5_SPDI
import module5_VR_SPDI_code
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
@app.route("/module_function", methods=["POST"])
def call_module_function():
    input_data = request.json  # Assuming JSON input
    if "ENST" in input_data.get("ensembleTranscript", ""):
        module1_output = module1_variantrecoder.ensembleMapper(ensembleTranscript)
        result = {
            "module1_output": module1_output,
            "ensembleTranscript": input_data.get("ensembleTranscript")
         }
    elif "NM_" in input_data.get("transcript_id", ""):
        module2_output = module2_variantvalidator.get_genomic_info_from_transcript(transcript_id)
        result = {
             "module2_output": module2_output,
             "transcript_id": input_data.get("transcript_id")
         }
    else:
        return "Invalid input: transcript_id should contain 'ENST' or 'NM_'"

    return jsonify(result)


@app.route("/module3_function", methods=["POST"])
def call_module3_function():
    input_data = request.json  # Assuming JSON input
    if input_data is None:
        return "Invalid input: JSON data not provided"

    # Define variant_description based on module1_output or module2_output
    if "module1_output" in input_data:
        variant_description = input_data["module1_output"]
    elif "module2_output" in input_data:
        variant_description = input_data["module2_output"]
    else:
        return "Invalid input: module1_output or module2_output not provided"

    # Call module 3 function to get mane variant description for GRCh37 and GRCh38
    dict_mane_variants_grch37 = module3_VV_LOVD_code_only.get_for_GRCh37(variant_description)
    dict_mane_variants_grch38 = module3_VV_LOVD_code_only.get_for_GRCh38(variant_description)

    print("Module 3 MANE output:", dict_mane_variants_grch37, dict_mane_variants_grch38)  # Print module3 output
    return jsonify({"MANE_GRCh37": dict_mane_variants_grch37, "MANE_GRCh38": dict_mane_variants_grch38})


@app.route("/module4_function", methods=["POST"])
def call_module4_function():
    input_data = request.json  # Assuming JSON input
    if input_data is None:
        return "Invalid input: JSON data not provided"

    # Define hgvs_variant based on module1_output or module2_output
    if "module1_output" in input_data:
        hgvs_variant = input_data["module1_output"]
    elif "module2_output" in input_data:
        hgvs_variant = input_data["module2_output"]
    else:
        return "Invalid input: module1_output or module2_output not provided"

    # Call module 4 function to get VEP annotations for GRCh37 and GRCh38
    dict_vep_annotation = module4_VEP_code_only.get_variant_annotation(hgvs_variant)

    print("Module 4 VEP Output:", dict_vep_annotation)  # Print module4 output
    return jsonify({"VEP_annotations": dict_vep_annotation})


@app.route("/module5_function", methods=["POST"])
def call_module5_function():
    input_data = request.json  # Assuming JSON input
    if input_data is None:
        return "Invalid input: JSON data not provided"

    # Define hgvs based on module1_output or module2_output
    if "module1_output" in input_data:
        hgvs = input_data["module1_output"]
    elif "module2_output" in input_data:
        hgvs = input_data["module2_output"]
    else:
        return "Invalid input: module1_output or module2_output not provided"

    # Call modules 5 functions to get SPDI format and descriptive detail
    dict_spdi_format = module5_VR_SPDI_code.get_SPDI(hgvs)
    dict_spdi_detail = module5_SPDI.get(hgvs)

    print("Module 5 SPDI Output:", dict_spdi_format, dict_spdi_detail)  # Print module5 output
    return jsonify({"SPDI_format": dict_spdi_format, "SPDI_detail": dict_spdi_detail})


if __name__ == "__main__":
    app.run(debug=True)
