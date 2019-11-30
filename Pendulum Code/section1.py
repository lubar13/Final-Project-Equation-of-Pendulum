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



'''

In this section I will explore the behavior for a pendulum for which 
the small angle approximation holds. I will be using the modules I have 
created elsewhere in order to decrease the run time.


'''

### =======================================================================
### Define the parameters for the natural frequency of the pendulum, 
### and for the pendulum equation.
### =======================================================================

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
print(parameters['M'])
parameters['omega_0'] = np.sqrt((parameters['M']*g*L_cm)/I)
print(parameters['omega_0'])

### ======================================================================
### Create a time interval and some initial conditions.
### ======================================================================

times = np.linspace(0, 5, 20000)
initialvals = np.linspace(np.pi/15, np.pi/1.1, 3)
phi_in = np.pi/20
vel_in = 0
y_0 = np.array([phi_in, vel_in])
### Define a period for later use
T = (2*np.pi)/parameters['omega_0']

### ======================================================================
### In order to test the small angle approximation, we shall compare it 
### to the analytical solution that this approximation yields. 
### ======================================================================

smol = phi_in*np.cos(parameters['omega_0']*times)

### ======================================================================
### Calculate the numerical solution with the Runge-Kutta method.
### ======================================================================

yvals = RK4(pendulum, y_0, times, parameters)


### ======================================================================
### Plot the numerical and analytical solution to compare.
### ======================================================================

plotargs = pp.Plot_Arguments

colors = ['orange', 'red', 'coral', 'maroon', 'crimson', 'blueviolet', 'darkslategrey', 'royalblue'
          'darkgreen', 'crimson', 'maroon', 'greenyellow', 'coral', 'orangered', 'turquoise',
          'salmon']

plotargs['xlabel'] = 'Time (s)'
plotargs['ylabel'] = 'Angular Displacement (rad)'
plotargs['title'] = r'Displacement for $\omega_0 = $ {} rad/s, $\dot\phi_0 = 0, \phi_0 = {}$ rad'.format(str(round(parameters['omega_0'], 3)), str(round(phi_in, 3)))
plotargs['loc'] = 4
plotargs['lineshape'] = '-'
plotargs['color'] = colors[0]
plotargs['graph label'] = r'$\ddot\phi(t) = \omega_0^2$sin$(\omega_0 t)$'
plotargs['titlesize'] = 18
plotargs['labelsize'] = 12


pp.displacementplot(times, yvals, plotargs)
plt.plot(times, smol, '--', c='k', label=r'$\phi(t) = $ cos$(\omega_0 t)$')
plt.legend(loc=1)

plt.rcParams["figure.figsize"] = (8,5.33)

plt.savefig('numerical_vs_analytical_soln.png', dpi=100)
plt.show()

### ======================================================================
### Now we will plot the numerical solution for a damped pendulum, 
### using different damping coefficients. Due to the way I've defined 
### the equation in the pendulumeqs.py file, I will use the variable 
### alpha as chi, but will label that parameter as chi in the real plot.
### ======================================================================


alphavals = [0.15, 1.00, 1.85]

plotargs['title'] = r'Displacement for Different Damping Coefficients $\chi$'
plotargs['xlabel'] = 'Time (s)'
plotargs['ylabel'] = 'Angular Displacement (rad)'
plotargs['lineshape'] = '-'
plotargs['loc'] = 1

for i in range(len(alphavals)):
    parameters['alpha'] = alphavals[i]
    parameters['kappa'] = parameters['alpha']*(2*parameters['omega_0'])
    chi = str(round(parameters['alpha'], 2))
    plotargs['color'] = colors[i+1]
    plotargs['graph label'] = r'$\chi =$ '+ chi 
    yvals = RK4(pendulum, y_0, times, parameters)
    
    pp.displacementplot(times, yvals, plotargs)

plt.rcParams["figure.figsize"] = (8,5.33)
plt.savefig('damped_oscillator.png', dpi=100)
plt.show() 

### ========================================================================
### I will now plot the phase space both for the damped and undamped pendula. 
### As such, I need to change the alphavals to include chi = 0.
### ========================================================================


alphavals = [0, 0.15, 1., 1.85]

plotargs['title'] = r'Phase Space for Different Damping Coefficients $\chi$'
plotargs['xlabel'] = 'Angular Displacement (rad)'
plotargs['ylabel'] = 'Angular Velocity (rad/s)'

for i in range(len(alphavals)):
    parameters['alpha'] = alphavals[i]
    parameters['kappa'] = parameters['alpha']*(2*parameters['omega_0'])
    chi = str(round(parameters['alpha'], 2))
    plotargs['color'] = colors[i]
    plotargs['graph label'] = r'$\chi =$ '+ chi 
    yvals = RK4(pendulum, y_0, times, parameters)
    
    pp.phasespace(times, yvals, plotargs)


plt.savefig('sect1_phasespace.png', dpi=100)
plt.show()






