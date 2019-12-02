clear all;
tR = [ 0 : 63 ];
fastWaveR = sin( 30 / 64 * pi * tR );
slowWaveR = sin( 4 / 64 * pi * tR );
yR = fastWaveR + slowWaveR;

subplot( 2, 3, 1 );
plot( yR );
title( "Inital Signal" );

yfftR = fft( yR );
subplot( 2, 3, 2 );
plot( imag( yfftR ) );
title( "FFT of Signal" );

hammingR = fftshift( hamming( 64 )'.^5 );
subplot( 2, 3, 3 );
plot( hammingR );
title( "Fifth Power Window Function" );

yfftFilteredR = yfftR .* hammingR;
subplot( 2, 3, 4 );
plot( imag( yfftFilteredR ) );
title( "Filtered FFT Signal" );

yFilteredR = real ( ifft( yfftFilteredR ) );
subplot( 2, 3, 5 );
plot( yFilteredR );
title( "Final Filtered Signal" );
