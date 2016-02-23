import math #importing tools needed for math operations in the function

def orbit_height():
    period = float(input("Enter desired period value in seconds: ")) #getting period value from the user

    universal_gravitational_constant = 6.67*pow(10, -11.0) #assigning universatl gravitational constant

    mass_of_earth = 5.97*pow(10, 24.0) #assigning mass of earth

    radius_of_earth = 6371.0*pow(10, 3.0) #assigning radius of earth

    altitude = pow(universal_gravitational_constant*mass_of_earth*pow(period,2)/(4*pow(math.pi, 2)), 1/3.0) - radius_of_earth #plugging in final formula

    print("The altitude for the satellite to be in a circular orbit for a period of ", period, " seconds is ", altitude, "m.") #final output