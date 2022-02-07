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
Constantes para el seteo 
"""

from pandas import read_excel
from .functions import gen_cash_flow

# Constantes

VALOR_AUTO = 2400000.
VALOR_CAPITALIZAR = 1200000.
TASA_INTERES = .3
INFLACION_MENSUAL = .03
CAHH_FLOW = gen_cash_flow(r'../Data/data.ods')

#CASH_FLOW = #data['importe'].sum()
