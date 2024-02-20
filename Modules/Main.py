# -*- coding: UTF-8 -*-
"""
This module is the central module that will be used to call upon the other modules and logs its usage.
"""

# Import modules that will be called to complete requests from the Main.py API
import module1_variantrecoder
import module2_variantvalidator
import module3_VV_LOVD_code_only
import module4_VEP_code_only
import module5_SPDI
import logging

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

# Import functions from the other modules
from flask import Flask

app = Flask(__name__)


# Routes for module functionality
"""
Input should be an Ensembl transcript
"""
@app.route("/SprintFinish/Modules/module1_variantrecoder.py")
def call_module1_function():
    result = module1_variantrecoder.function1()
    return result

"""
Input should be a Refseq transcript
"""
@app.route("/SprintFinish/Modules/module2_variantvalidator.py")
def call_module2_function():
    result = module2_variantvalidator.function2()
    return result

"""
Input for module3 should be the output from module1 or module2
"""
@app.route("/SprintFinish/Modules/module3_VV_LOVD_code_only.py")
def call_module3_function():
    result = module3_VV_LOVD_code_only.function3()
    return result

"""
Input for module4 should be the output from module1 or module2
"""
@app.route("/SprintFinish/Modules/module4_VEP_code_only.py")
def call_module4_function():
    result = module4_VEP_code_only.function4()
    return result

@app.route("SprintFinish/Modules/module5_SPDI.py")
def call_module5_function():
    result = module5_SPDI.function5()
    return result

if __name__ == "__main__":
    app.run(debug=True)
    app.run(host="127.0.0.1", port=5000)  # Specify a host and port for the app