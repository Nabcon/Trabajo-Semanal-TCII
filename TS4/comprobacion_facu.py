# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 09:56:25 2022

@author: alumno
"""

import scipy.signal as sig
import numpy as np
import matplotlib.pyplot as plt
import splane as tc2

nn = 4 # orden
alfa_max = 1 # dB

eps = np.sqrt(10**(alfa_max/10)-1)

Q = 20/9
p_bp = [1, 1/Q, (2*Q**2+1)/Q**2, 1/Q, 1]
num = [10**0.5/Q**3, 0, 0, 0]
den = np.convolve([1, 1/Q, 1], p_bp)



z,p,k = sig.cheb1ap(nn, alfa_max)
num_lp, den_lp = sig.zpk2tf(z,p,k)


num_bp, den_bp = sig.lp2hp(num_lp, den_lp)

sys = sig.TransferFunction(num_bp, den_bp)

f = np.logspace(-2, 2,10000)
w, mag, phase = sig.bode(sys,f)



group_delay_diff = -np.diff(phase) / np.diff(w)
group_d = np.append(group_delay_diff[0],group_delay_diff)


fig, (ax1,ax2) = plt.subplots(nrows=2 , ncols=1, sharex=True)
ax1.plot(w,group_d*(w[1]))
# ax1.semilogx(w,mag,label='|T(w)|')
ax1.grid(True)
ax1.set_title('Magnitude Response')
ax1.set_ylabel('Magnitude[dB]')
ax1.legend()

# # ax2.semilogx(w, phase,color='red',label='ang[T(w)]')
# # ax2.grid(True)
# # ax2.set_title('Phase Response')
# # ax2.set_ylabel('Phase[deg]')
# # ax2.legend()

sos_pbanda = tc2.tf2sos_analog(num_bp, den_bp)
tc2.analyze_sys( sos_pbanda )