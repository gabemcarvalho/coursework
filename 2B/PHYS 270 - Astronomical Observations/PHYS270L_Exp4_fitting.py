from numpy import loadtxt, sin, linspace, sqrt, power
import matplotlib.pyplot as plt

def f( A, period, phase, t ):
    return A * sin( 2 * 3.14159265 / period * t + phase )

def chi2( y, expected, error ):
    return power( y - expected, 2 ) / power( error, 2 )

data = loadtxt("callisto.txt",float)
times = data[:,0]
dist = data[:,1]
error = data[:,2]
n = len( times )
period = 5113.7

tmin = -500
tmax = 4000
phase_values = linspace( 0, 2*3.14159265, 101 )
A_values = linspace( 150, 250, 101 )

phase_best = 0
A_best = 0
chi2_min = 10000000

for phase in phase_values:
    for A in A_values:
        chi2_val = 0
        for i in range( 0, n ):
            chi2_val += chi2( dist[i], f( A, period, phase, times[i] ), error[i] )
        if ( chi2_val < chi2_min ):
            chi2_min = chi2_val
            phase_best = phase
            A_best = A
            
print( "A = " + str( A_best ) )
print( "phase = " + str( phase_best ) )
print( "chi2 = " + str( chi2_min ) )

plot_times = linspace( tmin, tmax, 101 )
plot_y = f( A_best, period, phase_best, plot_times )


plt.figure(figsize=(10, 6), dpi=80)
plt.plot( times, dist, 'bo', label='data' )
plt.errorbar( times, dist, yerr=error, fmt='o')
plt.plot( plot_times, plot_y, label='fit' )
plt.title("Figure 2: Position vs. Time for Europa")
plt.xlabel("position [arcsec]")
plt.ylabel("time [min]")
plt.legend()
plt.grid(True)
plt.show()
