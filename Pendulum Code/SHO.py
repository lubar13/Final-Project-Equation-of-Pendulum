#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 16:07:16 2019

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

parameters['M'] = m_1 + m_2
parameters['omega_0'] = np.sqrt((parameters['M']*g*L_cm)/I)
ratios = np.linspace(0.1, 3, 10)
parameters['omega_d'] = 4.12
parameters['kappa'] = 2*parameters['omega_0']*0
parameters['eta'] = 2
parameters['delta'] = 0


times = np.linspace(0, 75, 75000)

phi_in = np.pi/3

vel_in = 5

alphavals = np.linspace(0.1, 2, 6)

y_0 = np.array([phi_in, vel_in])

yvals = RK4(pendulum, y_0, times, parameters)

smol1 = phi_in*np.cos(parameters['omega_0']*times)


plotargs = pp.Plot_Arguments

colors = ['red', 'blue', 'green', 'orange', 'magenta', 'c'] * 10

plotargs['title'] = r'Displacement for Different Damping Coefficients $\chi$'
plotargs['xlabel'] = 'Time (s)'
plotargs['ylabel'] = 'Angular Displacement (rad)'
plotargs['lineshape'] = '-'
plotargs['loc'] = 1
plotargs['color'] = colors[3]

#plt.plot(times, smol1, '--', color='k', label=r'$\phi = \phi_0\mathrm{cos}(\omega_0t)$')



pp.displacementplot(times, yvals, plotargs)

plt.show()


pp.phasespace(times, yvals, plotargs)