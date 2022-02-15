#!.venv/bin/python3
# -*- coding: utf-8 -*-
#
# Created on Fri Feb  4 17:35:09 2022
#
# Arbitrador de Planes vs Capitalización
#
# https://github.com/anresz73/PlanAuto

## PlanAuto
# Arbitrador de un plan con Capital Amortizado de alguna manera

# Libs
#from PlanAuto import get_cash_flow

from os import path
from setuptools import setup, find_packages
import io

here = path.abspath(path.dirname(__file__))

with io.open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Setup
setup(
      name = 'PlanAuto',
      packages = find_packages(),
      long_description = long_description,
      )