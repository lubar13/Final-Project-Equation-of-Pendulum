#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 18:04:41 2019

@author: lucasbaralt
"""

import numpy as np
import matplotlib.pyplot as plt
from rungekutta4 import RK4
from pendulumeqs import pendulum, Parameters

import pendulumplot as pp




observables = Parameters

g = 9.8 #[m/s^2]
l = 1. #[m]
observables['M'] = 3. #[kg]
I = (1/3)*observables['M']*l*l
observables['kappa'] = 0.
observables['eta'] = 0.
observables['omega_0'] = np.sqrt((observables['M']*g*l)/I)

N = 500
times = np.linspace(0., 10., N+1)


phi_0 = np.pi/1.1

phidot_0 = 0.


initial_conditions = np.array([phi_0, phidot_0])

yvals = RK4(pendulum, initial_conditions, times, observables)





plt.plot(times, yvals[:,0], '-', c='r', label='Calculated Angular Displacement')

plt.legend(loc=2)
plt.title('Time Evolution of Simple Harmonic Pendulum')
plt.xlabel('Time(s)')
plt.ylabel('Angle (rad)')

plt.show()

plotargs = pp.Plot_Arguments

plotargs['color'] = 'orange'
plotargs['lineshape'] = '-'
plotargs['title'] = 'Phase Space'
plotargs['xlabel'] = r'$\phi(t)$ (rad)'
plotargs['ylabel'] = r'$\dot\phi(t)$ (rad $s^{-1}$)'
plotargs['graph label'] = None
plotargs['legend'] = None




pp.phasespace(times, yvals, plotargs)

plt.show()


plotargs['color'] = 'magenta'
plotargs['lineshape'] = '-'
plotargs['title'] = 'Spectrum'
plotargs['xlabel'] = r'$\omega$ (rad $s^{-1}$)'
plotargs['ylabel'] = 'Relative Power'
plotargs['graph label'] = None
plotargs['legend'] = None

pp.frequencyspectrum(times, yvals, plotargs)








