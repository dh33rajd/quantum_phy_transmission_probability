# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 00:20:50 2022

@author: HP
"""

import numpy as np
import cmath
hb=1.054*pow(10,-34)
mass=9.1*pow(10,-31)
E=float(input("Enter the energy of the wave (in 10^-34): "))
E=E*pow(10,-34)
k1=np.sqrt(2.0*mass*E)/hb
U=float(input("Enter the energy of the barrier (in 10^-34): "))
U=U*pow(10,-34)
if U > E:
    alpha=np.sqrt(2.0*mass*(U-E))/hb
    length=float(input("value of length in 10^-9: "))
    length=length*pow(10,-9)
    a1=pow(2.303,-1*alpha*length)
    a2=pow(2.303,alpha*length)

    a3=pow(2.303,complex(0,-1*k1*length))
    A = np.array([[1, -1, -1, 0], [0, a1, a2, -a3], [complex(0,1*k1), -1*alpha, alpha, 0], [0, -1*alpha*a1,alpha*a2, complex(0,-1*k1*a3)]])
    b = np.array([-1, 0, complex(0,1)*k1, 0])
    x = np.linalg.solve(A, b)
    f=x[len(x)-1]
    z=f.real
    y=f.imag
    prob=np.sqrt(pow(z,2)+pow(y,2))
    print("transmission probability is "+str(prob))
else:
    print("Energy of Barrier less than wave")