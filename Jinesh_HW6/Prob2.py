from numpy import empty, pi, sin
from pylab import plot,xlabel,ylabel,show, legend   #necessary imports

# Constants
L = 20.0      # Thickness of dirt in meters
D = 0.1      # Thermal diffusivity
N = 20       # Number of divisions in grid
a = L/N       # Grid spacing
h = 1.0      # Time-step
epsilon = h     #epsilon
tau = 365.0     #sampling time

A = 10.0
B = 12.0

Tlo = 11.0     # Low temperature in Celcius
Tmid = 10.0   # Intermediate temperature in Celcius

def Thi(time):                  #high temperature function
    return A + B*sin((2.0*pi*time)/tau)

t1 = 9*365.0            #Time for 9 years
t2 = 9*365.0 + 91       #Time for 9.25 years
t3 = 9*365.0 + 182      #Time for 9.5 years
t4 = 9*365.0 + 273      #Time for 9.75 years
t5 = 10*365.0           #Time for 10 years
tend = t5               #End time

# Create arrays
T = empty(N+1,float)
T[N] = Tlo
T[1:N] = Tmid
Tp = empty(N+1,float)
Tp[N] = Tlo

# Main loop
t = 0.0
c = h*D/(a*a)
while t<tend:
    T[0] = Thi(t)   #update values of T hi

    # Calculate the new values of T
    for i in range(1,N):
        Tp[i] = T[i] + c*(T[i+1]+T[i-1]-2*T[i])     #heat equation
    T,Tp = Tp,T
    t += h

    # Make plots at the given times
    if abs(t-t1)<epsilon:
        plot(T, label = "9")
    if (abs(t-t2)<epsilon):
        plot(T, label = "9.25")
    if abs(t-t3)<epsilon:
        plot(T, label = "9.5")
    if abs(t-t4)<epsilon:
        plot(T, label = "9.75")
    if abs(t-t5)<epsilon:
        plot(T, label = "10")

legend()
xlabel("Time")      #plotting answer
ylabel("Temp")
show()