# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 20:51:06 2022

@author: Nahuel
"""

import sympy as sp
import splane as tc2
from schemdraw import Drawing
from schemdraw.elements import  Capacitor, Inductor, Resistor

# Resolución simbólica

RL = 1

s = sp.symbols('s ', complex=True)

# Sea la siguiente función de excitación
ZZ = 2*(s**2 + 0.5)/(s**3+2*s)
ZZ = (2*s**2+1)/(s**3+2*s)

# Restricción circuital: L2*C2 = 1 r/s
# remoción parcial en infinito de 1/YY

omega_LC = 3

Y2, Yc3 = tc2.remover_polo_infinito(1/ZZ, omega_zero = omega_LC )

# Yc1 es la admitancia removida
# extraigo C1
C3= Yc3/s

Z4, Zt2, L2, C2 = tc2.remover_polo_jw(1/Y2, omega = omega_LC , isImpedance = True)


Z6, C1 = tc2.remover_polo_dc(Z4)


# # Dibujamos la red resultante:
    
# d = Drawing(unit=4)  # unit=2 makes elements have shorter than normal leads

# d = tc2.dibujar_puerto_entrada(d,
#                         voltage_lbl = ('+', '$V$', '-'), 
#                         current_lbl = '$I$')

# d, zz_lbl = tc2.dibujar_funcion_exc_abajo(d, 
#                                           'Z',  
#                                           ZZ, 
#                                           hacia_salida = True,
#                                           k_gap_width = 0.5)

# d = tc2.dibujar_elemento_serie(d, Capacitor, C1)
# d = tc2.dibujar_espacio_derivacion(d)

# d = tc2.dibujar_tanque_serie(d, L2, C2)

# d = tc2.dibujar_espacio_derivacion(d)

# d = tc2.dibujar_elemento_derivacion(d, Capacitor, C3)

# d = tc2.dibujar_espacio_derivacion(d)

# d = tc2.dibujar_elemento_derivacion(d, Resistor, RL)

# display(d)