# -*- coding: utf-8 -*-
"""
Created on Mon May 18 18:48:51 2020

@author: Gabriel Carvalho
"""

import numpy as np
import matplotlib.pyplot as plt

# searching for set of a and b where both equations equal zero

# equation at x = 0
def eq1(a, b, y1):
    if abs(a) < 1E-5: return -1;
    return np.exp(b / a) + np.power(a, 2.0) * np.exp(-b / a) - 2.0 * y1;

# equation at x = 1
def eq2(a, b, y2):
    if abs(a) < 1E-5: return -1;
    return np.exp((b + 1.0) / a) + np.power(a, 2.0) * np.exp(-(b + 1.0) / a) - 2.0 * y2;

N = 1001
grid = 0.001;
Y1 = 1.0;
Y2 = 0.5871;

# starts from -x, +y corner
a1 = -1;
a2 = 1;
b1 = 1;
b2 = -1;

apoints = np.linspace(a1, a2, N)
bpoints = np.linspace(b1, b2, N)

results = np.zeros((N, N))
min_val = 1000000.0;
imin = 0;
jmin = 0;


for i in range(N):
    for j in range(N):
        val =  abs(eq1(apoints[i], bpoints[j], Y1)) + abs(eq2(apoints[i], bpoints[j], Y2));
        results[j, i] = np.log( 1.0 / min( val, 1000) );
        if val < min_val:
            imin = i;
            jmin = j;
            min_val = val;
            
amin = a1 + (a2 - a1) / (N - 1.0) * imin;
bmin = b1 + (b2 - b1) / (N - 1.0) * jmin;
delta = (b2 - b1) / (N - 1.0);
print("min values:");
print("a: " + str(amin));
print("b: " + str(bmin));
print("delta: " + str(delta));

plt.figure(figsize=(10,10), dpi=160);
plt.grid(True, color="k", alpha=0.5);
plt.xlabel("a");
plt.ylabel("b");
plt.xticks(np.arange(a1, a2 + grid / 2.0, grid));
plt.yticks(np.arange(b2, b1 + grid / 2.0, grid));
plt.imshow(results, extent=[a1, a2, b2, b1]);

