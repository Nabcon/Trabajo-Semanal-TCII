# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 09:56:25 2022

@author: alumno
"""

import scipy.signal as sig
import numpy as np
import matplotlib.pyplot as plt


nn = 3 # orden
alfa_max = 1 # dB

eps = np.sqrt(10**(alfa_max/10)-1)

z,p,k = sig.cheb1ap(nn, alfa_max)
num, den = sig.zpk2tf(z,p,k)
num_bp, den_bp = sig.lp2bp(num,den)

#tc2.pretty_print_lti(num_pb, den_pb)

sys = sig.TransferFunction(num_bp, den_bp)
f = np.logspace(-2,2,1000)
w, mag_bp, phase = sig.bode(sys,f)
fig, (ax1,ax2) = plt.subplots(nrows=2 , ncols=1, sharex=True)
ax1.semilogx(w,mag_bp,label='|T_lp(w)|')
ax1.grid(True)
ax1.set_title('Magnitude Response')
ax1.set_ylabel('Magnitude[dB]')
ax1.legend()

ax2.semilogx(w, phase,label='ang[T(w)]')
ax2.grid(True)
ax2.set_title('Phase Response')
ax2.set_ylabel('Phase[deg]')
ax2.set_label('labeeee')
ax2.legend()
