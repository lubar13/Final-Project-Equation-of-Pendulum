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
parameters['omega_0'] = 1 #np.sqrt((parameters['M']*g*L_cm)/I)
parameters['kappa'] = 0.1
parameters['omega_d'] = 2
parameters['eta'] = 30
T_drive = (2*np.pi)/parameters['omega_d']
print(parameters['omega_0'])
print(parameters['omega_d'], T_drive, T_drive*150, parameters['kappa'])

transtime = 150
#when cos term is zero
initialdrivetime = (transtime*np.arccos(0) + np.pi/2)/transtime*parameters['omega_d']
numoftimes = 100000

times = np.linspace(0, 500, 150000)
y_0 = [1., 1.]

yvals = RK4(pendulumTorque, y_0, times, parameters)
plotargs = pp.Plot_Arguments

plotargs['color'] = 'royalblue'
plotargs['lineshape'] = '-'

#pp.displacementplot(times, yvals, plotargs)

etas = np.linspace(0, 5, 1000)
velocities = [] 

#def bifurcation()


for i in range(len(etas)):
    tol = 0.0006
    parameters['eta'] = etas[i]
    yvals = RK4(pendulumTorque, y_0, times, parameters)
    l = 1
    limit = int(numoftimes/2)
    for t in times[limit:]:
        k = np.where(times == t)
        #print(k)
        if np.abs(parameters['eta']*np.cos(parameters['omega_d']*t
                  +parameters['delta'])*np.sin(yvals[k,0])) <= tol:
            vel = np.abs(yvals[k, 1][0][0])
            velocities.append(vel)
            break
            #plt.plot(etas[i], vel, ',', color='crimson')
        #l += 1    
        #if l == 150:
        #    break
print(etas)
print(velocities)

fig, axs = plt.subplots()

axs.plot(etas, velocities, ',', color='crimson')
axs.set_title(r'Bifurcation Diagram for $\dot\phi = {},  \phi = {}, \omega_0 = {}, \omega_d = {}, \kappa = {}$'.format(y_0[1], y_0[0], 
              parameters['omega_0'], parameters['omega_d'], parameters['kappa']))

axs.set_xlabel(r'$\eta$')
axs.set_ylabel(r'$|\dot\phi(t)|$')
fig.set_size_inches(8, 5.33)
fig.savefig('bifurcationdiagram.png', dpi=100)
plt.show()





