import math
import matplotlib.pyplot as plt
import numpy as np

lower = -5
upper = 5
wavelength = 1
z = 3
N = 50
I_0 = 100

def diffraction():
    y = [0]*50
    x = np.linspace(lower, upper, num = 50)
    counter = 0
    while counter < (len(x)):
        print(x[counter])
        y[counter] = function_main(x[counter])/I_0
        counter += 1

    plt.plot(x, y)
    plt.show()

def function_main(x):
    u = x * pow(2/(wavelength*z),0.5)
    C = Trapezoidal_Rule_cos(N, u)
    S = Trapezoidal_Rule_sin(N, u)
    return I_0/8.0 * ((2*C + 1) ** 2 + (2*S + 1) ** 2)

def function_cos(num):
    return math.cos(math.pi*0.5*num**2)

def Trapezoidal_Rule_cos(N, u):
    a = 0.0
    b = u

    h = (b - a) / N
    x = a
 
    summation = function_cos(a)
    for k in range(1, N):
        x  = x + h
        summation = summation + 2*function_cos(x)
 
    return (summation + function_cos(b))*h*0.5


def function_sin(num):
    return math.sin(math.pi*0.5*num**2)

def Trapezoidal_Rule_sin(N, u):
    a = 0.0
    b = u

    h = (b - a) / N
    x = a
 
    summation = function_sin(a)
    for k in range(1, N):
        x  = x + h
        summation = summation + 2*function_sin(x)
 
    return (summation + function_sin(b))*h*0.5