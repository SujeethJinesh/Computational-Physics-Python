import math
from numpy import array, linspace
from sympy import sin
import matplotlib.pyplot as plt         #necessary imports

g = 9.81
l = 0.1
r=array([math.radians(179),0.0])
N=1000
t=linspace(0,10,1001)
theta = []
omega = []              #defining constants

def f(r, t):                        #function for performing RK4
    theta = float(math.radians(r[0]))
    omega = r[1]
    fTheta = omega
    fOmega = -(g/l)*sin(theta)
    return (array([fTheta, fOmega], float))

for i in t:             #beginning RK4
    if i==0:
        theta.append(r[0])
        omega.append(r[1])
    else:
        k1=0.01*f(r,i)
        k2=0.01*f(r+0.5*k1,i+0.5*0.01)
        k3=0.01*f(r+0.5*k2,i+0.5*0.01)          #RK4
        k4=0.01*f(r+0.5*k3,i+0.01)
        r=r+(1/6.0)*(k1+2*k2+2*k3+k4)
        theta.append((r[0]))
        omega.append(r[1])

plt.plot(t,theta)
plt.xlabel('Time')
plt.ylabel('Theta (Radians)')
plt.title('Angular Motion of Pendulum')         #making plot
plt.show()

#part b, attempted to create animation, but failed to get it running.

# import numpy as np
# from matplotlib import pyplot as plt
# from matplotlib import animation
#
# # First set up the figure, the axis, and the plot element we want to animate
# fig = plt.figure()
# ax = plt.axes(xlim=(0, 2), ylim=(-2, 2))
# line, = ax.plot([], [], lw=2)
#
# # initialization function: plot the background of each frame
# def init():
#     line.set_data([], [])
#     return line,
#
# # animation function.  This is called sequentially
# def animate(i):
#     x = linspace(0,10,1001)
#     y = -(g/l)*sin(x)
#     line.set_data(x, y)
#     return line,
#
# # call the animator.  blit=True means only re-draw the parts that have changed.
# anim = animation.FuncAnimation(fig, animate, init_func=init,
#                                frames=200, interval=20, blit=True)
#
# # save the animation as an mp4.  This requires ffmpeg or mencoder to be
# # installed.  The extra_args ensure that the x264 codec is used, so that
# # the video can be embedded in html5.  You may need to adjust this for
# # your system: for more information, see
# # http://matplotlib.sourceforge.net/api/animation_api.html
# #anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
#
# plt.show()