import matplotlib
import numpy as np
from sympy import solve, plot
from sympy.mpmath import linspace


def newtons_method(u):
    error = 1E-12
    xpoints = linspace(-0.99, 0.99, 100)
    ypoints = []
    x = xpoints[0]
    x1 = xpoints[1]
    accuracy = abs(x1 - x)
    while accuracy > error:
        x1 = x - f(x, u)/derivative(x)
        x1 = x
        ypoints.append(x1)

    plot(xpoints, ypoints)

def f(x, u):
    return np.tanh(x) - u

def derivative(x):
    return 1/(np.cosh(x))**2
