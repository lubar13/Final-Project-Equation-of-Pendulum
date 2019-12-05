#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 23:35:27 2019

@author: lucasbaralt

"""

import numpy as np
import matplotlib.pyplot as plt



"""

I will define the Runge-Kutta 4 algorithm in this file. Note: it is 
based on the code provided to us in the PHYS 250 github repository. 
I will later use this 
for solving the differential equation for the pendulum. I'm creating a separate 
file so that I may use it in future projects, should I need it.

"""


def RK4(function, y_0, xvals, args={}):
    
    """
    
    The arguments of the RK4:
        
        function: (callable)   --> System of first order ODE's
        y_0     : (array)      --> Takes in the initial conditions of the system of ODE's
        xvals   : (array)      --> Defines the steps that the function is to take
        args    : (dictionary) --> Provides the parameters for the ODE
    
    Returns:
        
        y       : (array)      --> Array of approximations of the ODE
        
    
    """
    
    
    ### ====================================================================
    ### First create an array of zeroes where we can store the values of the 
    ### system we're approximating.
    ### ====================================================================
    
    
    y = np.zeros([len(xvals), len(y_0)])
    
    ### The initial conditions of the system:
    
    y[0] = y_0
    
    ### Implement the Runge-Kutta algorithm:
    
    for i, x_i in enumerate(xvals[:-1]):
        
        h = xvals[i+1] - x_i
        
        k1 = h*function(x_i, y[i], args)
        k2 = h*function(x_i + h/2, y[i] + k1/2, args)
        k3 = h*function(x_i + h/2, y[i] + k2/2, args)
        k4 = h*function(x_i + h, y[i] + k3, args)
        
        y[i+1] = y[i] + (1./6.)*(k1 + 2*k2 + 2*k3 + k4)
        
    
    ### The function will return an array of the approximations of the system
    ### for the given initial conditions.    
    
    return y

### it is easy to test the algorithm with the following function   

'''
def expo(x, y, args):
    
    dydx = args['a']*y
    
    return dydx

'''
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
