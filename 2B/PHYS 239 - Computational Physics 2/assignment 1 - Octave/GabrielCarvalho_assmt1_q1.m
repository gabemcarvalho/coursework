#{
PHYS 239 Assignment 1 Question 1 - Second Order ODE
author: Gabriel Carvalho
last updated: 2019-05-26
#}

global constantsR; # [ m, k, gamma ]
constantsR = [ 1, 1, 0 ];
timesR = linspace( 0, 20, 200 ); # 200 values from 0 to 20

# solutions for 4 values of gamma
constantsR(3) = 0;
solutionRC = lsode( @oscillator, [ 1, 0 ], timesR );
subplot( 2, 2, 1 );
plot ( timesR, solutionRC(:,1) );
title( "gamma = 0" );

constantsR(3) = 1;
solutionRC = lsode( @oscillator, [ 1, 0 ], timesR );
subplot( 2, 2, 2 );
plot ( timesR, solutionRC(:,1) );
title( "gamma = 1" );

constantsR(3) = 2;
solutionRC = lsode( @oscillator, [ 1, 0 ], timesR );
subplot( 2, 2, 3 );
plot ( timesR, solutionRC(:,1) );
title( "gamma = 2" );

constantsR(3) = 4;
solutionRC = lsode( @oscillator, [ 1, 0 ], timesR );
subplot( 2, 2, 4 );
plot ( timesR, solutionRC(:,1) );
title( "gamma = 4" );

#{
Comment on output:
The "critically damped" case (gamma = 2) appears to be called such
because it approaches zero faster than any of the other cases. 
#}