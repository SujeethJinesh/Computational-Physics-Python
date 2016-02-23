from math import sin
import numpy as np

a = 0.0
b = 1.0

def Trapezoidal_Rule(n):
    h = (b - a) / n
    x = a
 
    summation = function(a)
    for i in range(1, n):
        x  = x + h
        summation = summation + 2*function(x)
 
    return (summation + function(b))*h*0.5

def function(number):
    return sin((100*number) ** 0.5) ** 2.0 
 
def romberg(numRows):

    I = np.zeros((numRows, numRows))
    for k in range(0, numRows):

        I[k, 0] = Trapezoidal_Rule(2**k)
 
        for j in range(0, k):
            I[k, j+1] = (4**(j+1) * I[k, j] - I[k-1, j]) / (4**(j+1) - 1)
 
        print(I[k,0:k+1])
 
    return I

def calculate_error(R1, R2, m):
    return (1/(4**m - 1))*(R1-R2)