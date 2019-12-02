#include <iostream>
#include <fstream>
using namespace std;

main() {
	
	// Get matrices from file in a single array
	ifstream file("q1_input.txt");
	int input[100];
	int inputSize = 0;
	while (1) {
		int x;
		file >> x;
		input[inputSize++] = x;
		if (file.eof())
			break;
	}
	
	// Initialize arrays for matrices
	int *aA1 = new int[4];
	int *aA2 = new int[4];
	int c = 0;
	
	for (int array=0; array<2; array++) {
		for (int i=0; i<2; i++) { for (int j=0; j<2; j++) {
			if (!array) {
				aA1[c] = input[c];
			} else {
				aA2[2*j+i] = input[c]; // Transpose of mA2
			}
			c++;
		}}
	}
	
	// Get arrays as matrices
	int **mA1 = new int*[2];
	mA1[0] = aA1; mA1[1] = &( aA1[2] );
	int **mA2 = new int*[2];
	mA2[0] = aA2; mA2[1] = &( aA2[2] );
	
	// Allocate output matrix
	int *aO = new int[4];
	aO[0] = aO[1] = aO[2] = aO[3] = 0;
	int **mO = new int*[2];
	mO[0] = aO; mO[1] = &( aO[2] );
	
	// Multiply the matrices
	for ( int i = -1; ++i< 2; ) {
		for ( int j = -1; ++j < 2; ) {
			for ( int k = -1; ++k < 2; ) {
				mO[i][j] += mA1[i][k] * mA2[j][k];
			}
		}
	}
	
	// Print the result
	cout << mO[0][0] << " " << mO[0][1] << endl << mO[1][0] << " " << mO[1][1] << endl;
	
	// Deallocate memory
	delete[] aA1; delete[] aA2; delete[] mA1; delete[] mA2; delete[] aO; delete[] mO;
	
}
