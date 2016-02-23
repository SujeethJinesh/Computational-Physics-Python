def derivative_calculator(): #defined function
    delta = pow(10, -2) #made the delta value
    x = float(input("What would you like your x value to be? ")) #got user input for x value
    derivative = (function((x + delta)) - function(x))/delta #calculated derivative using def of derivative
    print(derivative) #printed final result

def function(x): #created helper function
    return x*(x-1) #returns the function to be used