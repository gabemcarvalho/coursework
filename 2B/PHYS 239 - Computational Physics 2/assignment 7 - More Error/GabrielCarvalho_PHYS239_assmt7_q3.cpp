#include <iostream>
#include <cmath>
using namespace std;

double xRootX( double x ) {
	return x * sqrt( abs( x ) );
}

double deriv( double aF(double), double aX ) {
	double dx = 1.0e-4;
	return ( aF(aX+dx) - aF(aX-dx) ) / (2.0 * dx);
}

// Modified to just give the number of iterations before achieving the desired precision
double newton( double aF(double), double a, double aEps ) {
	double del = -aF( a ) / deriv( aF, a );
	a = a + del;
	if ( fabs(del) < aEps ) {
		return 0;
	} else {
		return 1 + newton( aF, a, aEps );
	}
}

main() {
	cout << "steps for sin(x): " << newton( sin, 0.1, 1.0e-4 ) << endl;
	cout << "steps for x*sqrt(abs(x)): " << newton( xRootX, 0.1, 1.0e-4 ) << endl;
}
