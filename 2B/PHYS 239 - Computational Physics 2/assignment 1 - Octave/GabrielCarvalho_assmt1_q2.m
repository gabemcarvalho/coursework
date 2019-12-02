#{
PHYS 239 Assignment 1 Question 2 - Rotation Matrix
author: Gabriel Carvalho
last updated: 2019-05-26
#}

aRC = [ 0, 1, 0; -1, 0, 0; 0, 0, 0 ]; # group generator
angle = pi / 2; # angle to rotate by
rRC = expm( -angle * aRC ); # rotation matrix

rRC * [ 1; 0; 0 ]
rRC * [ 0; 1; 0 ]