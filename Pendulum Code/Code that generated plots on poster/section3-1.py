#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 20:23:34 2019

@author: lucasbaralt
"""
import numpy as np
from pendulumeqs import pendulum, Parameters, pendulumTorque
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
parameters['omega_d'] = parameters['omega_0']*2#0.56
parameters['kappa'] = 2*parameters['omega_0']*0.013
parameters['eta'] = 84.5
parameters['delta'] = 0.


T = (2*np.pi)/parameters['omega_0']

step = 0.001
lim = 100
num = int(lim/step)

times = np.linspace(0, lim, num + 1)

initialvals = np.linspace(np.pi/15, np.pi/1.1, 3)
phi_in = 1.9
vel_in = 1.2

y_0 = np.array([phi_in, vel_in])
yvals = RK4(pendulum, y_0, times, parameters)

plotargs = pp.Plot_Arguments
colors = ['orange', 'red', 'turquoise', 'coral', 'crimson', 'magenta', 'blueviolet', 'darkslategrey', 'royalblue'
          'darkgreen', 'maroon', 'greenyellow', 'coral', 'orangered',
          'salmon']

initialvals = [np.pi/20, np.pi/4, np.pi/2, np.pi/1.01]

plotargs['loc'] = 4
plotargs['color'] = colors[0]
plotargs['lineshape'] = '-'
plotargs['title'] = ''
plotargs['titlesize'] = 18
plotargs['labelsize'] = 12

### ==============================================
### Convergent limit cycles
### ==============================================


### convergent limit cycle

y_1 = [2.4, -1.3]
y_2 = [1.9, -1.3]

y1 = RK4(pendulumTorque, y_1, times, parameters)
y2 = RK4(pendulumTorque, y_2, times, parameters)

fig, axes = plt.subplots(2, 1)


axes[0].plot(times, y1[:,0], '-', color='salmon', label=r'$\eta = ${}')
axes[0].set_ylabel('Angular Displacement (rad)', fontsize=12)
axes[0].set_xlabel('Time (s)', fontsize=12)
axes[0].set_title('Displacement', fontsize=16)

axes[1].plot(y1[:,0], y1[:,1], '-', color='salmon')
axes[1].set_ylabel('Angular Velocity (rad/s)',fontsize=12)
axes[1].set_xlabel('Angular Displacement (rad)',fontsize=12)
axes[1].set_title('Phase Space', fontsize=16)


fig.tight_layout(pad=2.5)

fig.suptitle(r'Non-Periodic Behavior for $\eta = {}$'.format(str(parameters['eta'])), fontsize=18)
fig.set_size_inches(12, 8)


fig.savefig('nonperiodicbehavior.png', bbox_inches='tight', dpi=100)

plt.show()

### Mode Locking


drivefreqs = parameters['omega_0']*np.array([0.5, 1, 2, 3])

times = np.linspace(0, 40, 25000)
'''
for i in range(len(drivefreqs)):
    parameters['omega_d'] = drivefreqs[i]
    parameters['kappa'] = 2*parameters['omega_0']*0.1
    parameters['eta'] = 16.
    parameters['delta'] = 0.
    freq = str(round(drivefreqs[i], 3))
    plotargs['graph label'] = r'$\omega_d = $' + freq
    plotargs['color'] = colors[i+1]
    yvals = RK4(pendulum, y_0, times, parameters)
    plt.rcParams["figure.figsize"] = (6, 4)
    pp.displacementplot(times[20000:], yvals[20000:], plotargs)
    
plt.show()

for i in range(len(drivefreqs)):
    parameters['omega_d'] = drivefreqs[i]
    parameters['kappa'] = 2*parameters['omega_0']*0.1
    parameters['eta'] = 16.
    parameters['delta'] = 0.
    freq = str(round(drivefreqs[i], 3))
    plotargs['graph label'] = r'$\omega_d = $' + freq
    plotargs['color'] = colors[i+1]
    yvals = RK4(pendulum, y_0, times, parameters)
    plt.rcParams["figure.figsize"] = (6, 4)
    pp.phasespace(times, yvals, plotargs)
'''

    

    

