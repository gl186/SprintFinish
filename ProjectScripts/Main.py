from flask import Flask, request
from flask_restx import Api, Resource, reqparse
import requests
import logging
import logging.handlers as handlers
import Modules.module3_VV_LOVD.rev_Sonja_code
import rev_Sonja_code
# Temporary debug code to understand main.py calling modules
rev_Sonja_code.debug_import()