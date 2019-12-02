#{
PHYS 239 Assignment 1 Question 3 - Eigenvalue Distributions
author: Gabriel Carvalho
last updated: 2019-05-26
#}

# set the state of the random function
rand( 'state', 0 );

# find the eigenvalues of 100 random 100x100 matrices
for mainLoop = 0:99
  
  # get new random eigenvalues
  eigvalUniformC = eig( round( rand( 100, 100 ) ) );
  eigvalGaussianC = eig( randn( 100, 100 ) );
  
  # append the eigenvalues to existing list
  for subLoop = 1:1:100 
    eigvalUniformR(100 * mainLoop + subLoop) = norm( eigvalUniformC(subLoop) );
    eigvalGaussianR(100 * mainLoop + subLoop) = norm( eigvalGaussianC(subLoop) );
  end
  
end

# generate historgrams of eigenvalues
subplot( 1, 2, 1 );
hist( eigvalUniformR, 200 );
title( "Eigenvalues of Matrix of Zeros and Ones" );
subplot( 1, 2, 2 );
hist( eigvalGaussianR, 200 );
title( "Eigenvalues of Matrix With Gaussian Distribution" );