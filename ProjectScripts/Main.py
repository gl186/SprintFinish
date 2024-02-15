from flask import Flask, request
from flask_restx import Api, Resource, reqparse
import requests
import logging
import logging.handlers as handlers

#import module 1 Var Recoder
from Modules import module1_variantrecoder

#import module 2 VarVal
from Modules import module2_variantvalidator

#import module 3 LOVD
from Modules import module3_VV_LOVD

#import module 4 VEP
from Modules import module4_VV_VEP

#import module 5 SPDI
from Modules import module5_SPDI



