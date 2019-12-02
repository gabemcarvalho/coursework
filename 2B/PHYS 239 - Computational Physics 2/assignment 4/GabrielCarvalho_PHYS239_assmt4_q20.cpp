#include <iostream>
#include <dislin.h>
using namespace std;

const double R = 0.082;

class Gas {
	public:
		double iA;
		double iB;
		Gas( double aA, double aB ) {
			iA = aA;
			iB = aB;
		}
};

class VanDerWaalsCalculator {
	public:
		Gas iGas;
		double iVolume[100];
		double iPressure[100];
		double iTemperature;
		double iNumberOfMoles;
		int iNumberOfPoints;
		
		VanDerWaalsCalculator( Gas aGas, double aMinVolume,
			double aMaxVolume, double aTemperature, double
			aNumberOfMoles, int aNumberOfPoints ) : iGas(aGas) {
				iTemperature = aTemperature;
				iNumberOfMoles = aNumberOfMoles;
				iNumberOfPoints = aNumberOfPoints;
				for (int i = 0; i < iNumberOfPoints; i++) {
					iVolume[i] = aMinVolume + double(i) / ( iNumberOfPoints - 1 ) * ( aMaxVolume - aMinVolume );
				}
			}
			
		// Use Van der Waals formula to generate pressure vector
		void generatePressure() {
			for (int i = 0; i < iNumberOfPoints; i++) {
				iPressure[i] = iNumberOfMoles * R * iTemperature / ( iVolume[i] - iGas.iB * iNumberOfMoles )
					- iGas.iA * iNumberOfMoles * iNumberOfMoles / ( iVolume[i] * iVolume[i] );
			}
		}
		
		// Graph presure vs. volume
		void draw() {
			metafl( "XWIN" );
			disini();
			name( "Volume (L)", "x" );
			name( "Pressure (atm)", "y" );
			titlin( "Van der Waals Equation: Pressure vs. Volume", 4 );
			graf( 1.0, 10.0, 1.0, 1.0, 0.0, 25.0, 0.0, 5.0 );
			qplot( iVolume, iPressure, iNumberOfPoints );
			disfin();
		}
};

main() {
	Gas oxygen( 0.027, 0.0024 );
	int numberOfPoints = 100;
	double minVolume = 1;
	double maxVolume = 10;
	double temperature = 300;
	double numberOfMoles = 1;
	VanDerWaalsCalculator VDW( oxygen, minVolume, maxVolume,
		temperature, numberOfMoles, numberOfPoints );
	VDW.generatePressure();
	VDW.draw();
}
