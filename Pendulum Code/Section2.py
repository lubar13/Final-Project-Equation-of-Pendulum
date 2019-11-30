#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 16:28:02 2019

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


I = (1/3)*m_1*L*L + (L+r)**2*m_2



parameters['M'] = m_1 + m_2
parameters['omega_0'] = np.sqrt((parameters['M']*g*L_cm)/I)

T = (2*np.pi)/parameters['omega_0']

times = np.linspace(0, 5, 20000)

initialvals = np.linspace(np.pi/15, np.pi/1.1, 3)
phi_in = 0
vel_in = 0

y_0 = np.array([phi_in, vel_in])

yvals = RK4(pendulum, y_0, times, parameters)

plotargs = pp.Plot_Arguments
colors = ['orange', 'red', 'coral', 'crimson', 'magenta', 'crimson', 'blueviolet', 'darkslategrey', 'royalblue'
          'darkgreen', 'crimson', 'maroon', 'greenyellow', 'coral', 'orangered', 'turquoise',
          'salmon']

initialvals = [np.pi/20, np.pi/4, np.pi/2, np.pi/1.01]

plotargs['loc'] = 4
plotargs['color'] = colors[0]
plotargs['lineshape'] = '-'
plotargs['title'] = r'Displacement for Different $\phi_0$ with $T_0 = {} s$'.format(str(round(T,3))) 
plotargs['titlesize'] = 18
plotargs['labelsize'] = 12

for i in range(len(initialvals)):
    times = times
    y_0 = np.array([initialvals[i], 0])
    plotargs['color'] = colors[i]
    phi = str(round(initialvals[i], 3))
    plotargs['graph label'] = r'$\phi_0 = $' + phi
    yvals = RK4(pendulum, y_0, times, parameters)
    
    pp.displacementplot(times, yvals, plotargs)

x = np.array([0., T, 2*T, 3*T, 4*T, 5*T])
xlabels = ['0', r'$T_0$', r'$2T_0$', r'$3T_0$', r'$4T_0$',r'$5T_0$']


plt.xticks(x, xlabels)
plt.grid()
plt.rcParams["figure.figsize"] = (8, 5.33)

plt.savefig('displacement_for_diff_phi_in.png', dpi=100)

plt.show()

initialvels = np.linspace(1., 13.717, 4)
plotargs['title'] = r'Displacement for Different $\dot\phi_0$ with $T_0 = {} s$'.format(str(round(T,3))) 

for i in range(len(initialvels)):
    times = times
    y_0 = np.array([0, initialvels[i]])
    plotargs['color'] = colors[i]
    phidot = str(round(initialvels[i], 3))
    plotargs['graph label'] = r'$\dot\phi_0 = $' + phidot
    yvals = RK4(pendulum, y_0, times, parameters)
    
    pp.displacementplot(times, yvals, plotargs)

plt.xticks(x, xlabels)
plt.grid()

plt.savefig('displacement_for_diff_vel_in.png', dpi=100)

plt.show()

plotargs['title'] = r'Phase Space for Different $\dot\phi_0$ with $T_0 = {} s$'.format(str(round(T,3)))
plotargs['xlabel'] = 'Angular Displacement (rad)'
plotargs['ylabel'] = 'Angular Velocity (rad/s)'


for i in range(len(initialvels)):
    times = times
    y_0 = np.array([0, initialvels[i]])
    plotargs['color'] = colors[i]
    phidot = str(round(initialvels[i], 3))
    plotargs['graph label'] = r'$\dot\phi_0 = $' + phidot
    yvals = RK4(pendulum, y_0, times, parameters)
    
    pp.phasespace(times, yvals, plotargs)


plt.savefig('phasespace_for_dif_vel_in.png', dpi=100)
plt.show()
plotargs['title'] = r'Phase Space for Different $\phi_0$ with $T_0 = {} s$'.format(str(round(T,3)))

for i in range(len(initialvals)):
    times = times
    y_0 = np.array([0, initialvels[i]])
    plotargs['color'] = colors[i]
    phi = str(round(initialvals[i], 3))
    plotargs['graph label'] = r'$\phi_0 = $' + phi
    yvals = RK4(pendulum, y_0, times, parameters)
    
    pp.phasespace(times, yvals, plotargs)


plt.savefig('phasespace_for_dif_phi_in.png', dpi=100)
plt.show()
    
    


comparisons = 150
initialvals = np.linspace(np.pi/150, np.pi-0.01, comparisons)

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

yticvals = [T, 1.6*T, 2.2*T, 2.8*T, 3.4*T, 4*T]
ytic = [r'$T_0$', r'$1.6T_0$', r'$2.2T_0$', r'$2.8T_0$', r'$3.4T_0$', r'$4T_0$']


plt.plot(initialvals, periods, '-', color = 'crimson')
plt.title(r'Divergence of Period as $\phi_0 \to \pi$')
plt.xlabel(r'$\phi_0$ (rad)', fontsize=12)
plt.ylabel('Period (s)', fontsize=12)
plt.axvline(np.pi, color = 'k', linestyle = '--')
plt.yticks(yticvals, ytic)

plt.savefig('divergence_of_period.png', dpi=100)


plt.show()
