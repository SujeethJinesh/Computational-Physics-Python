import time #importing timer function

def integral_calculator():
    N = float(input("Please input the number of slices: ")) #got input from user for number of slices
    start = time.time() #started timer
    h = 2.0/N #got h value (basically the step size)
    integral = 0.0 #initialized the integral we will have
    for k in range(1, int(N + 1)): #looping through all values from 1 to N, added one because python doesn't go through all values
        x_k = -1.0 + float(h*k)  #got x value per k
        y_k = h*(pow(1.0 - pow(x_k, 2.0), 0.5)) #got y value from formula
        integral = y_k + integral #summed the integral
    print("The integral is ", integral) #printed final result
    end = time.time() #ended timer
    print(end-start) #for part b, inputted different number of slices and calculated time necessary for computation