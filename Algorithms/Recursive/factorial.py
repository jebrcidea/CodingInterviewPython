def factorial(number):
	if number == 1:
		return 1
	return number*factorial(number-1)
	
	
def factorialIterative(number):
	response = 1
	counter = 0
	while counter < number:
		counter +=1
		response *= counter
	return response