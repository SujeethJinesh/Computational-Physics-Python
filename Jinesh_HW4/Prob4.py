from pylab import plot,show,xlabel,ylabel
from numpy import linspace #necessary imports
from math import pow

#initial arrays for size
xs = []
ys = []

#function to find roots
def P(x):
    return (924*pow(x,6.0) - 2772*pow(x,5.0) + 3150*pow(x,4.0) - 1680*pow(x,3.0) + 420*pow(x,2.0) - 42*x + 1)

#adding in values to make plot
for i in linspace(0,1,10000):
    xs.append(i)
    ys.append(P(i))

plot(xs,ys)
xlabel('u')
ylabel('result')
show()

#calculates the values for newton's method

#derivative of P(x)
def dP(x):
    return (924*6*pow(x,5.0) - 2772*5*pow(x,4.0) + 3150*4*pow(x,3.0) - 1680*3*pow(x,2.0) + 420*2*x - 42)

#takes in start value to calculate from where the root should be to nearest consecutive root
def roots(start):
    e=1e-8
    x1 = start
    while True:
        x2=x1-P(x1)/dP(x1)
        if(abs(x2-x1)<e):
            break
        x1=x2
    print x2