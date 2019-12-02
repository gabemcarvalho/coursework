/* Demonstrates the DISLIN plotting program */
#include <iostream>
#include "dislin.h"		// Includes the DISLIN potting routines
using namespace std;
double f( double aX ) {	// Function to be graphed
	return aX * aX;
}

main() {
	
	double x[11], y[11];	// 11 element arrays for coords
	double del = 0.1;		// spacing between x values
	for ( int loop = 0; loop < 11; loop++ ) {
		// fill the arrays with data
		x[loop] = loop * del;
		y[loop] = f( x[loop] );
	}
	
	metafl( "PDF" );		// Initializes the output device
	/*
	Export options:
	- "XWIN": opens in a sparate window
	- "TIFF": export as a .tiff
	- "POST": export as a postscript plot file
	- "PDF":  export as a .pdf
	*/
	disini();				// Init plotting package
	name( "X-axis", "x" );	// Axis labels
	name( "Y-axis", "y" );
	qplsca( x, y, 11 );		// plotting routine
	disfin();				// exits DISLIN
	
}
