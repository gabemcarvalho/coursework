clear all

stepNum = 50;
repeatNum = 50000;
kT = 5;
beta = 1 / kT;

histogram = zeros( 1, stepNum );
stepsR = randi( 2, [ 1, stepNum ] ) - 1;
histogramIndex = sum( stepsR );
centralPoint = stepNum / 2;

for loop = 1 : repeatNum
  
  flipPosition = randi( stepNum, 1 );
  stepsR(flipPosition) = 1 - stepsR(flipPosition);
  histogramIndexNew = sum( stepsR ) + 1;
  
  if rand < exp( beta * ( abs( histogramIndexNew - centralPoint ) - ...
    abs( histogramIndex - centralPoint ) ) )
    histogramIndex = histogramIndexNew;
  else
    stepsR(flipPosition) = 1 - stepsR(flipPosition);  
  endif
  
  histogram(histogramIndex) = histogram(histogramIndex) + 1;
  
  # Steadily increase beta as the algorithm preceeds
  kT = 5.0 - 4.5 * loop / repeatNum;
  beta = 1 / kT;
  
endfor

histogram = histogram .* exp( -beta * abs( [ 1 : stepNum ] - centralPoint ) );

stepsR
stepToTheRight = sum( stepsR )

