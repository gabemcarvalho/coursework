#{
PHYS 239 Assignment 1 - Oscillator Function
author: Gabriel Carvalho
last updated: 2019-05-26
#}

function resultC = oscillator( derivativeValuesR, timesR )
  global constantsR;
  # x_dot = v
  # v_dot = -gamma*v - k/m*x
  resultC = [ derivativeValuesR(2); -constantsR(3) * derivativeValuesR(2) - constantsR(2) / constantsR(1) * derivativeValuesR(1) ];
endfunction