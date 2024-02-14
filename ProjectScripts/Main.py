# This is the main py script from SprintFinish group
# Press Shift+F10 to execute it

#import necessary modules, flask imported to create the web application
#api and resource from flask_restx are imported to define the restful api endpoints
#requests is imported to sent http requests for testing the api
from flask import Flask
from flask_restx import Api, Resource
import requests
import logging
import logging.handlers as handlers

