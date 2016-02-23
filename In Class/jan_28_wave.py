from math import sqrt, sin, pi
from numpy import empty
from pylab import imshow, gray, show

class jan_28_wave:

	def interference_maker(self):
		wavelength = input("input wavelength: ")
		k = 2*pi/wavelength
		amplitude = input("input amplitude: ")
		distance_between_centers = input("input distance between centers: ")
		length = 100.0
		num_points = 500
		spacing = length/num_points

		first_x = length/2 + distance_between_centers/2
		second_x = length/2 - distance_between_centers/2

		first_y = length/2
		second_y = first_y

		points_array = empty([num_points, num_points], float)

		for i in range(num_points):
			y = spacing*i
			for j in range(num_points):
				x = spacing*j
				r1 = sqrt((x-first_x)**2 + (y - first_y)**2)
				r2 = sqrt((x-second_x)**2 + (y - second_y)**2)
				points_array[i, j] = amplitude*(sin(k*r1)+sin(k*r2))

		imshow(points_array, origin="lower", extent=[0, length, 0, length])
		gray()
		show()