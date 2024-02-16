# -*- coding: utf-8 -*-
"""
This module is the central module that will be used to call upon the other modules and logs its usage.
"""

# Import modules that will be called to complete requests from the Main.py API
import module1_variantrecoder
import module2_variantvalidator
import rev_Sonja_code
import module4_VV_VEP_final
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
from flask import Flask, redirect, url_for, request


app = Flask(__name__)

# Create Variantrecoder object
class variantrecoder
    """
    This object contains 
    """
# Pass the function to the respective module
@app.route(SprintFinish/Modules/module1_variantrecoder/module1_variantrecoder.py)
# Define functions for each module
#change to get request

@app.route(SprintFinish/Modules/module2_variantvalidator/module2_variantvalidator.py)
#change to get request


@app.route(SprintFinish/Modules/module3_VV_LOVD/rev_Sonja_code.py)
#change to get request


@app.route(SprintFinish/Modules/module4_VV_VEP/module4_VV_VEP_final.py)
#change to get request


if __name__ == "__main__":
    app.run(debug=True)
    app.run(host="127.0.0.1", port=5000)  # Specify a host and port for the app