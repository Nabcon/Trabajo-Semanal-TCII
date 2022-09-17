# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 16:09:37 2022

@author: Nahuel

Matriz Admitancia Indefinida (MAI)
----------------------------------
Ejemplos de cálculo simbólico mediante MAI de una red T puenteada de R constante.

Referencias:
------------
Cap. 9. Avendaño L. Sistemas electrónicos Analógicos: Un enfoque matricial.
"""

import sympy as sp
from splane import print_latex, calc_MAI_impedance_ij, calc_MAI_vtransf_ij_mn, calc_MAI_ztransf_ij_mn


# explicación:
'''    
Cirucito
        
    0---------YL1---1--YL3---2
                    |       |
                   YC2      G
                    |       |
    3---------------+--------
    
'''    

YL1, YL3, YC2, = sp.symbols('YL1 YL3 YC2', complex=True)
G = sp.symbols('G', real=True, positive=True)

# Armo la MAI

#               Nodos: 0      1        2        3
Ymai = sp.Matrix([  
                    [  YL1 ,     -YL1     ,    0    ,    0   ],
                    [ -YL1 ,  YL1+YC2+YL3 ,  -YL3   ,  -YC2  ],
                    [   0  ,     -YL3     ,  G+YL3  ,   -G   ],
                    [   0  ,     -YC2     ,   -G    ,  G+YC2 ]
                 ])

# con_detalles = False
con_detalles = True

# Calculo la Z en el puerto de entrada a partir de la MAI
Zmai = calc_MAI_impedance_ij(Ymai, 0, 1, verbose=con_detalles)

print('Transferencia de tensión:')
Vmai = calc_MAI_vtransf_ij_mn(Ymai, 2, 3, 0, 3, verbose=con_detalles)
# Vmai = sp.simplify(Vmai.subs(Ya*Yb, G**2))
# Vmai_Ya = sp.simplify(Vmai.subs(Yb, G**2/Ya))
# Vmai_Yb = sp.simplify(Vmai.subs(Ya, G**2/Yb))

# print_latex( r'T^{{ {:d}{:d} }}_{{ {:d}{:d} }} = '.format(3, 1, 0, 1) +  sp.latex(Vmai_Ya) + ' = ' + sp.latex(Vmai_Yb) )
