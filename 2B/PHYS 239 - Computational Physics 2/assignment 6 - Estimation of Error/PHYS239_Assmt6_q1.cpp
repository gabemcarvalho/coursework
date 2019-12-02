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
			return ( (*iF)(aX-2*iDx) - 8*(*iF)(aX-iDx) + 8*(*iF)(aX+iDx) - (*iF)(aX+2*iDx) ) / (12*iDx);
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
	double xTo3rd[10], xTo4th[10], logError[10], logDx[10];
	for (int loop=0; loop<10; loop++) {
		xTo3rd[loop] = pow(x[loop],3);
		xTo4th[loop] = pow(x[loop],4);
		logError[loop] = log(y[loop]);
		logDx[loop] = log(x[loop]);
	}
	
	// Print the slope of the log plot
	cout << "Slope of graph 3: " << (logError[9] - logError[0]) / (logDx[9] - logDx[0]);
	
	// Plot of error vs. dx^3
	metafl("XWIN");
	disini();
	name("Step Length ^3", "x");
	name("Error", "y");
	titlin( "Graph 1: Error vs Step Length To The Third Power", 4 );
	labels("EXP", "xy");
	incmrk(1);
	setscl(xTo3rd, 10, "x");
	setscl(y, 10, "y");
	graf(0, 10, 0, 1, 0, 10, 0, 1);
	title();
	curve(xTo3rd, y, 10);
	disfin();
	
	// Plot of error vs dx^4
	metafl("XWIN");
	disini();
	name("Step Length ^4", "x");
	name("Error", "y");
	titlin( "Graph 2: Error vs Step Length To The Fourth Power", 4 );
	labels("EXP", "xy");
	incmrk(1);
	setscl(xTo4th, 10, "x");
	setscl(y, 10, "y");
	graf(0, 10, 0, 1, 0, 10, 0, 1);
	title();
	curve(xTo4th, y, 10);
	disfin();
	
	// Plot of log(error) vs log(dx)
	metafl("XWIN");
	disini();
	name("Log of Step Length", "x");
	name("Log of Error", "y");
	titlin( "Graph 3: Log of Error vs Log of Step Length", 4 );
	incmrk(1);
	setscl(logDx, 10, "x");
	setscl(logError, 10, "y");
	graf(0, 10, 0, 1, 0, 10, 0, 1);
	title();
	curve(logDx, logError, 10);
	disfin();
	
}
