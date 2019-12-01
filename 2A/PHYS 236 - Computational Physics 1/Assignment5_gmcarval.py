# Phys 236 Assignment 5 / Midterm Practice Problems
# Gabriel Carvalho
# 2018-10-16
print("Assignment 5 - Gabriel Carvalho")

import numpy
import matplotlib.pyplot as plt
from math import cos, sqrt, erfc, exp
import random

# This function just prints the question number in the console
def next_question(q):
    q += 1
    q_text = "Question "+str(q)+":"
    print(" ")
    print("----------")
    print(q_text)
    return q

question = 0

""" -------------------------------------------------------------------------------------------
1.  Write code in Python that loops over every number from 1 to 12, printing a message when
it reaches the 7th step.  Then modify this code to increment a floating point variable from 1.0
to 12.0 in steps of 1.0, printing a message when it comes to the 7th step.  Make sure you do
this in a 'safe' way, given you are comparing  floating point numbers.
"""
question = next_question(question)

# Loop through intergers 1 to 12, print a message at 7
r = range(1,13)
for step in r:
    if step == 7:
        print("'a message'")

# Loop through floats 1.0 to 12.0 in increments of 1.0
step2 = 1.0
while step2 < 12.5:
    # Print a message if step2 and 7.0 are very close together
    if abs(step2 - 7.0) < 10e-10:
        print("'a message'")
    step2 += 1.0

"""
2.  a) Print all the numbers from 0 to 200 that are divisible by 2 or 7, but not by 3.  b) Print
the integers from 1 to 20, raised to the power of 1.5.
"""
question = next_question(question)

print("Part a)")
part_a = []
for n in range(0,201):
    if (n % 2 == 0 or n % 7 == 0) and n % 3 != 0:
        part_a.append(n)
print(part_a)

print("Part b)")
part_b = []
n = 1.0
while n < 20.5:
    part_b.append(n**1.5)
    n += 1.0
print(part_b)

"""
3.  Write statements that generate the following sets of values as lists,  and then statements
that generate them as arrays:  (1.0,1.5,2.0,2.5,3.0,3.5), (-1,-2,-3,-4,-5,-6), (1,4,7,10,13,16).  Also
write a (user-defined) function that given a number N, returns an array of N evenly spaced values ranging
from (and including) 0 to pi.  Call your function to show it works.
"""
question = next_question(question)

# Define and print lists
l1 = [1.0,1.5,2.0,2.5,3.0,3.5]
print(l1)

l2 = []
for n in range(-1,-7,-1):
    l2.append(n)
print(l2)

l3 = []
for n in range(1,17,3):
    l3.append(n)
print(l3)

# Define and print arrays
a1 = numpy.arange(1.0,4.0,0.5)
print(a1)

a2 = numpy.arange(-1,-7,-1)
print(a2)

a3 = numpy.arange(1,17,3)
print(a3)

# Define and print function pi_range()
def pi_range(N):
    if N >= 3:
        pi_array = numpy.linspace(0.0,3.141592653589,N)
        return(pi_array)
    else:
        print("N must be equal to or greater than 3!")
pi_range_10 = pi_range(10)
print(pi_range_10)

"""
4.  Given a 2-D array of 9 rows by 8 columns, write expressions for the following slices:  a) the
last 3 rows, b) the  first five elements of the first two rows, c) the last 3 elements of row 7.
"""
question = next_question(question)

# Make a 9 by 8 array
array98 = numpy.zeros([9,8],int)
# Fill the array with numbers representative of their coordinates
for i in range(0,9):
    for j in range(0,8):
        pos98 = 10*(i+1)+(j+1)
        array98[i,j] = pos98
print("Original Array:")
print(array98)

# Make slices of the array
print("Slice 1:")
array98_s1 = array98[6:, :]
print(array98_s1)

print("Slice 2:")
array98_s2 = array98[:2, :5]
print(array98_s2)

print("Slice 3:")
array98_s3 = array98[6:7, 5:]
print(array98_s3)

"""
5.  Using Python, plot the function f(x)=cos(x^2)/(1+x^2) between -5 and +5, with appropriately
scaled axes, labels, tickmarks etc.
"""
question = next_question(question)

# Get the x anf y values to plot
xx5 = []
yy5 = []

n = -5.0
step_size = 0.1
while n < 5.0+step_size/2:
    xx5.append(n)
    yy5.append(cos(n**2)/(1+n**2))
    n += step_size

# Plot the function
plt.plot(xx5,yy5)
plt.title("Plot of f(x)=cos(x^2)/(1+x^2)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.xticks(range(-5,6,1))
plt.show()

"""
6.  Write your own factorial function in Python, and use it to make a plot of factorial of the
integers from 1 to 16, joined together as a continuous curve.  (You will need to log the y-axis
to get a reasonable plot.)  Compare the resulting curve to the function f(x)-exp(x^1.5 / 2),
drawn as a dashed line on the same plot
"""
question = next_question(question)


"""
7.  Given a data file (which you can create yourself) with 30 integer or floating point values
distributed between 0 and 100, each on one line, write a Python code to read in the file, create
a histogram of the values with sensible binning, and plot the result.  You can use the function
hist() from pylab to do this.
"""
question = next_question(question)

# Generate 100 random numbers from 1 to 100
data = []
for i in range(0,100):
    data.append(random.randint(1,101))

# Create a histogram of the random numbers
n,bins,patches = plt.hist(data,10)
plt.show()


"""
8.  Suppose my average course mark is 82 with an r.m.s.  of sigma = 10, and I have taken 20 courses.
How well determined is my average?  (i.e. what is the uncertainty or error associated with this average?)
"""
question = next_question(question)

# the error in the mean is the r.m.s. divided by the square root of the number of measurements
sigma = 10
N = 20
delta = sigma/sqrt(N)
print("Uncertainty:",delta)

"""
9.  Suppose an experiment gets one 4.0 sigma detection of a new particle,  and another gets
a 4.8 sigma detection.  What is the significance (in sigma) of both measurements considered
together?  (You can assume the probabilities multiply.)
"""
question = next_question(question)

from scipy import special

P1 = erfc(4.0/sqrt(2.0))
P2 = erfc(4.8/sqrt(2.0))
sigma3 = special.erfcinv(P1*P2)
print("Combined Significance:",sigma3,"sigma")

"""
10.  I have several measurements of a quantity:  value #1 is 1.0+-0.3, value #2 is 0.5+-0.3,
and value #3 is 1.5+-0.5.  Which measurements are consistent with one another?  What is
the probability of getting value #3, assuming value #2 is correct?  What is the probability of
getting value #2,  assuming value #3 is correct?  (You can assume Gaussian statistics,  with
each error corresponding to the 1-sigma r.m.s.)
"""
question = next_question(question)

# 1 and 2 are consistent, and 1 and 3 are consistent
# If 2 is correct, the value is 0.5 and one error bar is 0.3
#   Value 3 is 1.0 away from value 2, which is 3.33333 error bars
#   Find the probability for a 3.33333 sigma event:
P1 = erfc(3.33333/sqrt(2.0))
print("Probability of case 1:",P1)

# If 3 is correct, the value is 1.5 and one error bar is 0.5
#   Value 2 is 1.0 away from value 3, which is 2 error bars
#   Find the probability for a 2 sigma event:
P2 = erfc(2.0/sqrt(2.0))
print("Probability of case 2:",P2)

"""
11.  If the formula for a quantity is f=xy/z, and I have relative errors of 3% in x, 5% in y,
and 2% in z, what is the relative error in f, assuming the three variables are uncorrelated?
(You will need to review the rules for error propagation.)  What would it be if x and y were
completely correlated,  so that a larger/smaller value in one corresponds to a larger/smaller
value in the other?
"""
question = next_question(question)



"""
12.  Suppose I  t a line to data and get a chi^2 of 20.0. I then change the slope of the line slightly
and get a chi^2 of 21.0. Based on the definition of chi^2, how much less likely is this second model,
given the data?
"""
question = next_question(question)

# logP = const - (1/2)chi2
# e^logP = e^(const - (1/2)chi2)
# P = [ e^const ] * [ e^-(1/2)chi2 ]
# P2/P1 = [ e^-(1/2)chi2_2 ]/[ e^-(1/2)chi2_1 ]
# P2/P1 = e^( (1/2)chi2_1 - (1/2)chi2_2 )
# P2/P1 = e^(1/2 * [chi2_1 - chi2_2])
chi2_1 = 20.0
chi2_2 = 21.0
prob = exp(0.5 * (chi2_1 - chi2_2))
print("Ratio of probabilities:",prob)
print("A chi2 of 21.0 is",round(prob*100),"percent as likely as a chi2 of 20.0")

"""
13.  Suppose I flip a coin 5 times; what is the probability of getting 3 heads? (Hint:  review the
binomial distribution in unit 8.)
"""
question = next_question(question)

# binomial distribution problem
def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n*factorial(n-1)

def binomial_dist(k,n,p):
    return factorial(n)/(factorial(k)*factorial(n-k)) * (p**k)*(1-p)**(n-k)
# where k is the number of positive outcomes, n is the number of trials,
# and p is the probability of a positive outcome

print("Chance of getting 3 heads in in 5 flips:",binomial_dist(3,5,0.5))

"""
14.  Suppose a tornado hits Waterloo once every  fty years on average.  What is the probability
of getting two tornados in ten years? (Hint:  review the Poisson distribution in unit 8.)
"""
question = next_question(question)

# poisson distribution problem
def poisson(k,lam):
    return lam**k/factorial(k)*exp(-lam)
# where k is the number of events on an interval,
# and lambda is the mean rate of the event on that interval

print("Chance of 2 tornados in a year:",poisson(2,1/50))


"""
15.  Discuss how the final statements in each of the sections of code below differ in detail.
    a = 1.0
    b = a
and
    a = zeros(10)
    for i in range(10):   a[i] = i*2.5
    b = a
"""
question = next_question(question)