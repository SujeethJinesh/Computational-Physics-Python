import os

def sum_of_squares():

	os.path.abspath("mydir/jan_19.txt")

	file = open('jan_19', 'r')

	x = 0;

	line = file.readline()

	for line in file:

		num = pow(line,2)

		x += num

	print x