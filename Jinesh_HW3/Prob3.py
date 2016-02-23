from math import sin

def function(number):
    return sin((100*number) ** 0.5) ** 2.0   #function we are supposed to find integral of

def calculate_error(h_1): #calculates the error
    I_1 = Prob1(h_1)
    h_2 = 2*h_1
    I_2 = Prob1(h_2)
    e_2 = (1/3.0)*(I_2 - I_1)
    print(e_2)


def simpsons(a,b): #simpsons rule to be used again
    c = (a+b)/2.0
    return ((b-a)/6.0) * (function(a) + 4.0*function(c) + function(b))

def adaptiveSimpsonsRule(a,b,error, total, counter): #recursive def. of adaptive simpson's rule.
    counter = counter + 1
    print(counter)
    print(total)
    c = (a+b) / 2.0
    left = simpsons(a,c)
    right = simpsons(c,b)
    if abs(left + right - total) <= 15*error:
        return left + right + (left + right - total)/15.0
    return adaptiveSimpsonsRule(a,c,error/2.0,left, counter) + adaptiveSimpsonsRule(c,b,error/2.0,right, counter)

def adaptive_simpsons_rule(a,b,error):
    "Calculate integral of f from a to b with max error of eps."
    return ("final", adaptiveSimpsonsRule(a,b,error,simpsons(a,b), 0))