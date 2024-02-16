#code reviewed in team meeting. this code is not to be used. conflict with main branch due to incorrect push/pull reqyest. GL and CT copying code over onto main. 

from flask import Flask, request
from flask_restx import Api, Resource, reqparse
import requests
import logging
import logging.handlers as handlers