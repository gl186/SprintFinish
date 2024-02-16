# Import modules
from flask import Flask, make_response
from flask_restx import Api, Resource
import requests
import logging

# Determine logger format and create the file
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename = "E:\\python\\Mainpy.log",
                    level = logging.DEBUG,
                    format = LOG_FORMAT)
logger = logging.getLogger()

#Testing logger messages
logger.info("This is an info message")
logging.debug("This is a debug message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")

print(logger.level)

# Import functions from the other modules
from flask import Flask, redirect, url_for, request


app = Flask(__name__)

# Pass the function to the respective module
@app.route(SprintFinish/ProjectScripts/Modules/module1_variantrecoder/module1_variantrecoder.py)
# Define functions for each module
#change to get request

@app.route(SprintFinish/ProjectScripts/Modules/module2_variantvalidator/modeule2_variantvalidator.py)
#change to get request


@app.route(SprintFinish/ProjectScripts/Modules/module3_VV_LOVD/rev_Sonja_code.py)
#change to get request


@app.route(SprintFinish/ProjectScripts/Modules/module4_VV_VEP/module4_VV_VEP_final.py)
#change to get request


if __name__ == "__main__":
    app.run(debug=True)
    app.run(host="127.0.0.1", port=5000)  # Specify a host and port for the app