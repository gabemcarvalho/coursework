#include <iostream>
#include <dislin.h>
#include <cmath>
using namespace std;

double xToThe7( double x ) {
	return x*x*x*x*x*x*x;
}

// Integrate the function aF() between A and B using N points
double integrate( double aF(double), double A, double B, int N ) {
	double sum = 0;
	double dx = ( B - A ) / double(N);
	for ( int n = 0; n <= N; n++ ) {
		double xi = A + n * dx;
		sum += aF(xi) + 4*aF(xi + dx / 2.0) + aF(xi + dx);
	}
	sum *= dx / 6.0;
	return sum;
}

// Same thing, specify step size instead
double integrate( double aF(double), double A, double B, double stepSize, bool step) {
	int N = ( B - A ) / stepSize;
	return integrate( aF, A, B, N );
}

main() {
	// Expected integration of x^7 from 0 to 4 is 8192
	double delta = 0.1;
	double x[10], y[10];
	for (int loop=0; loop<10; loop++) {
		double error = abs( integrate( xToThe7, 0, 4, delta, true ) - 8192 );
		y[loop] = error;
		cout << "dx = " << delta << " : error = " << error << endl;
		x[loop] = delta;
		delta /= 1.3;
	}
	
	cout << "-----" << endl;	
	
	// Compute points for graphs
	double xPower[10];
	for (int loop=0; loop<10; loop++) {
		xPower[loop] = pow(x[loop],4);
	}
	
	// Plot of error vs. dx^3
	metafl("XWIN");
	disini();
	name("Step Length", "x");
	name("Error", "y");
	titlin( "Error vs Step Length with Bad Algorithm", 4 );
	labels("EXP", "x");
	incmrk(1);
	setscl(x, 10, "x");
	setscl(y, 10, "y");
	graf(0, 10, 0, 1, 0, 10, 0, 1);
	title();
	curve(x, y, 10);
	disfin();
}
