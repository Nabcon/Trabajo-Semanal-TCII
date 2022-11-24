# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 19:21:26 2022

@author: Nahuel
"""

import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt


# DATOS

alfa_max = 1


# Calculo de parametros para equivalente pasabajo
ee = 10**(alfa_max/10)-1

e = np.sqrt(ee)


# Elijo el n que cumpla ambas condiciones --> n = 3

# Calculo de las raices
A = ee*64

# num = ([1, 0, 2, 0, 1.25, 0, 0.25, 0, (ee)/A])
# den = ([1, 0, 2, 0, 1.25, 0, 0.25, 0, (ee+1)/A])


num = np.roots([1, 0, 2, 0, 1.25, 0, 0.25, 0, (ee)/A])
den = np.roots([1, 0, 2, 0, 1.25, 0, 0.25, 0, (ee+1)/A])



# num[8] = (ee+1)/A - 1/A


r1_num = np.append(num[6], num[7])
r2_num = np.append(num[0], num[1])
rt_num = np.append(r1_num,r2_num)

r1_den = np.append(den[4], den[5])
r2_den = np.append(den[0], den[1])
rt_den = np.append(r1_den,r2_den)

p1_num = np.poly(r1_num)
p2_num = np.poly(r2_num)

p1_den = np.poly(r1_den)
p2_den = np.poly(r2_den)

num_s11 = np.poly(rt_num)
den_s11 = np.poly(rt_den)

num_s11[1] = 0
num_s11[3] = 0
##
#       1  +  S11
# Z1 = -----------
#       1  -  S11
##
## si no usas el copy, ambas variables quedan vinculadas y se modifican al mismo tiempo
Z1_num = den_s11.copy() + num_s11.copy()
Z1_den = den_s11.copy() - num_s11.copy()

#%%

A = np.arcsinh(1/e)/(4)


k = np.arange(4) +1

Real_polo = -np.sinh(A)*np.sin((2*k - 1)*np.pi/(2*4))

Imag_polo = np.cosh(A)*np.cos((2*k - 1)*np.pi/(2*4))

den_ch = Real_polo + 1j*Imag_polo

#%%



A = np.roots([1, 0, 3, 0, 3,0, 1])


A = np.roots([1,3,3,1])
