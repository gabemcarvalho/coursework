from numpy import loadtxt, cos, pi, linspace, sqrt, exp
import matplotlib.pyplot as plt

# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 18:28:58 2019

@author: Gabriel
"""

data = loadtxt("PartBDischarge.txt",float)
data_times = data[:,2]
data_V = data[:,1]

def curve(time, A, B):
        return A * exp(-time*B)
    
def compute_B(times, y_data, B_values, A):
    error = 10000000.0
    B = 0
    for i in B_values:
        
        # generate curve
        y = []
        for t in times:
            y.append( curve( t, A, B ) )
        
        # this is a pretty basic error sum, but it's good enough
        # calculate error and set values if it has been lowered
        new_error = sum( abs( y_data - y ) )
        if new_error < error:
            error = new_error
            B = i
    
    
    return B

B_value = compute_B(data_times, data_V, linspace(10, 11, 1001), 6.02)
print("RC = " + str(B_value) )

fit_data = []
test_times = linspace( 0.0, 1.0, 101 )
for t in test_times:
    fit_data.append( curve( t, 6, B_value ) )

plt.plot(data_times, data_V)
plt.plot(test_times, fit_data)
plt.show()