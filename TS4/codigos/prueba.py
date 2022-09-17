#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 23:14:49 2019

@author: mariano
"""

import numpy as np
import scipy.signal as sig
from splane import analyze_sys


# # ejemplo simple
# wo = 1
# qq = np.sqrt(2)/2 

# num = np.array([wo**2]) 
# den = np.array([1, wo/qq, wo**2])

a = 10**(15/20)
wb = 0.7133

# Numerador y denominador de la transferencia
num = [a,0,0];
den = [1, np.sqrt(2)*wb, wb**2];


mi_sos = sig.TransferFunction(num,den)
    
analyze_sys(mi_sos, 'mi SOS')


