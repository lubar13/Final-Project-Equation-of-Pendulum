#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 13:56:12 2019

@author: lucasbaralt
"""

import numpy as np


"""

In this file, I create the system of ODE's for the pendulum in question. I have 
included three different functions for the pendulum, whereby each is written 
in terms of particular parameters, so that it becomes easier to manipulate 
different parameters and to see what effect such manipulation has in the overall
motion of the pendulum. As such, I have written an equation for the pendulum in the 
two important ways: in terms of a constant torque whose amplitude only depends on the 
driving frequency and time, and in terms of a torque that also depends on the displacement 
of the pendulum from equilibrium, which is what we expect to happen for gravity acting 
on the pendulum or using a metal pendulum and putting a magnetic field below it.


I have also added a dictionary of the parameters, so that I can just call and rename
its values in future files. 


While I include in the parameters dictionary options for manipulating the mass
and thus the moment of inertia and other such parameters, the code can work with only the 
variables provided. We can of course define these variables in terms of a real measurements 
in the case that we want to simulate a real life pendulum of interest.

"""



Parameters = {'omega_0': 0., 'kappa': 0., 'chi': 0., 'eta': 0., 'omega_d': 0., 'M': 0., 
              'alpha': 0., 'delta': 0.}

def pendulum(t, y, args):
    
    dydt = np.zeros(2)
    
    dydt[0] = y[1]
    
    dydt[1] = (-(args['omega_0']**2)*np.sin(y[0]) - args['kappa']*y[1]
    + args['eta']*np.cos(args['omega_d']*t+args['delta']))
    
    return dydt

    
def pendulumTorque(t, y, args):
    
    dydt = np.zeros(2)
    
    dydt[0] = y[1]
    dydt[1] = -(np.sin(y[0]))*(args['omega_0']**2+args['eta']*np.cos(args['omega_d']*t+args['delta'])) - args['kappa']*y[1]
    
    return dydt


