from numpy import loadtxt, power, sqrt, linspace, exp, arange
import matplotlib.pyplot as plt
from math import factorial

# QUESTION 1 ------------------------------------------------------------------
def poisson(events, rate):
    p = exp(-rate) * power(rate, events) / factorial(events)
    return p

def gaussian(var, mean, x):
    p = 1 / sqrt( 2*3.14159265359 ) / var * exp( - power( x - mean, 2 ) / 2 / power( var, 2 ) )
    return p

# PART B AND C ----------------------------------------------------------------
k = range( 0, 21 )
p = []
for i in k:
    p.append( poisson( i, 5.2 ) )
    
print("sum = "+str(sum(p)))    

plt.plot( k, p )
plt.title("Poisson Distrubution for rate = 5.2")
plt.show()

delta = 0.1
mu = arange(0,20.1,delta)
p2 = []
pAbove10 = 0
for i in mu:
    val = poisson( 6, i )
    p2.append( val )
    if i > 10:
        pAbove10 += delta * val
    
print("p2 sum = "+str(sum(p2)*delta))  

plt.figure(figsize=(16, 6), dpi=80)
plt.plot( mu, p2 )
plt.title("Figure 1: Probability of True Photon Rate")
plt.xlabel("rate in photons/second")
plt.ylabel("probability")
plt.grid(True)
plt.show()

print("prob. of rate greater than 10: "+str(pAbove10))

# PART D ----------------------------------------------------------------------
x = arange(4.0,8.01,0.01)
mean = 6
var = 0.06
p3 = []
for i in x:
    val = gaussian( var, mean, i )
    p3.append( val )

plt.figure(figsize=(16, 6), dpi=80)
plt.plot( x, p3 )
plt.title("Figure 2: Probability Distribution of Flux with 1% Uncertainty")
plt.xlabel("r [photons/second]")
plt.ylabel("P(r)")
plt.grid(True)
plt.show()


# QUESTION 3 ------------------------------------------------------------------
data = loadtxt("phy270_a5_q3_data.txt", float)
xx = data[:,0]
yy = data[:,1]
dy = data[:,2]

# weighted mean
mean = 0
var = 0
for i in range(0,len(xx)):
    mean += yy[i] / power( dy[i], 2 )
    var += 1 / power( dy[i], 2 )
    
mean /= var
var = sqrt( 1 / var )

print("mean = "+str(mean)+" +- "+str(var))

# chi-squared
chi_squared = 0;
for i in range(0,len(xx)):
    chi_squared += power( yy[i] - mean, 2 ) / power( dy[i], 2 )
    
reduced_chi_squared = chi_squared / ( len(xx) - 1 )

print("chi-squared = "+str(chi_squared))
print("reduced chi-squared = "+str(reduced_chi_squared))

# linear fit
m_best = 0
b_best = 0
chi2_best = 10000000
for m in linspace(0.3,0.4,101):
    for b in linspace(-6,-5.9,101):
        chi2 = 0;
        for i in range(0,len(xx)):
            chi2 += power( yy[i] - ( m * xx[i] + b ), 2 ) / power( dy[i], 2 )
        if chi2 < chi2_best:
            chi2_best = chi2
            m_best = m
            b_best = b

print("m = "+str(m_best))
print("b = "+str(b_best))
print("linear chi2 = "+str(chi2_best))
print("reduced linear chi2 = "+str(chi2_best/8))


plt.figure(figsize=(16, 6), dpi=80)
plt.plot( xx, yy, 'bo', label='data' )
plt.errorbar( xx, yy, yerr=dy, fmt='o')
plt.plot( [18,26], [mean, mean], c='k', ls='-', label='mean' )
plt.plot( [18,26], [mean-var, mean-var], c='k', ls='--' )
plt.plot( [18,26], [mean+var, mean+var], c='k', ls='--' )
plt.plot( [18,26], [m_best*18+b_best, m_best*26+b_best], c='m', ls='-', label='linear fit' )
plt.title("Figure 3: Plot of Colour vs Magnitude")
plt.xlabel("magnitude")
plt.ylabel("colour")
plt.legend()
plt.grid(True)
plt.show()

