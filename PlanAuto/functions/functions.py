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

#from ..constants import *

import pandas as pd
import numpy as np

def gen_cash_flow(file_name):
    """
    Generates Cash Flow from libreoffice file
    """
    data = pd.read_excel(io = file_name,
                         sheet_name = 0,
                         engine = 'odf',
                         dtype = {'cuotanro' : np.int32, 'importe' : np.float32})
    return data

###
#   Rate Simulators / Generators
###

def _random_simulator(x0, scale, n):
    """
    Generates a random interest rate
    """
    if isinstance(x0, (int, float)) and isinstance(n, int):
        return np.random.normal(loc = x0, scale = scale, size = n)
    elif isinstance(x0, (list, np.ndarray)):
        return np.random.normal(loc = x0, scale = scale, size = (n, len(x0))).transpose().ravel()

def _gbm_simulator(mu, sigma, n, x0, dt = .1):
    """
    Geometric Brownian Motion generator.
    mu : float - mean of data return / list - return appended simulation with mu's'
    sigma : float - standard deviation of data return
    n : int - sample size
    x0 : float - initial rate
    """
    if isinstance(mu, float):
        x = np.exp(
                   (mu - sigma ** 2 / 2.) * dt
                   + sigma * np.random.normal(0, np.sqrt(dt), size = (1, n)).T
        )
        x = np.vstack([[1.], x])
        x = x0 * x.cumprod(axis = 0)
        return x
    elif isinstance(mu, (list, np.ndarray)):
        for mu_i in mu:
            try:
                x0 = result[-1].item()
            except NameError:
                x0 = x0
                result = [x0]
            result = np.append(result, 
                               _gbm_simulator(mu = mu_i, sigma = sigma, n = n, x0 = x0)[1:])
            #result.append(_gbm(mu = mu_i, sigma = sigma, n = n, x0 = x0))
        return result

def _generator(df):
    """
    generates DataFrame with Projected Payments
    """
    

###
# Aux Functions
###

def _clip(data, lim):
    """
    Clip edges in given data.
    data 
    lim
    """
    

def inst_to_ann(r):
    """
    Converts short rate to an annualized rate
    """
    #return np.exp(r)-1
    return np.expm1(r)

def ann_to_inst(r):
    """
    Converts annualized to a short rate
    """
    return np.log1p(r)

def gbm_alt(mu = .07,
            sigma = [.15],
            n = 50,
            dt = 0.1,
            x0 = 100,
            random_seed = 1,
            plot = False):
    """
    GBM Alternative
    """
    if random_seed is not None:
        np.random.seed(random_seed)
    
    if not sigma:
        sigma = np.arange(0.8, 2, 0.2)
    else:
        sigma = np.array(sigma)
    
    x = np.exp(
               (mu - sigma ** 2 / 2.) * dt
               + sigma * np.random.normal(0, np.sqrt(dt), size = (len(sigma), n)).T
    )
    x = np.vstack([np.ones(len(sigma)), x])
    x = x0 * x.cumprod(axis = 0)
    
    if not plot:
        return pd.DataFrame(x)
    else:
        plt.plot(x)
        plt.legend(np.round(sigma, 2))
        plt.xlabel("$t$")
        plt.ylabel("$x$")
        plt.title("Realizations of Geometric Brownian Motion with different variances\n $\mu=1$")
        plt.show()

def cir(n_years = 10,
        n_scenarios = 1,
        a = 0.05,
        b = 0.03,
        sigma = 0.05,
        steps_per_year = 12,
        r_0 = None):
    """
    Generates a random interest rate evolution over time using CIR model
    b and r_0 are assumed to be the annualized rates, not the short rate
    and the returned values are the annualized rates as well
    """
    if r_0 is None:
        r_0 = b
    r_0 = ann_to_inst(r_0)
    # For small interest rates not very different ann and short
    dt = 1   / steps_per_year
    num_steps = int(n_years * steps_per_year) + 1  #Because n_years mught be a float
    
    shock = np.random.normal(0, scale = np.sqrt(dt), size = (num_steps, n_scenarios))
    rates = np.empty_like(shock)
    rates[0] = r_0
    
    ## For price generation
    h = np.sqrt(a ** 2 + 2 * sigma ** 2)
    prices = np.empty_like(shock)
    ####
    
    def price(ttm, r):
        _A = ((2 * h * np.exp((h + a) * ttm / 2)) / (2 * h + (h + a) * (np.exp(h * ttm) - 1))) ** (2 * a * b / sigma ** 2)
        _B = (2 * (np.exp(h * ttm) - 1)) / (2 * h + (h + a) * (np.exp(h * ttm) - 1))
        _P = _A * np.exp(-_B  * r)
        return _P
    prices[0] = price(n_years, r_0)
    ####
    
    for step in range(1, num_steps):
        r_t = rates[step - 1]
        d_r_t = a * (b - r_t) * dt + sigma * np.sqrt(r_t) * shock[step]
        rates[step] = abs(r_t + d_r_t)
        # Generate prices at time as well
        prices[step] = price(n_years - step * dt, rates[step])
        
    rates = pd.DataFrame(data = inst_to_ann(rates), index = range(num_steps))
    ### For prices
    prices = pd.DataFrame(data = prices, index = range(num_steps))
    ###
    return rates, prices