import math

#initial values
z = (1 + 5 ** 0.5)/2.0
sigma = 1
x1 = sigma/10.0
x4 = 10.0*sigma
x2 = x4 - (x4-x1)/z
x3 = x1 + (x4-x1)/z
target = 1e-6
numsteps = 0;

def V(r, V0):
    return V0*[(sigma/r)**6.0 - math.exp(-r/sigma)]

while (True):

    V1 = V(x1,1)
    V2 = V(x2,1)
    V3 = V(x3,1)
    V4 = V(x4,1)

    if (abs(x4-x1) < target):
        break
    else:
        numsteps += 1
        if V2 < V3:
            x4 = x3
            x3 = x2
            x2 = x4 - (x4 - x1)/z
        else:
            x1 = x2
            x2 = x3
            x3 = x1 + (x4-x1)/z

print('x coord of min:', (x4+x1)/2.0)
print('min: ', V(x1, 1))
print('number of steps:', numsteps)