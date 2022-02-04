#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Created on Fri Feb  4 17:35:09 2022
#
# Arbitrador de Planes vs Capitalización
#
# https://github.com/anresz73/PlanAuto
#

"""
Functions to use in PlanAuto
"""

import pandas as pd
import numpy as np

def gen_cash_flow(file_name):
    """
    Generates Cash Flow from file
    """
    data = pd.read_excel(io = file_name,
                         sheet_name = 0,
                         engine = 'odf',
                         dtype = {'cuotanro' : np.int32, 'importe' : np.float32})
    return data