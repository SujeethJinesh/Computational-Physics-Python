import math

def ball_drop():
    height = float(input("please input the height of the tower: ")) #This is how many meters tall the tower is
    gravity = 9.81 #This is the acceleration (m/s^2) due to gravity near earth's surface
    time = math.sqrt((2.0*height)/gravity) #derived from h = 1/2 gt^2 to solve for time
    print("It will take the ball ", time, " seconds to fall to earth.") #Final output statement.