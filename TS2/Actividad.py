# -*- coding: utf-8 -*-
"""
Created on Sun May  8 16:15:13 2022

@author: Nahuel
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as sig
from splane import analyze_sys

R1 = 1e3
R2 = 30e3
R3 = 10e3
C  = 100e-9
     
num = np.array([0,0,-1/(R1*R3*C**2)])
den = np.array([1,1/(R2*C),1/((R3**2)*(C**2))])

my_sos = sig.TransferFunction(num,den)
    

plt.close('all')
analyze_sys(my_sos, sys_name=1)
  