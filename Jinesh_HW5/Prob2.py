from __future__ import print_function,division
from math import *
from pylab import *                 #necessary imports
import matplotlib.pyplot as plt

sigma = 10
rLorenz = 28                #define constants
b = 8/3

def f(r, t):               #function for RK4
    x = r[0]
    y = r[1]
    z = r[2]
    fx = sigma*(y-x)
    fy = rLorenz*x - y - x*z
    fz = x*y - b*z
    return (array([fx, fy, fz]))

r=array([0,1, 0])           #initialize array
N=1000
t=linspace(0,10,1001)
x=[]
y=[]                    #initialize x,y,z
z=[]

for i in t:             #begin RK4 here
    if i==0:
        x.append(r[0])
        y.append(r[1])
        z.append(r[2])
    else:
        k1=0.01*f(r,i)
        k2=0.01*f(r+0.5*k1,i+0.5*0.01)
        k3=0.01*f(r+0.5*k2,i+0.5*0.01)
        k4=0.01*f(r+0.5*k3,i+0.01)
        r=r+(1/6.0)*(k1+2*k2+2*k3+k4)
        x.append(r[0])
        y.append(r[1])
        z.append(r[2])

plt.subplot(2, 1, 1)                #plot subplots
plt.plot(t,y)
plt.title('Angular Motion of Pendulum')
plt.xlabel('Time')
plt.ylabel('Theta (Radians)')

plt.subplot(2,1,2)
plt.plot(x,z)
plt.xlabel('Time')
plt.ylabel('Theta (Radians)')

show()                      #show plots