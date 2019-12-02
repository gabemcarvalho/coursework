#include <iostream>
using namespace std;

class Semiconductor {
	
	double iElectronDensity, iHoleDensity, iIntrinsicCarrierDensity;
	
	public:
		double getElectronDensity();
		double getHoleDensity();
		void setElectronDensity(double aElectronDensity);
		void setHoleDensity(double aHoleDensity);
		void print();
		
		Semiconductor(double aIntrinsicCarrierDensity) {
			iIntrinsicCarrierDensity = aIntrinsicCarrierDensity;
		}
	
};

double Semiconductor::getElectronDensity() {
	return iElectronDensity;
}

double Semiconductor::getHoleDensity() {
	return iHoleDensity;
}

void Semiconductor::setElectronDensity(double aElectronDensity) {
	iElectronDensity = aElectronDensity;
	iHoleDensity = iIntrinsicCarrierDensity * iIntrinsicCarrierDensity / aElectronDensity;
}

void Semiconductor::setHoleDensity(double aHoleDensity) {
	iHoleDensity = aHoleDensity;
	iElectronDensity = iIntrinsicCarrierDensity * iIntrinsicCarrierDensity / aHoleDensity;
}

void Semiconductor::print() {
	cout << "Electron Density = " << iElectronDensity << endl;
	cout << "Hole Density = " << iHoleDensity << endl;
	cout << "Intrinsic Carrier Density = " << iIntrinsicCarrierDensity << endl;
}

main() {
	Semiconductor silicon(1.5e10);
	silicon.setElectronDensity(1.0e10);
	silicon.print();
}



