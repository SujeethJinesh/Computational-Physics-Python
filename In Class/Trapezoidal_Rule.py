def Trapezoidal_Rule():
    N = int(input("How many slices? "))
    sum = 0.0
    a = 0.0
    b = 2.0

    for x in range(1,N):
        sum = sum + function(a + x*(b-a)/N)

    sum = sum + (function(a) + function(b))/2

    sum = ((b - a)/N)*sum

    print(sum)

def function(number):
    return (pow(number, 4) - 2*number + 1)