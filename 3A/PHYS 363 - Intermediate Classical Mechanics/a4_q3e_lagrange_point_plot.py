# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 16:51:23 2020

@author: Gabriel Carvalho
"""

import numpy as np
import matplotlib.pyplot as plt

def V(x, y, G, M1, M2, m, a):
    term1 = -0.5 * m * G * (M1 + M2) / np.power(a, 3) * np.sqrt(np.power(x, 2) + np.power(y, 2))
    term2 = -G * M1 * m / np.sqrt(np.power(a * M2 / (M1 + M2) - x, 2) + np.power(y, 2))
    term3 = -G * M2 * m / np.sqrt(np.power(a * M1 / (M1 + M2) + x, 2) + np.power(y, 2))
    return term1 + term2 + term3

G = 1
M2 = 1
M1 = 2 * M2
m = 1
a = 1

scale = 2
cx = 0
cy = 0
x1 = cx - scale
x2 = cx + scale
y1 = cy + scale
y2 = cy - scale

N = 101
grid = scale / 10;
xpoints = np.linspace(x1, x2, N)
ypoints = np.linspace(y1, y2, N)

plot = np.zeros((N, N))
for i in range(N):
    for j in range(N):
        plot[j, i] = max( V(xpoints[i], ypoints[j], G, M1, M2, m, a), -8)
        
plt.figure(figsize=(10,10), dpi=160);
plt.grid(True, color="k", alpha=0.2);
plt.xlabel("x");
plt.ylabel("y");
plt.xticks(np.arange(x1, x2 + grid / 2.0, grid));
plt.yticks(np.arange(y2, y1 + grid / 2.0, grid));
plt.contour(xpoints, ypoints, plot, 50, extent=[x1, x2, y2, y1]);
