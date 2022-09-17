# -*- coding: utf-8 -*-
"""
Created on Sun May  8 23:14:15 2022

@author: Nahuel
"""

from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
from pylab import *


# R1 = 1e3
# R2 = 30e3
# R3 = 10e3
# C  = 100e-9

# # num = np.array([0,0,-1/(R1*R3*C**2)])
# # den = np.array([1,1/(R2*C),1/((R3**2)*(C**2))])


R1 = 1e3
R2 = 10e3
R3 = 10e3
C  = 100e-9

num = np.array([0.0001,-(10)/(R2*C),0.0001])
den = np.array([1,1/(R2*C),1/((R3**2)*(C**2))])

sys = signal.TransferFunction(num, den)

f = logspace(0, 5)
w = 2 * pi * f

w, mag, phase = signal.bode(sys,w)


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
ax2.set_label('labeeee')
ax2.legend()


plt.xlabel('Angula frequency [rad/sec]')
