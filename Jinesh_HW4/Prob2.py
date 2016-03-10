from mailcap import show

import math #necessary imports
from numpy import arange, linspace
from sympy import plot

x1 = 1
x2 = 1
target = 1e-6

#function to evaluate
def f(x):
    return (1 - math.exp(-2*x)) - x
#derivative of said function
def df(x):
    return 2*math.exp(-2*x) - 1
#setting tolerance and initial conditions
e=1.0e-6
x1=0
#actual performance of newton's method
while True:
    x1=x2
    x2=x1-f(x1)/df(x1)
    if abs(x2-x1) < target:
        break

print(x2) #final answer printed out

############################################################
#part b

points = []
y = [];

def new_f(x,c):
    return (1 - math.exp(-c*x) - x)

def new_df(x, c):
    return c*math.exp(-c*x) - 1

for c in linspace(0,3,3):
    x1 = 1
    x2 = 1
    target = 1e-6
    points.append(c)
    while True:
        x1=x2
        x2=x1-new_f(x1, c)/new_df(x1, c)
        if abs(x2-x1) < target:
            if x2 is not None:
                y.append(x2)
            else:
                y.append(0)
                break

plot(points, y)
show()