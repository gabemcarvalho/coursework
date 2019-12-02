#include <iostream>
#include <fstream>
using namespace std;

//int *myFunction(int *aI, int *aJ) {
//	*aI = *aI * (*aJ);
//	return aI;
//}
//
//main() {
//	int *aI;
//	int *aJ;
//	*aI = 2; // ERROR: assigning a value to an uninitialized pointer
//	*aJ = 3;
//	cout << (*myFunction(aI, aJ)) << endl;
//}

//void function(int *aI, int *aJ) {
//	*aJ = 20;
//	aI = aJ; // doesn't do anything
//}
//
//main() {
//	int j = 10;
//	int k = 15;
//	function (&j, &k);
//	cout << j << '\t' << k << endl;
//}

//ostream* function(ostream *aOut) {
//	*(aOut) << "Hello" << endl;
//	return aOut;
//}
//
//main() {
//	function(function(&cout));
//}

//int *myFunction() {
//	int *aV = new int[3];
//	for (int loop=0; loop<3; loop++) {
//		aV[loop] = loop;
//	}
//	return aV;
//}
//
//main() {
//	int *v;
//	v = myFunction();
//	cout << v[1] << endl;
//}

//main() {
//	int *a = new int[9];
//	for (int loop=0; loop<9; loop++) a[loop] = loop;
//	int **b = new int*[3];
//	for (int loop = 0; loop < 3; loop++) b[loop] = a + 3*loop;
//	for (int loop = 0; loop < 3; loop++) {
//		for (int loop2 = 0; loop2 < 3; loop2++) {
//			b[loop2][loop] = loop;
//		}
//	}
//	delete[] a;
//	cout << b[2][2];
//	delete[] b;
//}

//main() {
//	const int j[4] = {1,2,3,4};
//	int *k = &j;
//	k[2] = 10;
//	cout << j[2] << endl;
//}

//int l = 5;
//int *lp = &l;
//int myF(int*(&p)) {
//	p = lp;
//	return *p;
//}
//main() {
//	l = 4;
//	int *p = &l;
//	myF(p);
//	cout << *p;
//}

main() {
	int** m = new int*[2];
	m[0] = new int [3];
	m[1] = new int [2];
	for (int i = 0; i < 3; i++) m[0][i] = i;
	for (int i = 0; i < 2; i++) m[1][i] = i+3;
	cout << (*m)[1];
}
