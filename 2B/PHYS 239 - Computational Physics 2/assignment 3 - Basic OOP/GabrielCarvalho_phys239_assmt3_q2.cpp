#include <iostream>
using namespace std;

class Rectangle {
	
	double iLength, iWidth;
	
	public:
		void setLength(double length);
		void setWidth(double width);
		double getLength();
		double getWidth();
		void area();
		
		Rectangle(double length, double width) {
			iLength = length;
			iWidth = width;
		}
	
};

void Rectangle::setLength(double length) {
	iLength = length;
}

void Rectangle::setWidth(double width) {
	iWidth = width;
}

double Rectangle::getLength() {
	return iLength;
}

double Rectangle::getWidth() {
	return iWidth;
}

void Rectangle::area() {
	cout << "Area = " << iLength * iWidth;
}

main() {
	Rectangle rectangle(10,20);
	rectangle.area();
}
