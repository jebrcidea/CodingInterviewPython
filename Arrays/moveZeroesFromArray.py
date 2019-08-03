'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Note:
    You must do this in-place without making a copy of the array.
    Minimize the total number of operations.

'''

def moveZeroesFromArray(array):
	movedElements = 0
	index = 0
	while index < len(array)-movedElements:
		if array[index] == 0:
			movedElements +=1
			array.append(array.pop(index))
		else:
			index +=1
	return array