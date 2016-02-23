import time
import math

def harmonic_oscillator():
    N = int(input("input N: "))
    start = time.clock()
    beta = 1.0/100.0
    h_bar = 1
    omega = 1
    sum = 0.0
    z = 0.0

    for i in range(0, N):
        z = z + pow(math.e, -beta*(i+0.5))

    for n in range(0, N):
        sum = sum + (n + 0.5)*pow(math.e, -beta*(n+0.5))

    finalSum = (1/z)*sum
    end = time.clock()

    print("Answer:", finalSum, "\ntime took is: ", end-start)