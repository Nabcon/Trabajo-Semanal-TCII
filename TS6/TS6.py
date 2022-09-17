# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 20:36:16 2022

@author: Nahuel
"""

import scipy.signal as sig
import numpy as np
import matplotlib.pyplot as plt

nn = 2
alfa_max = 1 # dB
ee = 10**(alfa_max/10)-1
e = np.sqrt(ee)
wb = e**(1/nn)

# num1 = [(wb**2)/9,0, 1]
# num2 = [0,1]
# den1 = [wb**2, wb*np.sqrt(2), 1]
# den2 = [wb, 1]

num1 = [1,0, 1/9]
num2 = [1,0]
den1 = [1, 1, 1]
den2 = [1, 1]

num1_b = [1,0, 9]
num2_b = [0,1]
den1_b = [1, np.sqrt(2), 1]
den2_b = [1, 1]

num4_1 = [1/9,0, 1]
num4_2 = [1/9,0,1]
den4_1 = [1, np.cos(np.pi/8), 1]
den4_2 = [1, np.cos(np.pi*3/8), 1]

den = np.convolve(den1,den2)
num = np.convolve(num1,num2)

den_b = np.convolve(den1_b,den2_b)
num_b = np.convolve(num1_b,num2_b)

num4 = np.convolve(num4_1, num4_2)
aux4 = np.convolve(den4_1, den4_2)
den4 = np.convolve(aux4,den2)

sys = sig.TransferFunction(num, den) #calculado
sys_b = sig.TransferFunction(num_b, den_b) #calculado

# vector de frencuencia logaritmado
f = np.logspace(-2, 1,10000)

# obtengo la magnitud y fase de las transferencias
w, mag, phase = sig.bode(sys,f)
w_b, mag_b, phase_b = sig.bode(sys_b,f)

fig, (ax1,ax2) = plt.subplots(nrows=2 , ncols=1, sharex=True)
#MODULO
ax1.semilogx(w,mag)
#ax1.semilogx(w_b,mag_b,label='butter')
ax1.grid(True, which="both", ls="--")
ax1.set_title('Magnitude Response')
ax1.set_ylabel('Magnitude[dB]')
# ax1.legend()
# ax1.set_yticks([-80,-60,-40,-20,0])
# ax1.set_ylim([-80,0])
ax1.autoscale(enable=True, axis='x', tight=True)

# FASE
ax2.semilogx(w, phase,color='purple')
#ax2.semilogx(w_b, phase_b,color='blue',label='butter')
ax2.grid(True, which="both", ls="--")
ax2.set_title('Phase Response')
ax2.set_ylabel('Phase[deg]')
# ax2.set_yticks([-270,-225,-180,-135,-90,-45,0])
# # ax2.legend()
# ax2.set_ylim([-275,0])
ax2.autoscale(enable=True, axis='x', tight=True)
# sos_pbanda = tc2.tf2sos_analog(num, den)
# tc2.analyze_sys( sys )