# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 18:27:12 2022

@author: Nahuel
"""

import scipy.signal as sig
import numpy as np
import matplotlib.pyplot as plt

num = [1,-np.sqrt(2)*0.5, 0.25]
den = [1, np.sqrt(2)*0.5, 0.25]

sys = sig.TransferFunction(num, den) #calculado

# vector de frencuencia logaritmado
f = np.logspace(-2, 2,10000)

# obtengo la magnitud y fase de las transferencias
w, mag, phase = sig.bode(sys,f)

fig, (ax1,ax2) = plt.subplots(nrows=2 , ncols=1, sharex=True)
#MODULO
ax1.semilogx(w,mag,label='calculado')
ax1.grid(True)
ax1.set_title('Magnitude Response')
ax1.set_ylabel('Magnitude[dB]')
ax1.legend()
ax1.set_ylim([-1,1])

# FASE
ax2.semilogx(w, phase,color='purple',label='calculado')
ax2.grid(True)
ax2.set_title('Phase Response')
ax2.set_ylabel('Phase[deg]')
ax2.legend()
ax2.set_yticks([-360,-270,-180,-90,0])
ax2.set_yticklabels(['$-2\pi$','$\dfrac{-3}{2}\pi$','$\pi$','$\dfrac{-1}{2}\pi$','0'])
# ax2.set_ylim([-180,30])

# sos_pbanda = tc2.tf2sos_analog(num, den)
# tc2.analyze_sys( sys )