from flask import Flask, request
from flask_restx import Api, Resource, reqparse
import requests
import logging
import logging.handlers as handlers

#import module 1 Var Recoder
from Modules import module1_variantrecoder
#need to call relevant attribute or class item from module code. tried all items and wont accept. repeated error message "no attribute"
    #print all available attributes or classes from module1 with:
        #print(dir(module1_variantrecoder))
module1_variantrecoder.__name__

#import module 2 VarVal
from Modules import module2_variantvalidator
#print(dir(module2_variantvalidator))
module2_variantvalidator.__name__

#import module 3 LOVD
from Modules import module3_VV_LOVD
module3_VV_LOVD.__name__

#import module 4 VEP
from Modules import module4_VV_VEP
module4_VV_VEP.__name__

#import module 5 SPDI
from Modules import module5_SPDI
module5_SPDI.__name__





#peters code examples from tutorial 16/2/24 start here:
import vep, vv, vr

if ensembletranscript in input:
    hgvs_genomic = vr(hgvs_transcript, genome_build)
if "NM_" input:
    hgvs_genomic = vv(hgvs_transcript, genome_build)

#annotation
if genmome_build = "GRCh38"
    vep38(variables)

def vep38():
    print ("hello from a function")

def vep37 ():
    print ("hello from a function 2")


