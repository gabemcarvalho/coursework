#include <iostream>
#include <complex>
using namespace std;

const int N = 3; // matrix aA needs size N x N
const complex<double> CI = complex<double>( 0.0, 1.0 );

int gauss( complex<double> aA[][N], complex<double> aC[], complex<double> aB[] ) {
	for ( int i = 0; i < N; i++ ) {
		if ( abs( aA[i][i] ) == 0 ) return 1;	// error flag
		for ( int j = i + 1; j < N; j++ ) {
			complex<double> d = aA[j][i] / aA[i][i];
			for ( int k = i + 1; k < N; k++ ) {
				aA[j][k] -= d * aA[i][k];
			}
			aB[j] -= d * aB[i];
		}
	}
	// back substitution
	for ( int i = N - 1; i >= 0; i-- ) {
		aC[i] = aB[i];
		for ( int j = i + 1; j < N; j++ ) {
			aC[i] -= aA[i][j] * aC[j];
		}
		aC[i] /= aA[i][i];
	}
	return 0;
}

main() {
	
	// set up input matrices
	complex<double> aA[3][3] = {1,0,CI,-CI,1,-CI,-1,0,CI};
	complex<double> aB[3] = {CI,0,-CI};
	complex<double> aC[3];
	
	// perform the gaussian elimination
	gauss( aA, aC, aB );
	
	// print result
	cout << aC[0] << " " << aC[1] << " " << aC[2] << endl;
	// output: aC = [ i; -1; 0 ]
	
}
