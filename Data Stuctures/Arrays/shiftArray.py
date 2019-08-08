'''
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

Note:

    Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
    Could you do it in-place with O(1) extra space?

'''
from collections import deque
def shiftArray(array, steps):
	array = deque(array)
	while steps > 0:
		array.appendleft(array.pop())
		steps -=1
	return array
	
def shiftArrayNoExtraSpace(array, steps):
	aux = 0
	while steps > 0:
		newIndexZero = array[len(array)-1]
		aux = array[0]
		array[0] = newIndexZero
		oldAux = aux
		currentIndex=1
		while(currentIndex < len(array)):
			aux = array[currentIndex]
			array[currentIndex] = oldAux
			oldAux = aux
			currentIndex+=1
			
		steps -=1
	return array