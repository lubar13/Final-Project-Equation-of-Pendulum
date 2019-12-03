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
import matplotlib.ticker as ticker


import pendulumplot as pp

'''

In this section I will consider the anharmonic behavior of the pendulum
with no external driving nor frictional forces. This anharmonic behavior 
starts to become apparent as the small angle approximation
which starts to become apparent as the small angle approximation no longer 
works. This can be explored by either making the initial angle large or the 
initial angular velocity large. 

'''


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

step = 0.001
lim = 5
num = int(lim/step)

times = np.linspace(0, lim, num + 1)


initialvals = np.linspace(np.pi/15, np.pi/1.1, 3)
phi_in = 0
vel_in = 0

y_0 = np.array([phi_in, vel_in])

yvals = RK4(pendulum, y_0, times, parameters)

plotargs = pp.Plot_Arguments
colors = ['salmon', 'crimson', 'maroon', 'royalblue', 'magenta', 'crimson', 'blueviolet', 'darkslategrey', 'royalblue'
          'darkgreen', 'crimson', 'maroon', 'greenyellow', 'coral', 'orangered', 'turquoise',
          'salmon']

initialvals = [np.pi/20, np.pi/4, np.pi/2, np.pi/1.01]

plotargs['loc'] = 4
plotargs['color'] = colors[0]
plotargs['lineshape'] = '-'
plotargs['title'] = r'Displacement for Different $\phi_0$ with $T_0 = {} s$'.format(str(round(T,3))) 
plotargs['xlabel'] = 'Angular Displacement (rad)'
plotargs['ylabel'] = 'Angular Velocity (rad/s)'
plotargs['titlesize'] = 18
plotargs['labelsize'] = 12

### ===========================================================================
### I will first plot the displacement for different instances in which I 
### increase the initial angle of the pendulum, marking the times at which 
### the analytical solution predicts the period. In this case, the initial 
### velocity will be set to zero for simplicity and in order to better observe
### the effects.
### ===========================================================================


fig, axs = plt.subplots(1,3)


for i in range(len(initialvals)):
    times = times
    y_0 = np.array([initialvals[i], 0])
    phi = str(round(initialvals[i], 3))
    
    yvals = RK4(pendulum, y_0, times, parameters)
    
    axs[0].plot(times, yvals[:,0], '-', color = colors[i], label=r'$\phi_0 = $' + phi)
    axs[1].plot(yvals[:,0], yvals[:,1], '-', color = colors[i], label=r'$\phi_0 = $' + phi)
    

x = np.array([0., T, 2*T, 3*T, 4*T, 5*T])
xlabels = ['','0', r'$T_0$', r'$2T_0$', r'$3T_0$', r'$4T_0$',r'$5T_0$']

axs[0].set_xticks(x, xlabels)
axs[0].xaxis.set_major_locator(ticker.MultipleLocator(T))
axs[0].xaxis.set_major_formatter(ticker.FixedFormatter(xlabels))
axs[0].set_xlabel('Time (s)',fontsize=12)
axs[0].set_ylabel('Angular Displacement (rad)', fontsize=12)
axs[0].set_title(r'Displacement', fontsize=16)
axs[0].legend(loc=3)
axs[0].grid()

axs[1].set_xlabel('Angular Displacement (rad)', fontsize=12)
axs[1].set_ylabel('Angular Velocity (rad/s)', fontsize=12)
axs[1].set_title('Phase Space', fontsize=16)




comparisons = 150
initials = np.linspace(np.pi/150, np.pi-0.01, comparisons)

periods = []
periodsarr = np.array(periods)
for i in range(len(initials)):
    y_0 = np.array([initials[i], 0])
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
ytic = ['', r'$T_0$', r'$2T_0$', r'$3T_0$', r'$4T_0$']


axs[2].plot(initials, periods, '-', color = 'darkslategrey')
axs[2].set_title(r'Divergence of Period as $\phi_0 \to \pi$', fontsize=16)
axs[2].set_xlabel(r'$\phi_0$ (rad)', fontsize=12)
axs[2].set_ylabel('Period (s)', fontsize=12)
axs[2].axvline(np.pi, color = 'k', linestyle = '--')

axs[2].yaxis.set_major_locator(ticker.MultipleLocator(T))
axs[2].yaxis.set_major_formatter(ticker.FixedFormatter(ytic))

fig.set_size_inches(25, 6)
fig.savefig('section2.png', bbox_inches='tight', dpi=100)


plt.show()



#plt.rcParams["figure.figsize"] = (8, 5.33)

#plt.savefig('displacement_for_diff_phi_in.png', dpi=100)

#plt.show()

### ===========================================================================
### I will now do the same for the initial velocity, setting the initial 
### position to zero. The maximum value for the initial velocity was chosen 
### on purpose to be the maximum velocity at zero displacement so that 
### the pendulum does not make a full revolution, but goes back down. Slightly 
### increasing the initial velocity by less than a hundredth is enough to be
### make over-the-top oscillations. 
### ===========================================================================
### ===========================================================================
### Below I plot the phase space for the above displacements.
### ===========================================================================


