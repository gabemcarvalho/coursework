#include <iostream>
#include <math.h>
#include <dislin.h>
using namespace std;

main() {
	
	double a = 1;
	double b = 0;
	double c = 0.3;
	double F = 10;
	double dt = 0.03;
	int steps = 40000;
	
	double x[steps];
	double v[steps];
	x[0] = 1;
	v[0] = 6;
	double t = 0;
	
	for ( int i = 1; i < steps; i++ ) {
		x[i] = x[i-1] + v[i-1] * dt;
		v[i] = v[i-1] - ( a * x[i] * x[i] * x[i] + b * x[i] + c * v[i-1] ) * dt + F * cos( t ) * dt;
		// NOTE: using x[i] instead of x[i-1] gives the proper oscillatory behaviour, based on reference plots I found using Google
		t += dt;
	}
	
	double minX, maxX, minY, maxY, stepX, stepY;
	metafl( "XWIN" );
	disini();
	name("Position, x", "x");
	name("Velocity, v", "y");
	titlin( "Velocity vs Position of a Duffing Oscillator", 4 );
	setscl( x, steps, "X" );
	setscl( v, steps, "Y" );
	incmrk( -1 );	// supresses lines between points
	marker( 21 );	// filled circles
	hsymbl( 5 );	// small size
	graf( minX, maxX, minX, stepX, minY, maxY, minY, stepY );
	title();
	curve( x, v, steps );
	endgrf();
	disfin();
	
}
