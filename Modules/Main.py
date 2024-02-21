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

app = Flask(__name__)

# Determine logger format and create the file
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename = "E:\\python\\Mainpy.log",
                    level = logging.DEBUG,
                    format = LOG_FORMAT)
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
    if "ENST" in input_data.get("transcript_id", ""):
        module1_output = module1_variantrecoder.function1()
        result = {
            "module1_output": module1_output,
            "transcript_id": input_data.get("transcript_id")
        }
    elif "NM_" in input_data.get("transcript_id", ""):
        module2_output = module2_variantvalidator.function2()
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
    if "module1_output" in input_data:
        module3_output = module3_VV_LOVD_code_only.function3(input_data["module1_output"])
    elif "module2_output" in input_data:
        module3_output = module3_VV_LOVD_code_only.function3(input_data["module2_output"])
    else:
        return "Invalid input: module1_output or module2_output not provided"

    print("Module 3 Output:", module3_output)  # Print module3 output
    return jsonify({"module3_output": module3_output})


@app.route("/module4_function", methods=["POST"])
def call_module4_function():
    input_data = request.json  # Assuming JSON input
    if "module1_output" in input_data:
        module4_output = module4_VEP_code_only.function4(input_data["module1_output"])
    elif "module2_output" in input_data:
        module4_output = module4_VEP_code_only.function4(input_data["module2_output"])
    else:
        return "Invalid input: module1_output or module2_output not provided"

    print("Module 4 Output:", module4_output)  # Print module4 output
    return jsonify({"module4_output": module4_output})


@app.route("/module5_function", methods=["POST"])
def call_module5_function():
    input_data = request.json  # Assuming JSON input
    if "module1_output" in input_data:
        module5_output = module5_SPDI.function5(input_data["module1_output"])
    elif "module2_output" in input_data:
        module5_output = module5_SPDI.function5(input_data["module2_output"])
    else:
        return "Invalid input: module1_output or module2_output not provided"

    print("Module 5 Output:", module5_output)  # Print module5 output
    return jsonify({"module5_output": module5_output})


if __name__ == "__main__":
    app.run(debug=True)

