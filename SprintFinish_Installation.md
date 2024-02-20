**INSTALLATION OF SPRINTFINISH**

This document gives the instruction to install the package and accompanying databases required for SprintFinish.

**For systems Linux and Mac OS X. For other systems or if you cannot install the databases, we recommend installing via docker.**

_**Pre-requisites**_

**Required:**

Python 3.11 or above


**_Download the SprintFinish source code_**

To download the SprintFinish source code simply clone the master branch.

git clone https://github.com/SprintFinishGroup/SprintFinish.git

When installing SprintFinish we recommend using a virtual environment, as it requires specific versions of several libraries including python and sqlite. This can be done either via conda or pip.


**Via conda (Recommended)**

After installing conda you can create a new virtual environment with the correct python and sqlite versions by running:

$ conda env create -f environment.yml
$ conda activate SprintFinish
The packages required for SprintFinish to function are now set up in the environment "SprintFinish".


**Via pip**

If you already have the right versions of python (>=3.12) and sqlite (>=3.8), then you can use pip to BT create a new virtual environment and install the packages required for SprintFinish to function.

$ python -m venv SprintFinish
$ source activate SprintFinish


**Installing SprintFinish**

Hint: your new environment SprintFinish should still be activated from the previous steps and you should still be in the /SprintFinish directory where setup.py is located.

To install SprintFinish within your virtual environment run:

$ pip install .


**Developers**

Please make all Pull Requests to the develop branch. If you are unsure, contact admin via issues.

For development purposes, use the following,

$ pip install -e 

**Configuration**

Before using SprintFinish some configuration is required. 
Please see the manual for further instruction.
