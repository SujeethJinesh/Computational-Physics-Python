from numpy import empty,zeros,max
from pylab import imshow,show

# Constants
M = 50         # Grid squares on a side
V = 1.0         # Voltage at top wall
target = 1e-6   # Target accuracy
epsilon = 1
C = 1.0         #charge density
step = 100/M

# Create arrays to hold potential values
phi = zeros([M+1,M+1],float)
phi[0,:] = V
phiprime = empty([M+1,M+1],float)
rho = empty([M+1, M+1], float) #array for charges

for i in range(M/5, 2*M/5 + 1):
    for j in range(3*M/5, 4*M/5 + 1):
        rho[i,j] = -C
for i in range(3*M/5, 4*M/5 + 1):
    for j in range(M/5, 2*M/5 + 1):
        rho[i,j] = C


# Main loop
delta = 1.0
while delta>target:

    # Calculate new values of the potential
    for i in range(M+1):
        for j in range(M+1):
            if i==0 or i==M or j==0 or j==M:
                phiprime[i,j] = phi[i,j]
            else:
                phiprime[i,j] = (phi[i+1,j] + phi[i-1,j]
                                 + phi[i,j+1] + phi[i,j-1])/4 + ((step**2)/4*epsilon)*rho[i,j]

    # Calculate maximum difference from old values
    delta = max(abs(phi-phiprime))

    # Swap the two arrays around
    phi,phiprime = phiprime,phi

# Make a plot
imshow(phi)
show()