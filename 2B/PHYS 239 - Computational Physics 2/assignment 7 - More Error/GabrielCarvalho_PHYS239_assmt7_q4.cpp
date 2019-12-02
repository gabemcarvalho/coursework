#include <iostream>
#include <cmath>
#include <dislin.h>
using namespace std;

double xCubed( double x ) {
	return x*x*x;
}

double deriv( double aF(double), double aX, double dx ) {
	return ( aF(aX+dx) - aF(aX-dx) ) / (2.0 * dx);
}

double newton( double aF(double), double a, double aEps, double dx ) {
	double del = -aF( a ) / deriv( aF, a, dx );
	a = a + del;
	if ( fabs(del) < aEps ) {
		return a;
	} else {
		return newton( aF, a, aEps, dx );
	}
}

main() {
	double dx = 0.1;
	double x[100], y[100];
	int loop = 0;
	while (dx >= 1.0e-6 && loop < 100) {
		double root = newton( xCubed, 0.1, 1.0e-6, dx );
		y[loop] = root;
		cout << "dx = " << dx << " : root = " << root << endl;
		x[loop] = dx;
		dx /= sqrt(10.0);
		loop++;
	}
	
	cout << "-----" << endl;	
	
	// Compute points for graphs
	double logY[loop];
	for (int i=0; i<10; i++) {
		logY[i] = log10(y[i]);
	}
	
	// Plot of error vs. dx^3
	metafl("XWIN");
	disini();
	name("Step Length", "x");
	name("Calculated Root", "y");
	titlin( "Convergence of Newton's Method with Varying dx", 4 );
	labels("EXP", "xy");
	incmrk(1);
	setscl(x, loop, "x");
	setscl(y, loop, "y");
	axsscl("LOG","xy");
	graf(0, 10, 0, 1, 0, 10, 0, 1);
	title();
	curve(x, y, loop);
	disfin();
}
