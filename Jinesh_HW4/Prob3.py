from __future__ import division,print_function #necessary import

#defining constants
G = 6.674e-11
M = 5.974e24
m = 7.348e22
R = 3.844e8
omega = 2.662e-6

#function to evaluate
def f(r):
    return G*M/(r ** 2.0) - G*m/(R-r)**2.0 - (omega ** 2.0)*r
#derivative of said function
def df(r):
    return -2.0*G*M/(r**3.0) - 2.0*G*m/(R-r)**3.0 - (omega**2.0)
#setting tolerance and initial conditions
e=1.0e-5
x1=3.0e8
x2=x1-f(x1)/df(x1)
#actual performance of newton's method
while True:
    x1=x2
    x2=x1-f(x1)/df(x1)
    if abs(x2-x1) < e:
        break

print(x2) #final answer printed out