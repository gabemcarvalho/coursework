# -*- coding: utf-8 -*-
"""
Created on Mon May 18 23:29:20 2020

@author: Gabriel Carvalho
"""

import numpy as np
import matplotlib.pyplot as plt

def y(x, a, b):
    return 0.5 * (np.exp((x + b) / a) + np.power(a, 2.0) * np.exp(-(x + b) / a));

A_I = [-0.8483, -0.2351, 0.8483, 0.2351];
A_II = [-0.6984, -0.2652, 0.6984, 0.2652];
A_III = [-0.4598, -0.3589, 0.4597, 0.3588];
A_E = [-0.405];
B_I = [-0.3604, -0.1596, -0.6396, -0.8404];
B_II = [-0.3770, -0.1790, -0.8784, -0.8830];
B_III = [-0.2922, -0.2366, -1.0067, -0.9721];
B_E = [-0.263];

graph_a = A_E;
graph_b = B_E;
xpoints = np.linspace(0, 1, 1001);

plt.figure(figsize=(10,10), dpi=160);
plt.xlabel("x");
plt.ylabel("y");
plt.xlim([0, 1]);
plt.ylim([0, 1.2]);
plt.grid(True, color="k", alpha=0.2);
plt.title("Solution for y1 = 1, y2 = 0.5871");

for i in range(len(graph_a)):
    ypoints = y(xpoints, graph_a[i], graph_b[i]);
    if i > 1: ypoints += 0.005;
    plt.plot(xpoints, ypoints, label="a = "+str(graph_a[i])+", b = "+str(graph_b[i]));

plt.legend();
plt.show();