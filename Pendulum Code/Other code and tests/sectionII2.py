#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 08:59:04 2019

@author: lucasbaralt
"""

import numpy as np
from pendulumeqs import pendulum, Parameters
import matplotlib.pyplot as plt
from rungekutta4 import RK4
import pendulumplot as pp

parameters = Parameters

g = 9.8
m_1 = 0.3
m_2 = 0.7
L = 0.35
r = 0.05

L_cm = ((L/2)*(m_1+m_2) + r*m_2)/(m_1+m_2)


I = (1/3)*m_1*L*L + (L+r)**2*m_2
print(I)

parameters['M'] = m_1 + m_2
print(np.sqrt((4*g*L_cm)/((np.pi**2)/100)))
parameters['omega_0'] = np.sqrt((parameters['M']*g*L_cm)/I)
print(parameters['omega_0'])
ratios = np.linspace(0.1, 3, 10)
parameters['omega_d'] = 4.12
parameters['kappa'] = 2*parameters['omega_0']
parameters['eta'] = 8.24
parameters['delta'] = 0


times = np.linspace(0, 190, 50000)

phi_in = np.pi/7
vel_in = 0

alphavals = np.linspace(0.1, 2, 6)

y_0 = np.array([phi_in, vel_in])
yvals = RK4(pendulum, y_0, times, parameters)

plotargs = pp.Plot_Arguments

colors = ['red', 'blue', 'green', 'orange', 'magenta', 'c'] * 10

plotargs['title'] = r'Displacement for Different Damping Coefficients $\chi$'
plotargs['xlabel'] = 'Time (s)'
plotargs['ylabel'] = 'Angular Displacement (rad)'
plotargs['lineshape'] = '-'
plotargs['loc'] = 1
plotargs['color'] = colors[3]

pp.displacementplot(times, yvals, plotargs)
#plt.rcParams["figure.figsize"] = (30,20)
plt.show()

plotargs['title'] = r'Phase Space$'
plotargs['xlabel'] = 'Angle (rad)'
plotargs['ylabel'] = 'Angular Velocity (rad/s)'
pp.phasespace(times, yvals, plotargs)

'''
parameters['eta'] = 0.
parameters['kappa'] = 0.
y = RK4(pendulum, y_0, times, parameters)
plotargs['color'] = 'b'
pp.displacementplot(times[30000:40000], y[30000:40000], plotargs)

T = 2*np.pi/parameters['omega_0']

whys = [np.transpose(yvals)[0][30000:40000], np.transpose(y)[0][30000:40000]]

periods = []

for j in whys:
    crossings = []
    for i in range(len(j)-1):
          
        if j[i]*j[i+1]<=0 and j[i]>=0:
            t = (times[i+1]+times[i])/2
            print(t)
            crossings.append(t)
    vals  = []
    for k in range(1, len(crossings)):
        diff = crossings[k]-crossings[k-1]
        vals.append(diff)
    period = np.average(vals)
    periods.append(period)

print(T)
print(periods)
'''