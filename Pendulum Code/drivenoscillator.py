#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 15:16:29 2019

@author: lucasbaralt
"""

import numpy as np
import matplotlib.pyplot as plt
from rungekutta4 import RK4
from pendulumeqs import pendulum, Parameters

import pendulumplot as pp


parameters = Parameters



m_1 = 0.35
m_2 = 0.80
g = 9.8
L = 0.35
r = 0.05

I = (1/3)*m_1*L**2 + (L+r)**2*m_1

parameters['M'] = m_1 + m_2
parameters['omega_0'] = np.sqrt(((m_1 + m_2)*g*L)/I)

frequency_ratios = np.linspace(0, 5, 26)

parameters['eta'] = 10.0


parameters['omega_d'] = 0.1*np.sqrt(((m_1 + m_2)*g*L)/I)




tmax = 10
N = 1000

times = np.linspace(0, tmax, N)

initial_angle = -np.pi/2
initial_velocity = 0.
y_0 = np.array([initial_angle, initial_velocity])


colors = ['black', 'red', 'blue', 'green', 'orange', 'magenta', 'c', 'y']

plotargs = pp.Plot_Arguments

maxamps = []

for i in range(len(frequency_ratios)):
    parameters['omega_d'] = frequency_ratios[i]*parameters['omega_0']
    yvals = RK4(pendulum, y_0, times, parameters)
    
    
    


