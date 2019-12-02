// Gravitational field of a point earth. Illustrates simple 3D plotting routines
#include <iostream>
#include <math.h>
#include "dislin.h"
using namespace std;

const double KM = 1000;
const double GRAVITATIONAL_CONSTANT = 6.6e-11;
const double EARTH_MASS = 5.97e24;
const double EARTH_RADIUS = 6380 * KM;

const int MATSIZE = 20;

// Gravitational field at a point in N/kg
double gravitationalField( double aX, double aY ) {
	double aR = sqrt( aX * aX + aY * aY );
	if ( aR < EARTH_RADIUS ) {
		return GRAVITATIONAL_CONSTANT * EARTH_MASS * aR / ( EARTH_RADIUS * EARTH_RADIUS * EARTH_RADIUS );
	}
	return GRAVITATIONAL_CONSTANT * EARTH_MASS / ( aX * aX + aY * aY );
}

main() {
	
	double position[MATSIZE];			// coords
	double field[MATSIZE][MATSIZE];		// gravitational field
	float offset = MATSIZE / 2 - 0.5; 	// grid starting point
	
	// calculate coords
	for ( int loop = 0; loop < MATSIZE; loop++ ) {
		position[loop] = 0.1 * EARTH_RADIUS * ( loop - offset );
	}
	
	// calculate field
	float x, y;
	for ( int outLoop = 0; outLoop < MATSIZE; outLoop++ ) {
		x = position[outLoop];
		for ( int inLoop = 0; inLoop < MATSIZE; inLoop++ ) {
			y = position[inLoop];
			field[outLoop][inLoop] = gravitationalField( x, y );
		}
	}
	
	// plot
	metafl( "PNG" );
	disini();
	int iPlot = 2;
	if ( iPlot == 1 ) { 				// surface plot
		qplsur( (double*) field, MATSIZE, MATSIZE );
	} else if ( iPlot == 2 ) {			// colour plot
		qplclr( (double*) field, MATSIZE, MATSIZE );
	} else {							// contour plot
		int numberOfContours = 30;
		qplcon( (double*) field, MATSIZE, MATSIZE, numberOfContours );
	}
	
}
