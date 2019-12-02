#include <iostream>
#include <dislin.h>
#include <math.h>
using namespace std;

main() {
	
	const int POINTS = 100;
	int timeSteps = 10000;
	
	double position[POINTS];
	double temp[POINTS];
	double tempLast[POINTS];
	for ( int i = 0; i < POINTS; i++ ) {
		position[i] = 3.14159265359 * i / ( POINTS - 1 );
		temp[i] = 10.0 * sin( position[i] );
	}
	
	double diffCoeff = 0.02;
	double dt = 0.01;
	double dx = 3.14159265359 / POINTS;
	double coefficient = diffCoeff * dt / ( dx * dx );
	
	// Initial plot
	metafl( "XWIN" );
	disini();
	name("Position", "x");
	name("Temperature", "y");
	titlin( "Initial Temperature vs Position", 4 );
	setscl( position, POINTS, "X" );
	graf( 0, 3.14159265, 0, dx, -1, 10, -1, 1 );
	title();
	curve( position, temp, POINTS );
	disfin();
	
	for ( int outLoop = 0; outLoop < timeSteps; outLoop++ ) {			// For 10,000 times of length 0.01s
		for ( int loop = 0; loop < POINTS; loop++ ) 				// Save the last set of temperatures
			tempLast[loop] = temp[loop];
		for ( int loop = 0; loop < POINTS; loop++ ) {					// Step through time
			int lowIndex = ( loop - 1 < 0 ) ? POINTS - 1 : loop - 1;	// Loop lower boundary
			int highIndex = ( loop + 1 > POINTS - 1 ) ? 0 : loop + 1;	// Loop upper boundary
			temp[loop] = temp[loop] + coefficient * 
			( tempLast[lowIndex] - 2 * tempLast[loop] + tempLast[highIndex] );
		}
	}
	
	// Final plot
	metafl( "XWIN" );
	disini();
	name("Position", "x");
	name("Temperature", "y");
	titlin( "Final Temperature vs Position", 4 );
	setscl( position, POINTS, "X" );
	graf( 0, 3.14159265, 0, dx, -1, 10, -1, 1 );
	title();
	curve( position, temp, POINTS );
	disfin();
	
}
