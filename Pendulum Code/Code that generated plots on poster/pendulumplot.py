#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 21:25:13 2019

@author: lucasbaralt
"""


import matplotlib.pyplot as plt
import numpy as np


Plot_Arguments = {'graph label': ' ', 'color': ' ', 'title': ' ', 
                    'xlabel': ' ', 'ylabel': ' ', 'lineshape': ' ', 'loc': 1,
                    'labelsize':18, 'titlesize':24}


def displacementplot(times, yvals, args):
    
    plt.plot(times, yvals[:,0], args['lineshape'], c=args['color'], label=args['graph label'])
    plt.legend(loc=args['loc'])
    plt.title(args['title'], fontsize=args['titlesize'])
    plt.xlabel(args['xlabel'], fontsize=args['labelsize'])
    plt.ylabel(args['ylabel'], fontsize=args['labelsize'])
    
    
    return

def phasespace(times, yvals, args):
    
    plt.plot(yvals[:, 0], yvals[:, 1], args['lineshape'], c=args['color'], label=args['graph label'])
    
    plt.legend(loc=args['loc'])
    plt.title(args['title'], fontsize=args['titlesize'])
    plt.xlabel(args['xlabel'], fontsize=args['labelsize'])
    plt.ylabel(args['ylabel'], fontsize=args['labelsize'])
    
    return

def frequencyspectrum(times, yvals, args):
    
    N = len(times) + 1
    
    frequencies = np.fft.fftfreq(len(times), times[1]-times[0])
    
    transform = np.fft.fft(yvals[:,0])/np.sqrt(2*len(times))
    
    plt.plot(frequencies[:int(N/2)]*2*np.pi, abs(transform[:int(N/2)]), 
                         args['lineshape'], c=args['color'], label=args['graph label'])
    
    plt.legend(loc=args['loc'])
    plt.title(args['title'], fontsize=args['titlesize'])
    plt.xlabel(args['xlabel'], fontsize=args['labelsize'])
    plt.ylabel(args['ylabel'], fontsize=args['labelsize'])
    
    
    return


