% Octave/Matlab program to illustrate Fourier transforms
% Octave download at https://www.gnu.org/software/octave/
%
% To run: Save program under the name fouriertransform.m to a 
% directory open up the Octave GUI, navigate to this directory 
% and type fouriertransform into the Octave command window.
%
% Further documentation in D. Yevick, "A Short Course in 
% Computational Science and Engineering: C++, Java and Octave 
% Numerical Programming with Free Software Tools", Cambridge
% University Press.

clf;
gridPointsR = [ 0 : 63 ];

slowSignalR = sin( 5 * 2 * pi / 64 * gridPointsR );
fastSignalR = sin( 25 * 2 * pi / 64 * gridPointsR );
noiseR = 0.8 * ( rand( 1, 64 ) - 0.5 );
totalSignalR = slowSignalR + fastSignalR + noiseR;

%figure( 1 );
subplot( 2, 3, 1 );
plot( totalSignalR );
title( 'Input Signal' );

%figure( 2 );
subplot( 2, 3, 2 );
plot( abs( fft( noiseR ) ).^2 );
title( 'Power Spectrum of White noise' );

fftOftotalSignalR = fft( totalSignalR );

%figure( 3 );
subplot( 2, 3, 3 );
plot( imag( fftOftotalSignalR ) );
title( 'Imaginary Part of FFT of Input Signal' );

hammingFilterR = fftshift( hamming( 64 )' );

%figure( 4 );
subplot( 2, 3, 4 );
plot( hammingFilterR );
title( 'Shifted Filter Function' );

filteredSpectrumR = fftOftotalSignalR .* hammingFilterR;

%figure( 5 );
subplot( 2, 3, 5 );
plot( abs( filteredSpectrumR ).^2 );
title( 'Power Spectrum of Filtered Input Signal' );

filteredSignalR = ifft( filteredSpectrumR );

%figure( 6 );
subplot( 2, 3, 6 );
plot( real( filteredSignalR ) );
hold on;
plot( slowSignalR, 'r' );
title( 'Recovered (Filtered) and Slow Input Signal' );
hold off;