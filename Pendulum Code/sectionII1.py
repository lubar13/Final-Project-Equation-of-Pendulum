#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 15:54:31 2019

@author: lucasbaralt
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 23:09:57 2019

@author: lucasbaralt
"""

import numpy as np
from pendulumeqs import pendulum, Parameters
import matplotlib.pyplot as plt
from rungekutta4 import RK4
import pendulumplot as pp

parameters = Parameters

g = 9.8
m_1 = 0.3
m_2 = 0.7
L = 0.35
r = 0.05

L_cm = ((L/2)*(m_1+m_2) + r*m_2)/(m_1+m_2)
 
I = (1/3)*m_1*L*L + (L+r)**2*m_2


parameters['M'] = m_1 + m_2
parameters['omega_0'] = np.sqrt((parameters['M']*g*L_cm)/I)


times = np.linspace(0, 15, 15000)

phi_in = np.pi/10
vel_in = 0

alphavals = [0.15, 1, 1.85]

y_0 = np.array([phi_in, vel_in])


plotargs = pp.Plot_Arguments

colors = ['red', 'blue', 'green', 'orange', 'magenta', 'c'] * 10

plotargs['title'] = r'Displacement for Different Damping Coefficients $\chi$'
plotargs['xlabel'] = 'Time (s)'
plotargs['ylabel'] = 'Angular Displacement (rad)'
plotargs['lineshape'] = '-'
plotargs['loc'] = 1

for i in range(len(alphavals)):
    parameters['alpha'] = alphavals[i]
    parameters['kappa'] = parameters['alpha']*(2*parameters['omega_0'])
    chi = str(round(parameters['alpha'], 2))
    plotargs['color'] = colors[i]
    plotargs['graph label'] = r'$\chi =$ '+ chi 
    yvals = RK4(pendulum, y_0, times, parameters)
    
    pp.displacementplot(times, yvals, plotargs)


plt.show()  


plotargs['title'] = r'Displacement for Different Damping Coefficients $\chi$'
plotargs['xlabel'] = r'Angular Displacement $\phi$ (rad)'
plotargs['ylabel'] = 'Angular Velocity $\dot\phi$ (rad/s)'
plotargs['lineshape'] = '-'
plotargs['loc'] = 1

for i in range(len(alphavals)):
    parameters['alpha'] = alphavals[i]
    parameters['kappa'] = parameters['alpha']*(2*parameters['omega_0'])
    chi = str(round(parameters['alpha'], 2))
    plotargs['color'] = colors[i]
    plotargs['graph label'] = r'$\chi =$ '+ chi 
    yvals = RK4(pendulum, y_0, times, parameters)
    
    pp.phasespace(times, yvals, plotargs)

plt.show()

