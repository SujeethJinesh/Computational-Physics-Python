def Trapezoidal_Rule(N):
    a = 0.0
    b = 1.0

    h = (b - a) / n
    x = a
 
    summation = function(a)
    for k in range(1, n):
        x  = x + h
        summation = summation + 2*function(x)
 
    return (summation + function(b))*h*0.5

def function(number):
    return sin((100*number) ** 0.5) ** 2.0

def calculate_e_2(h_1):
    I_1 = Trapezoidal_Rule(h_1)
    h_2 = 2*h_1
    I_2 = Trapezoidal_Rule(h_2)
    e_2 = (1/3.0)*(I_2 - I_1)
    print(e_2)
