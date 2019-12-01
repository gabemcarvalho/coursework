from numpy import log10, exp, linspace
import matplotlib.pyplot as plt

"""

PHYS 270 Assignment 2 - Question 2 Plot - Image Size vs. Wavelength For Various Telescopes
by Gabriel Carvalho
2019-06-15

"""

# r in cm, lmbda in nm, object at zenith, returns arcseconds
def totalFriedSeeing( r, lmbda ):
    return pow( r / 10, -1 ) * pow( lmbda / 500, -1/5 )

# D in m, lmbda in nm, returns arcseconds
def resolutionLimit( D, lmbda ):
    return 2 * 1.22 * lmbda * 1e-9 / D * 206265

x = range( 300, 901, 5 )

yA = []
yB = []
yC = []
yD = []

for i in x:
    yA.append( max ( totalFriedSeeing( 15, i ), resolutionLimit( 3.5, i ) ) )
    yB.append( max ( totalFriedSeeing( 10, i ), resolutionLimit( 0.2, i ) ) )
    yC.append( resolutionLimit( 30, i ) )
    yD.append( resolutionLimit( 6.5, i ) )

plt.figure(figsize=(8, 6), dpi=80)
plt.plot(x, log10( yA ), "r-")
plt.plot(x, log10( yB ), "b-")
plt.plot(x, log10( yC ), "g-")
plt.plot(x, log10( yD ), "m-")
plt.grid(True)
plt.title("Figure 1: Image Size vs. Wavelength")
plt.xlabel("Wavelength (nm)")
plt.ylabel("Point Source Diamter in log10( arcsec )")
plt.legend(["A","B","C","D"])
plt.show()


"""

Question 3 Plot - Thermal Background in AB Mag/arcsec^2 vs. Wavelength

"""

def wavelengthToABMagPerArcsecSquared( lmbda, T ):
    h = 6.62607015e-34
    k = 1.38064852e-23
    c = 299792458
    v = c / lmbda
    
    # Iv = intensity in watts per meter squared per square radian
    Iv = 2 * h * v*v*v / ( c*c ) / ( exp( h * v / ( k * T ) ) - 1 )
    Iv_arcsec = Iv / 42545250225
    
    return -2.5 * log10( Iv_arcsec ) - 56.1

lmbda_values = linspace( 1.0, 10.0, 100 )
bg_T293 = []
bg_T243 = []
#bg_T50  = []
for i in lmbda_values:
    bg_T293.append( wavelengthToABMagPerArcsecSquared( i * 1e-6, 293.15 ) )
    bg_T243.append( wavelengthToABMagPerArcsecSquared( i * 1e-6, 243.15 ) )
    #bg_T50.append( wavelengthToABMagPerArcsecSquared( i * 1e-6, 50 ) )
    
plt.figure(figsize=(8, 6), dpi=80)
plt.plot( lmbda_values, bg_T293, "r-" )
plt.plot( lmbda_values, bg_T243, "b-" )
#plt.plot( lmbda_values, bg_T50, "y-" )
plt.title("Figure 2: Thermal Background vs. Wavelength")
plt.xlabel("Wavelength (um)")
plt.ylabel("AB mag/arcsec^2")
#plt.legend(["20C","-30C","50K"])
plt.legend(["20C","-30C"])
plt.grid(True)
plt.show()
    

















    

