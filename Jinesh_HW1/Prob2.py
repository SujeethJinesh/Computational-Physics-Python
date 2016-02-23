import math

def travel_time():
    distance_from_planet = float(input("Enter distance from planet in light years: ")) #gets user input for light year distance

    speed_of_craft = float(input("please enter speed as a fraction of c: ")) #gets speed of craft in terms of c from user

    stationary_observer_time_years = distance_from_planet/speed_of_craft #calculates time according to stationary observer

    moving_observer_time_years = stationary_observer_time_years*math.sqrt(1 - pow(speed_of_craft, 2.0)) #Time dilation equation solved for observer's time

    print("It will take ", stationary_observer_time_years, " years according to the stationary observer's reference frame.") #output for stationary observer
    print("It will take ", moving_observer_time_years, " years according to the travelling observer's reference frame.") #output for moving observer
