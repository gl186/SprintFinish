from flask import Flask, request
from flask_restx import Api, Resource, reqparse
import requests
import logging
import logging.handlers as handlers

#import module 1
from Modules import module1_variantrecoder
from Modules.module1_variantrecoder import get



