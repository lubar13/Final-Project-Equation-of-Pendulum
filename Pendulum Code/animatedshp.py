#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 18:54:26 2019

@author: lucasbaralt
"""


import numpy as np
import matplotlib.pyplot as plt
from rungekutta4 import RK4
from pendulumeqs import pendulum, Parameters

import matplotlib.animation as animation
plt.rcParams['animation.ffmpeg_path'] = '/usr/local/bin/ffmpeg'

observables = Parameters

g = 9.8 #[m/s^2]
l = 1. #[m]
observables['M'] = 1. #[kg]
I = (1/3)*observables['M']*l*l
observables['kappa'] = 0.
observables['eta'] = 0.
observables['omega_0'] = np.sqrt((observables['M']*g*l)/I)

N = 500
times = np.linspace(0., 10., N+1)


phi_0 = np.pi/20

phidot_0 = 0.


initial_conditions = np.array([phi_0, phidot_0])

yvals = RK4(pendulum, initial_conditions, times, observables)



smol = phi_0*np.cos(observables['omega_0']*times)





'''
plt.plot(times, yvals[:,0], '-', c='r', label='Calculated Angular Displacement')
plt.plot(times, smol, '--', c='b', label='Small Angle Approximation')

plt.legend(loc=2)
plt.title('Time Evolution of Simple Harmonic Pendulum')
plt.xlabel('Time(s)')
plt.ylabel('Angle (rad)')
'''



dt = 0.02

### Positions
angles = yvals[:,0]
x1 = l*np.sin(angles)
y1 = -l*np.cos(angles)

'''
def animatewave(i):
    thisx = [0, times[i]]
    thisy = [0, angles[i]]
    line.set_data(thisx, thisy)
    
    return line, time_text
'''  



fig1 = plt.figure()
ax1 = fig1.add_subplot(111, autoscale_on=False, xlim=(0, 10), ylim=(-0.2, 0.2))

line1, = ax1.plot([], [], '-',c = 'g', lw=1)


def animatewave(i):
        
    
    xdata = []
    ydata = []
    
    
    xdata.append(times[:i])
    ydata.append(angles[:i])
        
    line1.set_data(xdata, ydata)
    
    
    return line1


def init():
    line.set_data([], [])
    time_text.set_text('')
    return line, time_text

waveanimation = animation.FuncAnimation(fig1, animatewave, np.arange(1,len(yvals[:,0])), 
                                        interval=25)

waveanimation.save('waveani.mp4', fps=15)


   
fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=(-1.5, 1.5), ylim=(-1.5, 1.5))
ax.grid()

line, = ax.plot([], [], 'o-', lw=2)
time_template = 'time = %.1fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)




def animate(i):
    thisx = [0, x1[i]]
    thisy = [0, y1[i]]

    line.set_data(thisx, thisy)
    time_text.set_text(time_template % (i*dt))
    return line, time_text

pendani = animation.FuncAnimation(fig, animate, np.arange(1, len(yvals[:,0])),
                              interval=25, blit=True, init_func=init)

pendani.save('shp.mp4', fps=15)
plt.show()




