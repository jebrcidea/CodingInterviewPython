import math

def mergeSort(numbers):
	numbersLenght = len(numbers)
	if (numbersLenght == 1):
		return numbers

	# Split Array in into right and left
	middle = math.floor(numbersLenght/2)
	left = numbers[0:middle]
	right = numbers[middle:numbersLenght]

	return merge(mergeSort(left),mergeSort(right))


def merge(left, right):
	leftIndex,rightIndex = 0,0
	leftLenght, rightLenght = len(left), len(right)
	sortedArray = list()
	while(leftIndex < leftLenght or rightIndex < rightLenght):
		if rightIndex == rightLenght or (leftIndex < leftLenght and left[leftIndex] < right[rightIndex]):
			sortedArray.append(left[leftIndex])
			leftIndex+=1
		else:
			sortedArray.append(right[rightIndex])
			rightIndex+=1
		#print(sortedArray, leftIndex, rightIndex) #debug
	return sortedArray




numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0];
print(mergeSort(numbers))