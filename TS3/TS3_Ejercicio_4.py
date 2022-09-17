# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 15:50:00 2022

@author: Nahuel
"""

import scipy.signal as sig
import numpy as np
import matplotlib.pyplot as plt

nn = 4
alfa_max = 1 # dB
e = np.sqrt(10**(alfa_max/10)-1)

wb = 1/(e**(-1/nn))

num = [1, 0, 0, 0, 0]
den = np.convolve([1, 2*np.cos(np.pi/8)*wb, wb**2], [1, 2*np.cos(np.pi*3/8)*wb, wb**2])

sys = sig.TransferFunction(num, den)

f = np.logspace(-1, 1,1000)
w, mag, phase = sig.bode(sys,f)

fig, (ax1,ax2) = plt.subplots(nrows=2 , ncols=1, sharex=True)
#fig.set_size_inches(16,9)
ax1.semilogx(w,mag,label='|T(w)|')
ax1.grid(True)
ax1.set_title('Magnitude Response')
ax1.set_ylabel('Magnitude[dB]')
ax1.set_yticks([-70,-50,-35,-30,-10,-1,0])
ax1.set_ylabel('Magnitude[dB]')
ax1.legend()

ax2.semilogx(w, phase,color='red',label='ang[T(w)]')
ax2.grid(True)
ax2.set_title('Phase Response')
ax2.set_ylabel('Phase[deg]')
ax2.set_xticks([2/7,1])
ax2.set_xticklabels(['$\omega_{NS} = 2/7$','$\omega_{NP} = 1$'])
ax2.legend()
