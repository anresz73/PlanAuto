"""
Created on Thu Feb  3 16:07:25 2022

@author: anresz73
"""

## PlanAuto
# Arbitrador de un plan con Capital Amortizado de alguna manera

# Libs
from os import path
import io

here = path.abspath(path.dirname(__file__))

with io.open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()