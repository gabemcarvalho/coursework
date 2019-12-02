#include <iostream>
#include <dislin.h>
#include <cmath>
using namespace std;

class DerivativeCalculator {
	double (*iF)(double);
	double iDx;
	
	public:
		void setDx(double aDx) {
			iDx = aDx;
		}
		double getDx() {
			return iDx;
		}
		double deriv(double aX) {
			return ( 4*(*iF)(aX+iDx) - 3*(*iF)(aX) - (*iF)(aX+2*iDx)) / (2*iDx);
		}
		
		DerivativeCalculator(double aDx, double aF(double)) : iDx( aDx ) {
			iF = aF;
		}
};

double XtoTheSix(double x) {
	return x*x*x*x*x*x;
}

main() {
	
	// Get derivative calculator and calculate error
	double delta = 1.0e-1;
	DerivativeCalculator DC1(delta, XtoTheSix);
	double x[10], y[10];
	for (int loop=0; loop<10; loop++) {
		double error = abs( DC1.deriv(1.0) - 6 );
		y[loop] = error;
		cout << "dx = " << DC1.getDx() << " : error = " << error << endl;
		x[loop] = DC1.getDx();
		DC1.setDx( DC1.getDx()/1.3 );
	}
	
	cout << "-----" << endl;	
	
	// Compute points for graphs
	double xSquared[10];
	for (int loop=0; loop<10; loop++) {
		xSquared[loop] = pow(x[loop],2);
	}
	
	// Plot of error vs. dx^3
	metafl("XWIN");
	disini();
	name("Step Length Squared", "x");
	name("Error", "y");
	titlin( "Error vs Step Length Squared", 4 );
	labels("EXP", "xy");
	incmrk(1);
	setscl(xSquared, 10, "x");
	setscl(y, 10, "y");
	graf(0, 10, 0, 1, 0, 10, 0, 1);
	title();
	curve(xSquared, y, 10);
	disfin();
	
}
