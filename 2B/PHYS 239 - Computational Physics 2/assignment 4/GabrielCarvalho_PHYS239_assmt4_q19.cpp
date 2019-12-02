#include <iostream>
double root2minus1expansion( int n ) { return ( n <= 0 ) ? 0 : 1 / ( 2 + root2minus1expansion( n - 1 ) ); }
main() { for ( int i = 1; i < 11; i++ ) std::cout << "n = " << i << ": " << root2minus1expansion( i ) << std::endl; }
