import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt

# Variables
a = 10**(15/20)
wb = 0.7133

# Numerador y denominador de la transferencia
num = [a,0,0];
den = [1, np.sqrt(2)*wb, wb**2]; 

sys = sig.TransferFunction(num, den)
f = np.logspace(-2, 1,10000)
w, mag, phase = sig.bode(sys,f)
grpdelay = sig.group_delay((num,den),w)

# PLOTEOS
fig, ax = plt.subplots(nrows=3 , ncols=1, sharex=True,constrained_layout=True)
fig.set_size_inches(10,6)
plt.xlabel('$\omega$')

# Plot Transferencia
ax[0].semilogx(w,mag,label='|T($\omega$)|',linewidth=3)
ax[0].grid(True)
ax[0].set_title('Modulo de Transferencia')
ax[0].set_ylabel('Magnitud[dB]')
ax[0].set_yticks([-60,-40,-20,-10,5,10,15])
ax[0].set_yticklabels(['-60','-40','-20','-10','5','10','15'])
ax[0].legend()

# Plot Fase
ax[1].semilogx(w, phase,label='$\phi$($\omega$)',linewidth=3)
ax[1].grid(True)
ax[1].set_title('Fase de Transferencia')
ax[1].set_ylabel('Fase')
ax[1].set_yticks([0,45,90,135,180])
ax[1].set_yticklabels(['0','$\pi/4$','$\pi/2$','$3\pi/4$','$\pi$'])
ax[1].legend()

# Plot Retardo de Grupo
ax[2].semilogx(w,grpdelay,label='tau($\omega$)',linewidth=3)
ax[2].grid(True)
ax[2].set_title('Retardo de Grupo')
ax[2].set_ylabel('Delay')
ax[2].set_xticks([41/110,0.7133,1,2,3])
ax[2].set_xticklabels(['$\omega_S$','$\omega_B$','$\omega_P$','2','3'])
ax[2].legend()

# Usar para visual studio. Poner run python file NO run CODE
##plt.savefig('fig.png',dpi=300)
##plt.show()
