from flask import Flask, request
from flask_restx import Api, Resource, reqparse
import requests
import logging
import logging.handlers as handlers

#import module 1 Var Recoder
import module1_variantrecoder
#need to call relevant attribute or class item from module code. tried all items and wont accept. repeated error message "no attribute"
    #print all available attributes or classes from module1 with:
        #print(dir(module1_variantrecoder))

#import module 2 VarVal
import module2_variantvalidator



#import module 3 LOVD
import module3_VV_LOVD


#import module 4 VEP
import module4_VV_VEP


#import module 5 SPDI
import module5_SPDI
if __name__ == "__main__":
    hgvs_input = input("Enter HGVS format (e.g., NC_000017.10:g.48275363C>A): ")
    variant_data = variant_data_module.get_variant_data(hgvs_input)
    print(variant_data)




#peters code examples from tutorial 16/2/24 start here:
#import vep, vv, vr

#if ensembletranscript in input:
 #   hgvs_genomic = vr(hgvs_transcript, genome_build)
#if "NM_" input:
  #  hgvs_genomic = vv(hgvs_transcript, genome_build)

#annotation
#if genmome_build = "GRCh38"
 #   vep38(variables)

#def vep38():
 #   print ("hello from a function")

#def vep37 ():
 #   print ("hello from a function 2")


