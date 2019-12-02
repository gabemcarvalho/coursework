#include <iostream>
double f(int n){return(n<=0)?0:1/(2+f(n-1));}
main(){for(int i=1;i<11;i++)std::cout<<"n="<<i<<": "<<f(i)<<std::endl;}
