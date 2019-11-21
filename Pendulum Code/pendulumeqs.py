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
two important ways: in terms of the acting torques on the system divided by the 
moment of inertia of the pendulum; and in a way that includes explicitly the damping 
coefficient, which I have decided to call chi. 


The damping coefficient is directly proportional to the frictional force acting on 
the system (e.g. air friction, fluid viscosity, etc), so it enables us to directly 
measure how increasing or decreasing the viscosity of the system affects it.

I have also added a dictionary of the parameters, so that I can just call and rename
its values in future files. 

"""



Parameters = {'omega_0': 0., 'kappa': 0., 'chi': 0., 'eta': 0., 'omega_d': 0., 'M': 0., 
              'alpha': 0., 'delta': 0., 'inertia': 0., 'torque':0.}

def pendulum(t, y, args):
    
    dydt = np.zeros(2)
    
    dydt[0] = y[1]
    
    dydt[1] = (-(args['omega_0']**2)*np.sin(y[0]) - args['kappa']*y[1] 
    + args['eta']*np.cos(args['omega_d']*t+args['delta']))
    
    return dydt

def pendulumChi(t, y, args):
    
    dydt = np.zeros(2)
    
    dydt[0] = y[1]
    dydt[1] = -(args['omega_0']**2)*np.sin(y[0]) - 2*(args['omega_0'])*(args['M'])*(args['chi'])
    + args['eta']*np.cos(args['omega_d']*t)
    
    
    return dydt
    
def pendulumTorque(t, y, args):
    
    dydt = np.zeros(2)
    
    dydt[0] = y[1]
    dydt[1] = -(np.sin(y[0]))*(args['omega_0']**2+args['eta']*np.cos(args['omega_d']*t+args['delta'])) - args['kappa']*y[1]
    
    return dydt


