#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 19:47:26 2019

@author: lucasbaralt
"""

import numpy as np
from pendulumeqs import pendulum, Parameters
import matplotlib.pyplot as plt
from rungekutta4 import RK4
import pendulumplot as pp

parameters = Parameters

g = 9.8
m_1 = 0.25
m_2 = 0.50
L = 0.35
r = 0.05

L_cm = ((L/2)*(m_1+m_2) + r*m_2)/(m_1+m_2)


I = (1/3)*m_1*L*L + (L+r)**2*m_2


parameters['M'] = m_1 + m_2
parameters['omega_0'] = np.sqrt(parameters['M']*g*L_cm)

times = np.linspace(0, 18, 5000)

initialvals = np.linspace(np.pi/15, np.pi/1.1, 5)
phi_in = np.pi/10
vel_in = 0

y_0 = np.array([phi_in, vel_in])

smol = initialvals[0]*np.cos(parameters['omega_0']*times)

yvals = RK4(pendulum, y_0, times, parameters)


plotargs = pp.Plot_Arguments


T = (2*np.pi)/parameters['omega_0']
colors = ['red', 'blue', 'green', 'orange', 'magenta', 'c']


plotargs['xlabel'] = 'Time (s)'
plotargs['ylabel'] = 'Angular Displacement (rad)'
plotargs['title'] = r'Displacement for $\omega_0 = $ {}, $\dot\phi_0 = 0$, T = {}'.format(str(round(parameters['omega_0'], 3)), str(round(T,3)))
plotargs['loc'] = 4
plotargs['lineshape'] = '-'

for i in range(len(initialvals)):
    y_0 = np.array([initialvals[i], 0])
    plotargs['color'] = colors[i]
    phi = str(round(initialvals[i], 3))
    plotargs['graph label'] = r'$\phi_0 = $' + phi
    yvals = RK4(pendulum, y_0, times, parameters)
    
    pp.displacementplot(times, yvals, plotargs)

plt.plot(times, smol, '--', color='w', label=r'$\phi = \phi_0\mathrm{cos}(\omega_0t)$')
plt.legend(loc=4)

x = np.array([0., T, 2*T, 3*T])

for xval in x:
    plt.axvline(xval, color = 'k', linestyle='--') 

plt.show()


### Determine convergence of the period


times = np.linspace(0, 20, 1000)
comparisons = 100
initialvals = np.linspace(np.pi/100, np.pi/1.1, comparisons)

periods = []
periodsarr = np.array(periods)
for i in range(len(initialvals)):
    y_0 = np.array([initialvals[i], 0])
    yvals = RK4(pendulum, y_0, times, parameters)
    ys = np.transpose(yvals)[0]
    crossings = []
    for j in range(len(ys)-1):
        if ys[j]*ys[j+1]<=0 and ys[j]>=0:
            t = (times[j+1]+times[j])/2
            crossings.append(t)
    period = crossings[1]-crossings[0]
    periods.append(period)
print(periods)

errors = []
for t in periods:
    err = t - T
    errors.append(err)

print(errors)


plt.plot(initialvals, periods, '-.', color = 'c')
plt.axhline(T, color = 'k', linestyle = '--')
plt.show()

plt.plot(initialvals, errors, '-.', color = 'green')

    
            
