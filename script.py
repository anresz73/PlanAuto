"""
Created on Thu Feb  3 16:07:25 2022

@author: anresz73
"""

## PlanAuto
# Arbitrador de un plan con Capital Amortizado de alguna manera

# Libs
import pandas as pd, numpy as np

#Import Data
data_file = r'./Data/data.ods'
data = pd.read_excel(io = data_file,
                     sheet_name = 0,
                     engine = 'odf',
                     dtype = {'cuotanro' : np.int32, 'importe' : np.float32})

#Datos
valor_auto = 2400000.
valor_capitalizar = 1200000.
valor_cuotas = data['importe'].sum()

#Salida
print(f'El valor total de las cuotas es {valor_cuotas}.')
print(f'El valor del auto es {valor_auto}.')
print(f'El valor a capitalizar es {valor_capitalizar}.')