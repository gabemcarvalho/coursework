from numpy import loadtxt, cos, pi, linspace, sqrt
import matplotlib.pyplot as plt

"""

Parallax Curve Fitting Program
by Gabriel Carvalho
2019-05-17

Input: [ Days, RA offset (mas), Dec offset (mas) ]
Output:
- graphs of data with individual components and extrapolated curves
- parallax radius
- proper motion in components and combined

Stuff that's still hardcoded:
- initial estimate for wave amplitude
- test values for amplitude and slope
- initial upper bound on error
- range of extrapolated curve

"""

# FUNCTIONS -------------------------------------------------------------------

# y(x) = R * cos(x + phi) + mx + b
def curve(day, R, phi, m, b):
        return R * cos( day * 2.0 * pi / 365.256 + phi ) + m * day + b
    
# given some data, calculates a fit for the curve
def fit(days, y_data, precision):
    
    # initialize variables (with some initial values to help)
    R = 150
    phi = 0
    m = ( y_data[len( y_data )-1] - y_data[0] ) / ( days[len(days)-1] - days[0] )
    b = y_data[0]
    
    # initial guess graph
    fit_data = []  
    for d in days:
        fit_data.append( curve( d, R, phi, m, b ) )
        
    plt.plot(days, y_data, "ko")
    plt.plot(days, fit_data, "b-")
    plt.title("Initial Guess")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()
    
    # find phase offset
    print( "[FIRST PASS] computing phase adjustment..." )
    phi_values = linspace( 0.0, 2.0 * pi, precision )
    phi = compute_phase(days, y_data, phi_values, R, m, b)
    
    # find amplitude and slope
    print( "[FIRST PASS] computing amplitude and slope..." )
    R_values = linspace( 100.0, 150.0, precision )
    m_values = linspace( 0.4, 1.0, precision )
    Rmb = compute_Rmb(days, y_data, R_values, m_values, phi)
    R = Rmb[0]
    m = Rmb[1]
    b = Rmb[2]
    
    # find phase offset (second pass)
    print( "[SECOND PASS] computing phase adjustment..." )
    phi_values = linspace( phi - pi / 4.0, phi + pi / 4.0, precision )
    phi = compute_phase(days, y_data, phi_values, R, m, b)
    
    # find amplitude and slope (second pass)
    print( "[SECOND PASS] computing amplitude and slope..." )
    R_values = linspace( R - 10.0, R + 10.0, precision )
    m_values = linspace( m * 0.8, m * 1.2, precision )
    Rmb = compute_Rmb(days, y_data, R_values, m_values, phi)
    R = Rmb[0]
    m = Rmb[1]
    b = Rmb[2]
    
    print( "R: " + str(R) )        
    print( "phi: " + str(phi) )
    print( "m: " + str(m) )
    print( "b: " + str(b) )
    
    return [ R, phi, m, b ]

def compute_phase(days, y_data, phi_values, R, m, b):
    error = 10000000.0
    phi = 0
    for i in phi_values:
        
        # generate curve
        y = []
        for d in days:
            y.append( curve( d, R, i, m, b ) )
        
        # this is a pretty basic error sum, but it's good enough
        # calculate error and set values if it has been lowered
        new_error = sum( abs( y_data - y ) )
        if new_error < error:
            error = new_error
            phi = i
    
    return phi

def compute_Rmb(days, y_data, R_values, m_values, phi):
    error = 10000000.0
    R = 0
    m = 0
    b = 0
    for i in m_values:
        for j in R_values:
            
            # set y position of first point to same as data
            b_new = y_data[0] - j * cos( days[0] * 2.0 * pi / 365.256 + phi )
            
            # generate curve
            y = []
            for d in days:
                y.append( curve( d, j, phi, i, b_new ) )
                
            # calculate error and set values if it has been lowered
            new_error = sum( abs( y_data - y ) ** 2 )
            if new_error < error:
                error = new_error
                m = i
                R = j
                b = b_new
    
    return [ R, m, b ]

# PROGRAM ---------------------------------------------------------------------

# get raw data
data = loadtxt("data_parallax.txt",float) # [ Days, RA offset (mas), Dec offset (mas) ]
days = data[:,0]
RA = data[:,1]
Dec = data[:,2]

# precision
precision = 101

# calculate fit for RA vs days
print( "computing fit for RA vs time..." )
RA_fit = fit( days, RA, precision )

# graph for RA vs days
RA_fit_data = []
test_days = linspace( -500.0, 1500.0, 201 )
for d in test_days:
    RA_fit_data.append( curve( d, RA_fit[0], RA_fit[1], RA_fit[2], RA_fit[3] ) )

plt.figure(figsize=(8, 6), dpi=80)
plt.plot(days, RA, "ko")
plt.plot(test_days, RA_fit_data, "b-")
plt.title("RA vs time")
plt.xlabel("t (days)")
plt.ylabel("RA (mas)")
plt.show()


# calculate fit for Dec vs days
print( "computing fit for Dec vs time..." )
Dec_fit = fit( days, Dec, precision )

# graph for RA vs days
Dec_fit_data = []  
for d in test_days:
    Dec_fit_data.append( curve( d, Dec_fit[0], Dec_fit[1], Dec_fit[2], Dec_fit[3] ) )

plt.figure(figsize=(8, 6), dpi=80)
plt.plot(days, Dec, "ko")
plt.plot(test_days, Dec_fit_data, "b-")
plt.title("Dec vs time")
plt.xlabel("t (days)")
plt.ylabel("Dec (mas)")
plt.show()


# final plot
plt.figure(figsize=(8, 6), dpi=80)
plt.plot(Dec, RA, "ko")
plt.plot(Dec_fit_data, RA_fit_data, "b-")
plt.title("Parallax of a Star")
plt.xlabel("Dec (mas)")
plt.ylabel("RA (mas)")
plt.show()
print( "parallax radius: " + str( 0.5 * (RA_fit[0] + Dec_fit[0]) ) + " mas" )
print( "RA proper motion: " + str( RA_fit[2] * 365.256 ) + " mas/year" )
print( "Dec proper motion: " + str( Dec_fit[2] * 365.256 ) + " mas/year" )
print( "Total proper motion: " 
      + str( sqrt( Dec_fit[2]**2 + RA_fit[2]**2 ) * 365.256 ) + " mas/year" )
print( "" )
print( "done!" )
