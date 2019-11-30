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

times = np.linspace(0, 5, 20000)

initialvals = np.linspace(np.pi/15, np.pi/1.1, 3)
phi_in = np.pi/20
vel_in = 0

y_0 = np.array([phi_in, vel_in])

smol = phi_in*np.cos(parameters['omega_0']*times)


yvals = RK4(pendulum, y_0, times, parameters)


plotargs = pp.Plot_Arguments


T = (2*np.pi)/parameters['omega_0']
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

'''
for i in range(len(initialvals)):
    y_0 = np.array([initialvals[i], 0])
    plotargs['color'] = colors[i]
    phi = str(round(initialvals[i], 3))
    plotargs['graph label'] = r'$\phi_0 = $' + phi
    yvals = RK4(pendulum, y_0, times, parameters)
    
    pp.displacementplot(times, yvals, plotargs)
    
plt.plot(times, smol1, '--', color='k', label=r'$\phi = \phi_0\mathrm{cos}(\omega_0t)$')
    

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

errors = []
for t in periods:
    err = t - T
    errors.append(err)



plt.plot(initialvals, periods, '-.', color = 'g')
plt.title(r'Divergence of Period as $\phi_0 \to \pi$')
plt.xlabel(r'$\phi_0$ (rad)')
plt.ylabel('T (s)')
plt.axvline(np.pi, color = 'b', linestyle = '--', label=r'$\pi$')
plt.axhline(T, color = 'r', linestyle = '--', label = 'T = {} s'.format(str(round(T,3))))
plt.legend(loc=2)
plt.show()

initials = np.linspace(np.pi/15, np.pi/1.1, 3)
times = np.linspace(0, 25, 1500)



plotargs['title'] = r'Phase Space for Different $\phi_0$'
plotargs['xlabel'] = r'Angular Displacement $\phi$ (rad)'
plotargs['ylabel'] = r'Angular Velocity $\dot\phi$ (rad/s)'
plotargs['loc'] = 2
plotargs['lineshape'] = '-'

for i in range(len(initials)):
    
    y_0 = np.array([initials[i], 0])
    plotargs['color'] = colors[i]
    phi = str(round(initials[i], 3))
    plotargs['graph label'] = r'$\phi_0 = $' + phi
    yvals = RK4(pendulum, y_0, times, parameters)
    
    pp.phasespace(times, yvals, plotargs)
plt.grid()
plt.show()  
            
parameters['M'] = m_1 + m_2
print(np.sqrt((4*g*L_cm)/((np.pi**2)/100)))
parameters['omega_0'] = np.sqrt((parameters['M']*g*L_cm)/I)
print(parameters['omega_0'])
ratios = np.linspace(0.1, 3, 10)
parameters['omega_d'] = 4.120023767/1.1
parameters['kappa'] = 2*parameters['omega_0']*0
parameters['eta'] = 0*parameters['kappa']
parameters['delta'] = 0


times = np.linspace(0, 30, 50000)

phi_in = 0
vel_in = 2*parameters['omega_0']

alphavals = np.linspace(0.1, 2, 6)

y_0 = np.array([phi_in, vel_in])
yvals = RK4(pendulum, y_0, times, parameters)
'''
plotargs = pp.Plot_Arguments

colors = ['red', 'blue', 'green', 'orange', 'magenta', 'c'] * 10

plotargs['title'] = r'Displacement for Different Damping Coefficients $\chi$'
plotargs['xlabel'] = 'Time (s)'
plotargs['ylabel'] = 'Angular Displacement (rad)'
plotargs['lineshape'] = '-'
plotargs['loc'] = 1
plotargs['color'] = colors[3]
'''
pp.displacementplot(times, yvals, plotargs)
plt.show()
pp.phasespace(times, yvals, plotargs)
'''