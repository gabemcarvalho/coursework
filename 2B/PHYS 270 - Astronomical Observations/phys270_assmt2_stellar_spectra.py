from numpy import loadtxt, linspace, log10, exp, power
import matplotlib.pyplot as plt

"""

Stellar Spectrum Analyzing Program for PHYS270 Assigment 2
author: Gabriel Carvalho
last updated: 2019-05-31

Input: [ Wavelength (angstroms), Flux (W/m^2/A) ]
Output:


"""

# FUNCTIONS -------------------------------------------------------------------

# photon flux from flux of W/m^2 and wavelength in angstroms
def photonFlux( flux_density, wavelength ):
    h = 6.62607004e-34 # planck's constant
    c = 299792458 # speed of light
    e_photon = h * c / (wavelength * 1e-10)
    return flux_density / e_photon

# sums the photon counts for G, R, and I filters with flux inputted as W/m^s/A
def sumPhotons( wavelengths, flux, band_width ):
    G = 0; R = 0; I = 0;
    for i in range( len( wavelengths ) ):
        w = wavelengths[i]
        if (w >= 4000.0 and w <= 5400.0): # g band
            G += photonFlux( flux[i] * band_width, w )
        if (w >= 5500.0 and w <= 6850.0): # r band
            R += photonFlux( flux_star[i] * band_width, w )
        if (w >= 6700.0 and w <= 8250.0): # i band
            I += photonFlux( flux_star[i] * band_width, w )
    return [G, R, I]

def sumFlux( wavelengths, flux, band_width ): # flux in W/m^2/A
    G = 0; R = 0; I = 0;
    for i in range( len( wavelengths ) ):
        w = wavelengths[i]
        if (w >= 4000.0 and w <= 5400.0): # g band
            G += flux[i] * band_width
        if (w >= 5500.0 and w <= 6850.0): # r band
            R += flux[i] * band_width
        if (w >= 6700.0 and w <= 8250.0): # i band
            I += flux[i] * band_width
    return [G, R, I]

# flux of a blackbody in W/m^2
def blackbodySpectrum( wavelength, T ):
    h = 6.62607004e-34 # planck's constant
    c = 299792458 # speed of light
    k = 1.380649e-23 # boltzmann constant
    return 2.0 * h * c * c / power( wavelength, 5.0 ) / ( exp( h * c / ( wavelength * k * T ) ) - 1.0 )

# PROGRAM ---------------------------------------------------------------------

# PART A: photon counts for unknown star
# load unknown star data and initialize variables
data_star = loadtxt( "phy270_ass2_spectrum.txt", float ) # [ Wavelength, Flux ]
wavelengths_star = data_star[:,0]
flux_star = data_star[:,1]
#pG_star = 0; pR_star = 0; pI_star = 0

# sum photons for each filter
pG_star, pR_star, pI_star = sumPhotons( wavelengths_star, flux_star, 5.0 )

# print info
print( "Photon Counts For Unknown Star:" )        
print( "G: " + str( pG_star ) )
print( "R: " + str( pR_star ) )
print( "I: " + str( pI_star ) )
print( "-----" )

# PART B: vega magnitude of unknown star
# load vega data and initialize more variables
data_vega = loadtxt( "vega.txt", float )
wavelengths_vega = data_vega[:,0]
flux_vega = data_vega[:,1]
#fG_star = 0; fR_star = 0; fI_star = 0
#fG_vega = 0; fR_vega = 0; fI_vega = 0

# sum flux through filters for both stars
fG_star, fR_star, fI_star = sumFlux( wavelengths_star, flux_star, 5.0 )
fG_vega, fR_vega, fI_vega = sumFlux( wavelengths_vega, flux_vega, 5.0 )

# print info
print( "Unknown Star Flux (W/m^2):" )        
print( "Fg = " + str( fG_star ) )
print( "Fr = " + str( fR_star ) )
print( "Fi = " + str( fI_star ) )
print( "-----" )
print( "Vega Flux (W/m^2):" )        
print( "Fg = " + str( fG_vega ) )
print( "Fr = " + str( fR_vega ) )
print( "Fi = " + str( fI_vega ) )
print( "-----" )

# calculate relative magnitudes
mG_star = -2.5 * log10( fG_star / fG_vega )
mR_star = -2.5 * log10( fR_star / fR_vega )
mI_star = -2.5 * log10( fI_star / fI_vega )
G_R_star = mG_star - mR_star
R_I_star = mR_star - mI_star

# print info
print( "Vega Magnitudes of Unknown Star:" )        
print( "mG = " + str( mG_star ) )
print( "mR = " + str( mR_star ) )
print( "mI = " + str( mI_star ) )
print( "G-R = " + str( G_R_star ) )
print( "R-I = " + str( R_I_star ) )
print( "-----" )

# some plots cause why not
vega_lambdaF = []
for i in range( len( wavelengths_vega ) ):
    vega_lambdaF.append( flux_vega[i] * wavelengths_vega[i] * 1e-10 )
star_lambdaF = []
for i in range( len( wavelengths_star ) ):
    star_lambdaF.append( flux_star[i] * wavelengths_star[i] * 1e-10 )
plt.plot( wavelengths_vega, vega_lambdaF )
plt.plot( wavelengths_star, star_lambdaF )
plt.title( "Star Spectra" )
plt.xlabel( "Wavelength (Angstroms)" )
plt.ylabel( "Flux Density * Wavelength" )
plt.grid(True)
plt.show()
print( "-----" )

# PART C: blackbody radiation
T_values = linspace( 5000, 20001, 50 )
G_R_bb_values = []
R_I_bb_values = []

for T_current in T_values:
    bb_wavelengths = []
    bb_flux = []
    for i in range( 1000, 9000, 5 ):
        bb_wavelengths.append( i )
        bb_flux.append( blackbodySpectrum( i * 1e-10, T_current ) )
        
    fG_bb, fR_bb, fI_bb = sumFlux( bb_wavelengths, bb_flux, 5e-10 )
    mG_bb = -2.5 * log10( fG_bb / fG_vega )
    mR_bb = -2.5 * log10( fR_bb / fR_vega )
    mI_bb = -2.5 * log10( fI_bb / fI_vega )
    
    G_R_bb_values.append( mG_bb - mR_bb )
    R_I_bb_values.append( mR_bb - mI_bb )

print( "Vega Magnitudes of a Blackbody:" )
G_R_line = []
R_I_line = []
for i in T_values:
    G_R_line.append( G_R_star )
    R_I_line.append( R_I_star )
plt.plot( T_values, G_R_bb_values )
plt.plot( T_values, G_R_line )
plt.title( "Blackbody g-r vs. T" )
plt.xlabel( "Temperature (K)" )
plt.ylabel( "g-r" )
plt.grid(True)
plt.show()
plt.plot( T_values, R_I_bb_values )
plt.plot( T_values, R_I_line )
plt.title( "Blackbody r-i vs. T" )
plt.xlabel( "Temperature (K)" )
plt.ylabel( "r-i" )
plt.grid(True)
plt.show()
print( "-----" )










