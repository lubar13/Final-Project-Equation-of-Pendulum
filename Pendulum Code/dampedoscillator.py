#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 17:04:07 2019

@author: lucasbaralt
"""

import numpy as np
import matplotlib.pyplot as plt
from rungekutta4 import RK4
from pendulumeqs import pendulum, Parameters

import pendulumplot as pp


parameters = Parameters

'''

In this file I will consider the motion of a damped pendulum, for which there 
is no external torque acting on it. I will consider the three cases of 
an underdamped, overdamped, and critically damped system. The pendulum will consist 
of a thin pole of length L and mass m_1, so that I_1 = (1/3)*m_1*L^2, with a 
spherical mass m_2 of radius r attached at the end, so that the total moment of 
inertia I = (1/3)*m_1*L^2 + (L+r)^2*m_2. 

'''


### ===============================================================================
### Underdamped pendulum (chi < 1). We expect the oscillation of the pendulum 
### to decrease exponentially while still oscillating. This behavior of oscillators
### is relevant in particular in electronics, where oscillations on the output 
### of a step signal is usually unwanted. 
### ===============================================================================


alphavals = np.linspace(0.1, 1, 6)

m_1 = 0.35
m_2 = 0.80
g = 9.8
L = 0.35
r = 0.05

I = (1/3)*m_1*L**2 + (L+r)**2*m_1

parameters['M'] = m_1 + m_2
parameters['omega_0'] = np.sqrt(((m_1 + m_2)*g*L)/I)
parameters['eta'] = 0.

tmax = 10
N = 100000

times = np.linspace(0, tmax, N)

initial_angle = -np.pi/10
initial_velocity = 0.
y_0 = np.array([initial_angle, initial_velocity])

colors = ['black', 'red', 'blue', 'green', 'orange', 'magenta', 'c', 'y']

plotargs = pp.Plot_Arguments


plotargs['title'] = r'Displacements for different damping coefficients $\chi$'
plotargs['xlabel'] = r'Time (s)'
plotargs['ylabel'] = r'Angular Displacement (rad)' 
plotargs['lineshape'] = '-'
plotargs['loc'] = 4

for i in range(len(alphavals)):
    parameters['alpha'] = alphavals[i]
    parameters['kappa'] = parameters['alpha']*(2*parameters['M']*parameters['omega_0'])
    chi = str(round(parameters['alpha'], 2))
    plotargs['color'] = colors[i]
    plotargs['graph label'] = r'$\chi =$ '+ chi 
    yvals = RK4(pendulum, y_0, times, parameters)
    pp.displacementplot(times, yvals, plotargs)


plt.figure(figsize=(2,2))
plt.show()  



plotargs['title'] = r'Phase Space for Different Damping Coefficients $\chi$'
plotargs['xlabel'] = r'$\phi$ (rad)'
plotargs['ylabel'] = r'$\dot\phi$ (rad/s)'
plotargs['loc'] = 1


for i in range(len(alphavals)):
    parameters['alpha'] = alphavals[i]
    parameters['kappa'] = parameters['alpha']*(2*parameters['M']*parameters['omega_0'])
    chi = str(round(parameters['alpha'], 2))
    plotargs['color'] = colors[i]
    plotargs['graph label'] = r'$\chi =$ '+ chi 
    yvals = RK4(pendulum, y_0, times, parameters)
    pp.phasespace(times, yvals, plotargs)
    plt.figure(figsize=(2,2))

    plt.show()
    


'''
overdamped = np.linspace(1, 5, 6)

for j in range(len(overdamped)):
    parameters['alpha'] = overdamped[j]
    parameters['kappa'] = parameters['alpha']*(2*parameters['M']*parameters['omega_0'])
    chi = str(round(parameters['alpha'], 2))
    plotargs['color'] = colors[j]
    plotargs['graph label'] = r'$\chi =$ ' + chi
    yvals = RK4(pendulum, y_0, times, parameters)
    pp.displacementplot(times, yvals, plotargs)
    
plt.figure(figsize=(2,2))
plt.show()


'''















