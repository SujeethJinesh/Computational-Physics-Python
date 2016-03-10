from numpy import arange
from pylab import plot, show, xlabel, ylabel
from math import sin

x = 0.0
a = 0.0
b = 10.0
N = 100
xx = []
h = (b-a)/N
t = arange(a,b,h)

def f(x,t):
    return -x**3 + sin(t)

for i in t:
    k1 = h*f(x,i)
    k2 = h*f(x+0.5*k1,i+0.5*h)
    x += k2
    xx.append(x)

plot(t, xx)
xlabel("t")
ylabel("x(t)")
show()