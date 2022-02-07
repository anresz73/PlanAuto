#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Created on Fri Feb  4 17:35:09 2022
#
# Arbitrador de Planes vs Capitalización
#
# https://github.com/anresz73/PlanAuto
#

# from .armado_cash_flow import ArmadoCashFlow

from .constants import constants
from .functions import *

class PlanAuto:
    """
    Arbitrador de Planes y Capital
    """
    
    def __init__(self, valor_auto, valor_capital, cash_flow, cuota_pura):
        """
        Class Constructor
        Params:
        ----
        valor_auto : float - precio de lista del auto
        valor_capital : float - valor a capitalizar. Ej. valor de reventa del auto usado
        cash_flow : pd.Series - 
        cuota_pura : float - valor de la "cuota pura" en los planes de ahorro.
        """
        
        self.valor_auto = valor_auto
        self.valor_capital = valor_capital
        self.cash_flow = cash_flow
        self.cuota_pura = cuota_pura
    
    def get_cash_flow(self):
        """
        Llama función cashflow
        """