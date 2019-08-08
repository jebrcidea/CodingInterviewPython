def selectionSort(numbers):
	numbersLenght = len(numbers)
	for i in range(0, numbersLenght):
		min = i
		for j in range(i+1, numbersLenght):
			if numbers[j] < numbers[min]:
				min = j
		temp = numbers[min]
		numbers[min] = numbers[i]
		numbers[i] = temp
	return numbers