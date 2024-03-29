#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 12:22:08 2019

@author: lucasbaralt
"""

import numpy as np
from pendulumeqs import Parameters, pendulumTorque, pendulum
import matplotlib.pyplot as plt
from rungekutta4 import RK4
import pendulumplot as pp

parameters = Parameters

g = 9.8
m_1 = 0.1
m_2 = 0.2
L = 0.2
r = 0.025

L_cm = ((L/2)*(m_1) + (L+r)*m_2)/(m_1+m_2)
print(L_cm)


I = (1/3)*m_1*L*L + (L+r)**2*m_2




parameters['M'] = m_1 + m_2
parameters['omega_0'] = np.sqrt((parameters['M']*g*L_cm)/I)
parameters['kappa'] = 2*parameters['omega_0']*0.013
parameters['omega_d'] = 2*parameters['omega_0']#0.56
parameters['eta'] = 30
T_drive = (2*np.pi)/parameters['omega_d']
print(parameters['omega_0'])
print(parameters['omega_d'], T_drive, T_drive*150, parameters['kappa'])

step = 0.001
lim = 500
num = int(lim/step)

times = np.linspace(0, lim, num + 1)

y_0 = [1.9, -1.3]


etas = np.linspace(0, 92, 375)
velocities = [] 



for i in range(len(etas)):
    parameters['eta'] = etas[i]
    yvals = RK4(pendulumTorque, y_0, times, parameters)
    print(i)
    limit = int(num//2)
    for t in times[limit:]:
        k = int(np.where(times == t)[0])
        
        init = parameters['eta']*np.cos(parameters['omega_d']*times[k-2]
                  +parameters['delta'])*np.sin(yvals[k-1,0])
        
        fin = parameters['eta']*np.cos(parameters['omega_d']*times[k]
                  +parameters['delta'])*np.sin(yvals[k,0])
        if init*fin<=0:
            #print(init, fin)
            vel = np.abs(yvals[k-1, 1])
            #print(vel)
            velocities.append(vel)
    et = [etas[i]] * len(velocities)
    plt.plot(et, velocities, ',', c='salmon')
    plt.xlabel(r'$\eta$', fontsize=12)
    plt.ylabel(r'$|\dot\phi|$', fontsize=12)
    plt.title(r'Bifurcation Diagram for $\omega_d = ${}, $\kappa = {}$'.format(round(parameters['omega_d'], 3),
                                                                               round(parameters['kappa'],3)),
              fontsize=18)
    plt.rcParams["figure.figsize"] = (8,5.33)
    
    velocities = []
           

plt.savefig('birfurcationdiagram.png', dpi=100)

#fig, axs = plt.subplots()

#axs.plot(etas, velocities, '.', color='crimson')
#axs.set_title(r'Bifurcation Diagram for $\dot\phi = {},  \phi = {}, \omega_0 = {}, \omega_d = {}, \kappa = {}$'.format(y_0[1], y_0[0], 
 #             parameters['omega_0'], parameters['omega_d'], parameters['kappa']))

#axs.set_xlabel(r'$\eta$')
#axs.set_ylabel(r'$|\dot\phi(t)|$')
#fig.set_size_inches(8, 5.33)
#fig.savefig('bifurcationdiagram.png', dpi=100)
#plt.show()





