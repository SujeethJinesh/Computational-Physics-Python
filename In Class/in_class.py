def in_class():
    t = float(input("Please input the time: "))
    height = float(input("Please input the height: "))
    g = 9.8 #m/s^2
    distance = (1/2.0)*g*t**2.0 #m
    height_above_ground = height - distance #m

    if height_above_ground <= 0:
    	print ("The ball hit the ground")
    else:
    	print("The height of the ball is ", height_above_ground, "meters")