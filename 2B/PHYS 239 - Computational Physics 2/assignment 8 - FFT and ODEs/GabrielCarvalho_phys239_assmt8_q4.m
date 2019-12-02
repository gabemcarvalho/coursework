clear all;

function y = f( x )
  y = sqrt( 1 - x.^2 );
endfunction

function value = monteCarlo( x1, x2, y1, y2, points )
  area = ( x2 - x1 ) * ( y2 - y1 );
  xRandR = rand( 1, points ) * ( x2 - x1) + x1;
  yRandR = rand( 1, points ) * ( y2 - y1) + y1;
  pointsBelowCurve = sum( yRandR < f( xRandR ) );
  value = area * pointsBelowCurve / points + y1 * ( x2 - x2 );
endfunction

for i = 1 : 10
  steps(i) = 1000 * power( 2, i );
  % Integrates a quarter of a unit circle, then multiplies by 4
  integral = monteCarlo( 0, 1, 0, 1, steps(i) );
  circleArea = integral * 4;
  error(i) = abs( 3.14159265 - circleArea );
  % NOTE: The expected area is pi*(1)^2 = pi = 3.14159265
endfor

loglog( steps, error );
title( "Error vs. Number of Points For Monte-Carlo Integration" );
xlabel( "Number of Points" );
ylabel( "Error" );

% Comment on result:  the graph looks different every time,
%                     but the general trend is downward, meaning
%                     more points = higher precision.