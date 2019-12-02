from astropy.io import fits
from numpy import median, loadtxt, sqrt, linspace
from photutils import aperture_photometry, CircularAperture, CircularAnnulus
import matplotlib.pyplot as plt

hdul = fits.open( 'phy270_ass6.fits' )
image = hdul['SCI'].data
print( "imported data" )

mid_val = median( image )
print( "median = " + str( mid_val ) )

coords = loadtxt( 'phy270_ass6.coords' )
apertures = CircularAperture( coords, r=1.5/0.16 )
annuli = CircularAnnulus( coords, 5.0/0.16, 10.0/0.16  )
phot_table = aperture_photometry(image, apertures)
bknd_table = aperture_photometry(image, annuli)
print( "apertures:" )
print( phot_table )
print( "background annuli:" )
print( bknd_table )
print( bknd_table['aperture_sum'] / 9203.9 )

print( "done" )

def sigNoiseRatio( t, s, b, n, ro ):
    return s * t / sqrt( s * t + n * ( b * t + ro * ro ) )

for i in [ 1, 10, 100 ]:
    range1 = linspace( 0, 1000, 1001 )
    ratios1 = sigNoiseRatio( range1, i, 10.06, 276.1, 6 )
    
    plt.title( "signal = " + str(i) )
    plt.xscale( "log" )
    plt.yscale( "log" )
    plt.xlabel( "time (s)" )
    plt.ylabel( "signal-to-noise ratio" )
    plt.grid()
    plt.plot( range1, ratios1 )
    plt.show()

print( str(image.shape) )

src_counts = phot_table['aperture_sum']
bknd_counts = bknd_table['aperture_sum']

src_flux = ( src_counts - bknd_counts * 276.1 / 9203.9 ) / 600
#src_error = sqrt( src_counts / 3 + bknd_counts / 3 * ( 276.1 / 9203.9 )**2 + ( 276.1 * 6 )**2 )
src_error = sqrt( src_counts / 3 + 94.8 * bknd_counts / 9203.9 + 10238 ) / 600
#src_error = sqrt( src_counts / 3 + 276.1**2 * ( 1 + 1/9203.9 ) * ( bknd_counts/9203.9 + 36 ) ) / 600

snr = src_flux / src_error

print( src_flux )
print( src_error )
print( snr )

# linear fit
m_best = 0
b_best = 0
chi2_best = 10000000
for m in linspace(0,1,1001):
    for b in linspace(0,10,1001):
        chi2 = 0;
        for i in range(0,len(src_flux)):
            chi2 += ( snr[i] - ( m * src_flux[i] + b ) )**2
        if chi2 < chi2_best:
            chi2_best = chi2
            m_best = m
            b_best = b

print("m = "+str(m_best))
print("b = "+str(b_best))



plt.title( "S/N vs. Source Flux " )
plt.xlabel( "flux" )
plt.ylabel( "signal-to-noise ratio" )
plt.grid()
plt.plot( src_flux, snr, "bo" )
plt.plot( linspace(0,1300,2), linspace(0,1300,2)*m_best+b_best, "m-" )