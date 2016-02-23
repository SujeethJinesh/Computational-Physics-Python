def ask_for_input():
	odd = int(input("Enter an odd number: "))

	even = int(input("Enter an even number: "))

	if odd%2 == 1 and even%2 == 0:
		print "Nice job!"
	else:
		print "You suck."