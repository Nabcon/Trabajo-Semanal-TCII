# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 20:36:07 2022

@author: Nahuel
"""

import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt

k = 2.27445
w1 = 1
w2 = 1.107
w3 = 0.90297
Q1 = 7.981
Q2 = 16.05

alfa_max = 0.5

ee = 10**(alfa_max/10)-1
e = np.sqrt(ee)

a2 = k**3*(1/Q1)*(w2/Q2)*(w3/Q2) 
a = 1/((5**3)*4*e)


p1 = [1, w1/Q1, w1**2]
p2 = [1, w2/Q2, w2**2]
p3 = [1, w3/Q2, w3**2]

# p1 = [1, 0.1253, 1]
# p2 = [1, 0.0690175, 1.22646]
# p3 = [1, 0.0562738, 0.815356]

aux = np.convolve(p1, p2)
den = np.convolve(aux, p3)
num = [a, 0, 0, 0]

sys = sig.TransferFunction(num, den)
f = np.logspace(-2, 2,10000)
w, mag, phase = sig.bode(sys,f)

fig, (ax1,ax2) = plt.subplots(nrows=2 , ncols=1, sharex=True)
ax1.semilogx(w,mag,label='|T(w)|')
ax1.grid(True)
ax1.set_title('Magnitude Response')
ax1.set_ylabel('Magnitude[dB]')
ax1.legend()

ax2.semilogx(w, phase,color='red',label='ang[T(w)]')
ax2.grid(True)
ax2.set_title('Phase Response')
ax2.set_ylabel('Phase[deg]')
ax2.legend()