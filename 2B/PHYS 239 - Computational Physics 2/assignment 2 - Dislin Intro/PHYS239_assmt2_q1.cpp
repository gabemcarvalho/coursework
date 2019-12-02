#include <dislin.h>
const int N = 4;
main() {
	double x[N] = { 0 }, y[4] = { 0 };
	for ( int i = 0; i < N; i++ ) {
		x[i] = i; y[i] = i * i;
	}
	qplot( x, y, N); // N =  number of points = 4
}
