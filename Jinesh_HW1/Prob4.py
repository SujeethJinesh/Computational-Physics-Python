"""This function is recursive, it calls itself until it reaches the terminating condition
defined by the if statement. The else statement continues the function calls and increments
towards the terminating condition."""

def catalan_numbers(catalan_number, iteration):
    if catalan_number > 1000000000:    #The call stack will terminate when it reaches this upper limit
        return     #This will actually terminate the stack
    else:
        print(catalan_number)   #This prints the number

        if catalan_number == 1:
        	print(catalan_number)

        new_catalan_number = ((4.0*iteration+2.0)/(iteration+2.0))*catalan_number   #Calculates catalan number
        iteration = iteration + 1  #increments the iteration
        catalan_numbers(new_catalan_number, iteration)  #calls the function again.