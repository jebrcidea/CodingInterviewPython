#0,1,1,2,3,5,8,13,21,34,55
#0,1,2,3,4,5,6,7 ,8 ,9 ,10

def fibonacciIterative(position):
	if position == 0:
		return 0
	if position==1 or position==2:
		return 1
	fibonacci = [0,1,1]
	for index in range(3, position+1):
		fibonacci.append(fibonacci[index-2] + fibonacci[index-1])
	return fibonacci[position]

def fibonacciRecursive(position):
	if position == 0:
		return 0
	if position==1 or position==2:
		return 1
	return fibonacciRecursive(position-1) + fibonacciRecursive(position-2)