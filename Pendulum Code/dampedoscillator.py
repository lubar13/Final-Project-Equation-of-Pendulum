#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 17:04:07 2019

@author: lucasbaralt
"""

import numpy as np
import matplotlib.pyplot as plt
from rungekutta4 import RK4
from pendulumeqs import pendulum, Parameters

import pendulumplot as pp


parameters = Parameters

'''

In this file I will consider the motion of a damped pendulum, for which there 
is no external torque acting on it. I will consider the three cases of 
an underdamped, overdamped, and critically damped system. The pendulum will consist 
of a thin pole of length L and mass m_1, so that I_1 = (1/3)*m_1*L^2, with a 
spherical mass m_2 of radius r attached at the end, so that the total moment of 
inertia I = (1/3)*m_1*L^2 + (L+r)^2*m_2. 

'''


### ===============================================================================
### Underdamped pendulum (chi < 1). We expect the oscillation of the pendulum 
### to decrease exponentially while still oscillating. This behavior of oscillators
### is relevant in particular in electronics, where oscillations on the output 
### of a step signal is usually unwanted. 
### ===============================================================================



