#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 00:18:21 2019

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
parameters['omega_d'] = parameters['omega_0']*2
parameters['kappa'] = 2*parameters['omega_0']*0.1
parameters['eta'] = 16
parameters['delta'] = 0.


T = (2*np.pi)/parameters['omega_0']

step = 0.001
lim = 30
num = int(lim/step)

times = np.linspace(0, lim, num + 1)

initialvals = np.linspace(np.pi/15, np.pi/1.1, 3)
phi_in = 2.4
vel_in = -1.3

y_0 = np.array([phi_in, vel_in])
yvals = RK4(pendulum, y_0, times, parameters)

plotargs = pp.Plot_Arguments
colors = ['orange', 'red', 'turquoise', 'coral', 'crimson', 'magenta', 'blueviolet', 'darkslategrey', 'royalblue'
          'darkgreen', 'maroon', 'greenyellow', 'coral', 'orangered',
          'salmon']


plotargs['loc'] = 4
plotargs['color'] = colors[0]
plotargs['lineshape'] = '-'
plotargs['title'] = ''
plotargs['titlesize'] = 18
plotargs['labelsize'] = 12

fig1, axs1 = plt.subplots(2,1)


parameters['kappa'] = 2*parameters['omega_0']*0.013
parameters['omega_d'] = parameters['omega_0']*2#0.56
parameters['eta'] = 71.123#71.17
y1 = RK4(pendulum, y_0, times, parameters)

parameters['kappa'] = 2*parameters['omega_0']*0.013
parameters['omega_d'] = parameters['omega_0']*2#0.56
parameters['eta'] = 71.124#71.18
y2 = RK4(pendulum, y_0, times, parameters)

parameters['kappa'] = 2*parameters['omega_0']*0.013
parameters['omega_d'] = parameters['omega_0']*2#0.56
parameters['eta'] = 71.125#71.19
y3 = RK4(pendulum, y_0, times, parameters)

etas = [71.123, 71.124, 71.125]

axs1[0].plot(times, y1[:,0], '-', color='crimson', label=r'$\eta = $ {}'.format(etas[0]))
axs1[0].plot(times, y2[:,0], '-', color='royalblue', label=r'$\eta = $ {}'.format(etas[1]))
axs1[0].plot(times, y3[:,0], '-', color='darkgreen', label=r'$\eta = $ {}'.format(etas[2]))

axs1[0].set_xlabel('Time (s)')
axs1[0].set_ylabel('Angular Displacement (rad)')
fig1.suptitle(r'Butterfly Effects for Driving Force $\eta$')
axs1[0].legend(loc=3)
#fig1.set_size_inches(12, 8)
#fig1.savefig('butterflyeffect.png', dpi=100)
#plt.show()



#fig2, axs2 = plt.subplots()#1,3, sharey=True)

axs1[1].plot(y1[:,0], y1[:,1], '-', color='crimson', label=r'$\eta = $ {}'.format(etas[0]))
axs1[1].plot(y2[:,0], y2[:,1], '-', color='royalblue', label=r'$\eta = $ {}'.format(etas[1]))
axs1[1].plot(y3[:,0], y3[:,1], '-', color='darkgreen', label=r'$\eta = $ {}'.format(etas[2]))

#axs2[0].set_xlabel('Angular Displacement (rad)')
axs1[1].set_xlabel('Angular Displacement (rad)')
#axs2[2].set_xlabel('Angular Displacement (rad)')

axs1[1].set_ylabel('Angular Velocity (rad/s)')
#axs1[1].set_title(r'Butterfly Effects for Driving Force $\eta$')
axs1[1].legend(loc=2)

#fig1.tight_layout(pad=2.2)
fig1.set_size_inches(12, 8)
fig1.savefig('butterflyeffects.png', bbox_inches='tight',dpi=100)
plt.show()




