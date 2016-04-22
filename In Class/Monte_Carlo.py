from random import random
from math import sin

A = 2.0
N = 100000
k = 0.0

def function(x):
    return sin(1.0/(x*(2-x)))**2

for point in range(N):
    x = 2*random()
    y = random()

    if y <= function(x):
        k += 1

I = k*A/N

print("Integral: ", I)