## Intro 
About Ensemble Transcript Mapper 


this API uses the Variant Recoder which is a tool for translating between different variant names. It takes the ensemble transcript and mapping it to genomic HGVS for it to be an output.

For each input variant, Ensemble Transcript Mapper reports the variant identifiers held in Ensembl and HGVS genomic, transcript and protein descriptions on Ensembl, RefSeq and LRG sequences.
## How to use

The Ensemble Transcript Mapper web interface allows you to simply enter variant names and identifiers in a Ensemble annotation and obtain HGVS annotation as an output.
it will accept an Ensembl transcript variant description lacking the version number, and return genomic, transcript and protein HGVS

### how to run the API:
On terminal use this commandline 
```commandline
python3 ProjectScripts/Modules/module1_variantrecoder/module1_variantrecoder.py
```
### Sample Request 
```curls
curl -X 'GET' \
  'http://127.0.0.1:5000/VEP/NM_000138.4%3Ac.356G%3EA?assembly=GRCh37' \
  -H 'accept: application/json'
```

### Sample Response 
```json
{
  "Genomic-HGVS": [
    {
      "T": {
        "hgvsc": [
          "ENST00000366667.6:c.803C>T",
          "ENST00000679684.1:c.803C>T",
          "ENST00000679738.1:c.803C>T",
          "ENST00000679802.1:c.803C>T",
          "ENST00000679854.1:n.1314C>T",
          "ENST00000679957.1:c.803C>T",
          "ENST00000680041.1:c.803C>T",
          "ENST00000680783.1:c.803C>T",
          "ENST00000681269.1:c.803C>T",
          "ENST00000681347.1:n.1314C>T",
          "ENST00000681514.1:c.803C>T",
          "ENST00000681772.1:c.803C>T",
          "NM_001382817.3:c.803C>T",
          "NM_001384479.1:c.803C>T"
        ],
        "hgvsg": [
          "NC_000001.11:g.230710021G>A"
        ],
        "hgvsp": [
          "ENSP00000355627.5:p.Ala268Val",
          "ENSP00000505981.1:p.Ala268Val",
          "ENSP00000505063.1:p.Ala268Val",
          "ENSP00000505184.1:p.Ala268Val",
          "ENSP00000506646.1:p.Ala268Val",
          "ENSP00000504866.1:p.Ala268Val",
          "ENSP00000506329.1:p.Ala268Val",
          "ENSP00000505985.1:p.Ala268Val",
          "ENSP00000505963.1:p.Ala268Val",
          "ENSP00000505829.1:p.Ala268Val",
          "NP_001369746.2:p.Ala268Val",
          "NP_001371408.1:p.Ala268Val"
        ],
        "id": [
          "rs1228544607"
        ],
        "input": "ENST00000366667:c.803C>T",
        "spdi": [
          "NC_000001.11:230710020:G:A"
        ]
      }
    }
  ]
}
```

### Output
Output is a JSON array of objects, one per input variant, with the following keys:

    input: input string
    id: variant identifiers
    hgvsg: HGVS genomic nomenclature
    hgvsc: HGVS transcript nomenclature
    hgvsp: HGVS protein nomenclature
    spdi: Genomic SPDI notation
    vcf_string: VCF format (optional)
    var_synonyms: Extra known synonyms for co-located variants (optional)
    mane_select: MANE Select (Matched Annotation from NCBI and EMBL-EBI) Transcripts. (optional) Note: only available for human.
    warnings: Warnings generated e.g. for invalid HGVS


### Required software:
Conda
Python 2.7 version or above

### Required dependencies:
Flask
Request
Flask_restx

### Validations 
This API is tested to work on Mac OS X or Linux operating systems.

### License
Please see LICENSE.txt

