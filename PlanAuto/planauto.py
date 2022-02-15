#!.venv/bin/python3
# -*- coding: utf-8 -*-
#
# Created on Fri Feb  4 17:35:09 2022
#
# Arbitrador de Planes vs Capitalización
#
# https://github.com/anresz73/PlanAuto

# from .armado_cash_flow import ArmadoCashFlow

import pandas as pd
import numpy as np
from itertools import combinations

from .constants import *
from .functions import (
    _generator,
    _capitalizator,
    _random_simulator
)

class PlanAuto:
    """
    Arbitrador de Planes y Capital
    """

    def __init__(
        self, 
        valor_auto = VALOR_AUTO, 
        valor_capital = VALOR_CAPITALIZAR, 
        cash_flow = CASH_FLOW['importe'], 
        clip_rate = MAXIMO_AUMENTO,
        inflacion_mensual = INFLACION_MENSUAL
        ):
        """
        Class Constructor
        Params:
        ----
        valor_auto : float - precio de lista del auto
        valor_capital : float - valor a capitalizar. Ej. valor de reventa del auto usado
        cash_flow : pd.Series - 
        cuota_pura : float - valor de la "cuota pura" en los planes de ahorro.
        clip_rate : float - máximo aumento porcentual de cuota por mes o período
        """
        
        self.valor_auto = valor_auto
        self.valor_capital = valor_capital
        self.cash_flow = cash_flow
        self.clip_rate = clip_rate
        self.inflacion_mensual = inflacion_mensual

    def get_cash_flow(self):
        """
        Arma un cash flow Capitalizando el Capital Inicial a un interés constante o variable,
        descontando los pagos mensuales del plan ajustados a una tasa variable con métodos estocásticos.
        """
        test = _generator(
            payments = self.cash_flow, 
            first_price = self.valor_capital, 
            clip_i = self.clip_rate, 
            simulated_flow = _random_simulator(
                x0 = self.inflacion_mensual, 
                scale = .005, 
                n = len(self.cash_flow)
                )
            )

        capital = _capitalizator(
            ini_capital = self.valor_capital,
            annual_rate = self.inflacion_mensual,
            n_period = 365,
            n_years = 7,
            mid_payments = test[:, 2]
            )
        
        return pd.Series(capital)

    def gbm_simulator(
        self):
        pass

    def monte_carlo_simulator(
        self,
        size = 100
        ):
        """
        Monte Carlo Simulation
        Args:
            size : int - size of each simulation
        """
        result = []
        for e in range(size):
            result.append(self.get_cash_flow())
        return pd.DataFrame(result).T

