clear all;
goodX = [];
goodY = [];

function y = f( x )
  y = sqrt( 1 - x.^2 );
endfunction

x1 = 0;
x2 = 1;
y1 = 0;
y2 = 1;
area = ( x2 - x1 ) * ( y2 - y1 );

points = 32000;

xRandR = rand( 1, points ) * ( x2 - x1) + x1;
yRandR = rand( 1, points ) * ( y2 - y1) + y1;

pointsBelowCurve = 0;
for i = 1 : points
  check = yRandR(i) < f( xRandR(i) );
  pointsBelowCurve += check;
  if check
    goodX = [ goodX, xRandR(i) ];
    goodY = [ goodY, yRandR(i) ];
  endif
endfor

plot( goodX, goodY, '. b' );
title( "Visual Representation of Monte-Carlo Integration" );

integral = area * pointsBelowCurve / points + y1 * ( x2 - x2 );
circleArea = integral * 4