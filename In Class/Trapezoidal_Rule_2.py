def Trapezoidal_Rule(N):
    sum = 0.0
    a = 0.0
    b = 2.0

    for x in range(1,N):
        sum = sum + function(a + x*(b-a)/N)

    sum = sum + (function(a) + function(b))/2

    sum = ((b - a)/N)*sum

    return(sum)

def function(number):
    return (pow(number, 4) - 2*number + 1)

def calculate_e_2(h_1):
    I_1 = Trapezoidal_Rule(h_1)
    h_2 = 2*h_1
    I_2 = Trapezoidal_Rule(h_2)
    e_2 = (1/3.0)*(I_2 - I_1)
    print(e_2)
