# -*- coding: utf-8 -*-
"""
Created on Sun May 31 16:11:00 2020

@author: Gabriel Carvalho
"""

import numpy as np;
import matplotlib.pyplot as plt;

dt = 0.0001;
total_time = 100.0;
n = int(total_time / dt);

g = 1;
m = 0.01;

t = [0];
r = [1];
th = [0];
rdot = [0];
thdot = [0.5];

for i in range(n):
    t.append(t[i] + dt);
    rdot.append(rdot[i] + dt * (0.5 * r[i] * np.power(thdot[i], 2) - 0.5 * g));
    r.append(r[i] + dt * rdot[i]);
    thdot.append(thdot[i] - dt * 2 * rdot[i] / r[i] * thdot[i]);
    th.append(th[i] + dt * thdot[i]);

x = r * np.cos(th)
y = r * np.sin(th)

plt.figure(figsize=(10,10), dpi=300);
plt.xlabel("x");
plt.ylabel("y");
plt.plot(x, y, "k-");
plt.grid(True);
plt.tight_layout();
plt.savefig("q2_plot");
plt.show();
