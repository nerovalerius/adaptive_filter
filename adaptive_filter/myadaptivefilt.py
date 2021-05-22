
#            _             _   _              __ _ _ _            
#           | |           | | (_)            / _(_) | |           
#   __ _  __| | __ _ _ __ | |_ ___   _____  | |_ _| | |_ ___ _ __ 
#  / _` |/ _` |/ _` | '_ \| __| \ \ / / _ \ |  _| | | __/ _ \ '__|
# | (_| | (_| | (_| | |_) | |_| |\ V /  __/ | | | | | ||  __/ |   
#  \__,_|\__,_|\__,_| .__/ \__|_| \_/ \___| |_| |_|_|\__\___|_|   
#                   | |                                           
#                   |_|                                           
#                                                                                                                                                          
# Project       : Adaptive LMS Filter - create an adaptive LMS filter with a delay compensation - create a demo to illustrate
# File Purpose  : implementation of the LMS into a Python
# Course        : Digital Signal Processing 2 - Salzburg University Of Applied Sciences
# Author        : Armin Niedermueller
# Date          : 23.05.2021
# Literature    : none


import numpy as np
import matplotlib.pyplot as plt
import padasip as pa


# Adaptive LMS Filter Tasks:
# Create a filter which learns the difference from (signal + noise) to (noise)
# Use the filter to substract noise from our signal
# Learning = comparing (signal + noise) with (noise) with an error function and then changing the weights

def my_lms_filter(d, y, mu=0.1, b=np.ones(6)):
    """
    Parameters
    ----------
    d:          array[double], desired signal -> (noise) - delayed
    y:          array[double], input signal -> (signal + noise) (aka x, y_hat)
    mu:         double, learning rate
    b:          array[double], weights / or initial filter coefficients

    Returns
    ---------
    y_out:          array[double], output signal
    error:          array[double], filter error over time
    b_new:          array[double], the learned, weights over time
    """
    
    ############################# DELAY COMPENSATION ############################

    # Get first n values of our second signal - (signal + noise)
    needle = y[0:len(p)]

    # Error from needle in haystack comparison
    # infinity
    e = float("inf")
    new_e = 0
    delay = 0

    # find those values in the second signal
    for i in range(len(p), len(d)):
        # compare each position in the haystack with our needle
        for j in range(0, i):
            # squared error sum
            new_e = new_e + (needle[j]**2 - d[i-j]**2 )**0.5
        
        if new_e < e:
            e = new_e
            # save index position of delay
            delay = i - len(p)
            
    # find them in first signal, since first signal is delayed
    # implement a threshold 





















    ############################## ADAPTIVE FILTER ##############################

    # Signal length
    N = len(x)

    # Number of weights / filter taps / filter coefficients
    p = len(b)

    # Output signal
    y_out = []

    # Error
    error = []

        
    for n in range(p, N):

        # Creation of our input matrix with historical values -> dot product possible
        Y = np.array([y[n-i] for i in range(p)])

        # save output signal over time - dot product of signal and weights
        y_out.append(np.dot(b, Y))

        # save error over time
        error.append(d[n-p] - y_out[-1])

        # adapt the weights - learning
        b = b + (mu * error[-1] * Y)

    # our learned weights / coefficients
    b_new = b

    return y_out , error , b_new