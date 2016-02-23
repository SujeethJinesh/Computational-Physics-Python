from __future__ import print_function, division
from gaussxw import *

N = 3
a = 0.0
b = 2.0

xp, wp = gaussxwab(N, a, b)

summation = sum(wp*function(xp))

print(summation)

def function(number):
    return (pow(number, 4) - 2*number + 1)