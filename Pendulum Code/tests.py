#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 16:19:12 2019

@author: lucasbaralt
"""

import numpy as np
from rungekutta4 import RK4
from pendulumeqs import pendulum, Parameters, pendulumTorque
import pendulumplot as pp
import matplotlib.pyplot as plt

parameters = Parameters


m_1 = 0.35
m_2 = 0.80
g = 9.8
L = 0.35
r = 0.05

I = (1/3)*m_1*L**2 + (L+r)**2*m_1

parameters['M'] = m_1 + m_2
parameters['omega_0'] = np.sqrt(((m_1 + m_2)*g*L)/I)
parameters['eta'] = 0.
parameters['omega_d'] = parameters['omega_0']
parameters['delta'] = np.pi/3
parameters['kappa'] = 5

tmax = 10
N = 2500

times = np.linspace(0, tmax, N)

initial_angle = -np.pi/10
initial_velocity = 0.
y_0 = np.array([initial_angle, initial_velocity])

colors = ['black', 'red', 'blue', 'green', 'orange', 'magenta', 'c', 'y']

plotargs = pp.Plot_Arguments

plotargs['color'] = 'magenta'
plotargs['title'] = r'Phase Space'
plotargs['xlabel'] = r'Time (s)'
plotargs['ylabel'] = r'Angular Displacement (rad)' 
plotargs['lineshape'] = '-'
plotargs['loc'] = 4

yvals = RK4(pendulum, y_0, times, parameters)

pp.displacementplot(times, yvals, plotargs)

plt.show()

pp.phasespace(times, yvals, plotargs)


