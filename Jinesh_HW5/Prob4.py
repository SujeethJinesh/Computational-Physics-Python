import math
from datetime import time
from sympy import cos, sin              #necessary imports
import matplotlib.pyplot as plt

C = 2.0
bigOmega = 5.0
theta = math.radians(0.0)           #defining constants
u = 0.0
times = []
thetas = []

g = 9.81
l = 0.01

h = 0.05
t = 0.0

while (t < 100):                #performing double RK4
    m1 = u
    k1 = -(g/l)*sin(theta) + C*(cos(theta))*sin(bigOmega*t)
    m2 = u + (h/2.0) * k1
    t_2 = t + (h/2.0)
    theta_2 = (theta + (h/2.0) * m1)
    u_2 = m2
    k2 = -(g/l)*sin(theta_2) + C*(cos(theta_2))*sin(bigOmega*t_2)
    m3 = u + (h/2.0)*k2
    t_3 = t + (h/2.0)
    theta_3 = (theta + (h/2.0) * m2)
    u_3 = m3
    k3 = -(g/l)*sin(theta_3) + C*(cos(theta_3))*sin(bigOmega*t_3)
    m4 = u + h*k3
    t_4 = t + h
    theta_4 = (theta + h * m3)
    u_4 = m4
    k4 = -(g/l)*sin(theta_4) + C*(cos(theta_4))*sin(bigOmega*t_4)
    t = t + h
    theta = math.radians(theta + (h/6.0)*(m1 + 2.0*m2 + 2.0*m3 + m4))
    u = u + (h/6.0)*(k1 + 2.0*k2 + 2.0*k3 + k4)
    times.append(t)
    thetas.append(theta)

plt.plot(times, thetas)                 #part a
plt.xlabel('Time')
plt.ylabel('Theta (Radians)')
plt.title('Angular Motion of Pendulum')         #making plot
plt.show()

def partB(): #performing calculations once again for big omega

    for bigOmega in range(-5, 5):
        C = 2.0
        theta = math.radians(0.0)           #defining constants
        u = 0.0
        times = []
        thetas = []

        g = 9.81
        l = 0.01

        h = 0.05
        t = 0.0
        while (t < 100):                #performing double RK4
            m1 = u
            k1 = -(g/l)*sin(theta) + C*(cos(theta))*sin(bigOmega*t)
            m2 = u + (h/2.0) * k1
            t_2 = t + (h/2.0)
            theta_2 = (theta + (h/2.0) * m1)
            u_2 = m2
            k2 = -(g/l)*sin(theta_2) + C*(cos(theta_2))*sin(bigOmega*t_2)
            m3 = u + (h/2.0)*k2
            t_3 = t + (h/2.0)
            theta_3 = (theta + (h/2.0) * m2)
            u_3 = m3
            k3 = -(g/l)*sin(theta_3) + C*(cos(theta_3))*sin(bigOmega*t_3)
            m4 = u + h*k3
            t_4 = t + h
            theta_4 = (theta + h * m3)
            u_4 = m4
            k4 = -(g/l)*sin(theta_4) + C*(cos(theta_4))*sin(bigOmega*t_4)
            t = t + h
            t = math.radians(theta + (h/6.0)*(m1 + 2.0*m2 + 2.0*m3 + m4))
            u = u + (h/6.0)*(k1 + 2.0*k2 + 2.0*k3 + k4)
            times.append(t)
            thetas.append(theta)

        plt.plot(times, thetas)                 #part b
        plt.xlabel('Time')
        plt.ylabel('Theta (Radians)')
        plt.title('Angular Motion of Pendulum')         #making plot
        plt.show()
        time.sleep(10)