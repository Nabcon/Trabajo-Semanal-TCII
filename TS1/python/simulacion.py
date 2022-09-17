# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 22:00:41 2022

@author: Nahuel
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as sig
from splane import pretty_print_lti, analyze_sys


all_sos = []
valores_k = [0.5 , 1 , 1.5]

#definicion de los polinomios

for k in valores_k:
        
    num = np.array([1,-k])
    den = np.array([1,1])
    
    my_sos = sig.TransferFunction(num,den)
    
    pretty_print_lti(my_sos)

    all_sos += [my_sos]
    
plt.close('all')
analyze_sys(all_sos, sys_name=valores_k)
  
