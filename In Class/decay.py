import random
import matplotlib.pyplot as plt
from matplotlib import pyplot
from numpy.__config__ import show
from numpy.ma import arange

numThall = 1000
numLead = 0
tau = 3.053*60
h = 1.0
p = 1 - 2 ** (-h/tau)

points = arange(0,1000)
thallArray = []
leadArray = []

for point in points:
    if random.random() < p:
        numLead += 1
    leadArray.append(numLead)
    thallArray.append(numThall-numLead)

pyplot.ylabel("Num")
pyplot.xlabel("Time")
plt.plot(points, thallArray)
plt.plot(points, leadArray)
plt.show()