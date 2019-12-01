# PHYS 256L - Experiment 3 Part C Graph
import numpy
import matplotlib.pyplot as plt

P = [2.17,8.17,17.17,25.17,33.17,42.50,50.83,60.17]
aP = numpy.asarray(P)
#aP = aP+8.61
P_uncert = [1.15,1.15,1.15,1.15,1.15,1.15,1.15,1.15]
aP_uncert = numpy.asarray(P_uncert)
mu = [0,2.947,5.893,8.840,11.786,14.733,17.679,20.626]
amu = numpy.asarray(mu)

# already did calculation, result below
if 0 == 0:
    i = numpy.linspace(0.1,0.5,300)
    j = numpy.linspace(-10,10,300)
    chi2_low = 10000;
    a_low = 0;
    b_low = 0;
    for a in i:
        for b in j:
            m = a*aP+b
        
            d = (mu-m)/1.0
            d2 = d*d
            chi2 = sum(d2)/2.0
            
            if chi2 < chi2_low:
                chi2_low = chi2
                a_low = a
                b_low = b

#a_low = 0.3515050167224081
#b_low = -0.21070234113712383

m = a_low*aP+b_low
print("Slope =",a_low)
print("Y-int =",b_low)

plt.plot(aP,amu,"ko")
plt.plot(aP,m,"k-")
plt.errorbar(aP,amu,xerr=P_uncert,yerr=0,fmt=' o')
plt.title("Graph 1. Index of Refraction of Air versus Pressure")
plt.xlabel("Pressure (cm of mercury)")
plt.ylabel("Index of Refraction - 1 (x10^-5)")
plt.grid(True)
plt.text(38, 11, r'$m=0.350167224$', fontsize=10)
plt.figure(figsize=(20,10))
#plt.xticks(range(-5,6,1))
plt.show()
