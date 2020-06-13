# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 14:09:29 2020

@author: Gabriel Carvalho
"""

import matplotlib.pyplot as plt;

def factorial(n):
    if n < 0: return -1;
    if n == 1 or n == 0: return 1;
    return n * factorial(n - 1);

def multiplicity(N, q):
    return factorial(q + N - 1) / (factorial(q) * factorial(N - 1));

Na = 6;
Nb = 4;
q = 6;

a_multiplicities = [];
b_multiplicities = [];
total_multiplicities = [];

for i in range(q + 1):
    a_multiplicities.append(multiplicity(Na, i));
    b_multiplicities.append(multiplicity(Nb, q - i));
    total_multiplicities.append(a_multiplicities[i] * b_multiplicities[i]);

print(a_multiplicities);
print(b_multiplicities);
print(sum(total_multiplicities));
print("chance of least likely: " + str(100 * total_multiplicities[0] / sum(total_multiplicities)) + "%");
print("chance of most likely: " + str(100 * total_multiplicities[4] / sum(total_multiplicities)) + "%");

plt.plot(total_multiplicities, "ko");
plt.grid();
plt.show();
