from random import random
from numpy import arange
from pylab import plot,xlabel,ylabel,show, legend

# Constants
NBi213 = 10000            # Number of Bi213 atoms
NTl = 0              # Number of Tl atoms
NPb = 0               # Number of lead atoms
NBi209 = 0              #Number of Bi209 atoms

tauPbToBi209 = 3.3*60        # Half life of lead in seconds
tauTlToPb = 2.2*60          #half life of Tl in seconds
tauBi213Decay = 46.0*60

h = 1.0               # Size of time-step in seconds

pPbToBi209 = 1 - 2**(-h/tauPbToBi209)   # Probability of decay for Lead
pTlToPb = 1 - 2**(-h/tauTlToPb)         #Probability of decay for Tl
pBi213Decay = 1 - 2**(-h/tauBi213Decay) #Probability of decay for Bi213

tmax = 20000           # Total time

# Lists of plot points
tpoints = arange(0.0,tmax,h)

Bi213points = []        #arrays for different atoms
Pbpoints = []
Bi209points = []
Tlpoints = []

# Main loop
for t in tpoints:
    Pbpoints.append(NPb)
    Bi209points.append(NBi209)
    Tlpoints.append(NTl)
    Bi213points.append(NBi213)
    # Calculate the number of atoms that decay

    for i in range(NBi213):
        if random() < pBi213Decay:
            if random() < 0.9791:
                NBi213 -= 1
                NPb += 1
            else:
                NBi213 -= 1
                NTl += 1

    for j in range(NTl):
        if (random() < pTlToPb) & (NTl > 0):
            NPb += 1
            NTl -= 1

    for k in range(NPb):
        if (random() < pPbToBi209) & (NPb > 0):
            NPb -= 1
            NBi209 += 1

# Make the graph
plot(tpoints,Pbpoints, label = "Pb")
plot(tpoints,Tlpoints, label = "Tl")
plot(tpoints,Bi209points, label = "Bi209")
plot(tpoints,Bi213points, label = "Bi213")

legend()

xlabel("Time")
ylabel("Number of decayed atoms")       #graphs
show()