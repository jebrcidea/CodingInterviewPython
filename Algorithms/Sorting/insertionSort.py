def insertionSort(numbers):
	for i in range (1, len(numbers)):
		aux = i
		while numbers[aux] < numbers[aux-1] and aux > 0:
			temp = numbers[aux-1]
			numbers[aux-1] = numbers[aux]
			numbers[aux] = temp
			aux -=1
	return numbers
	
				



numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0];