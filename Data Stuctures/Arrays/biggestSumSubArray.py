'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''
from collections import deque
import sys

#inefficient method for solving it.
def worstBiggestSumSubArray(array):
	biggerSUM = -sys.maxsize - 1
	arrayLength = len(array)
	
	#validations ToDo
	
	#gets the biggest element in the array since it's the biggest 1-size sub-array
	if(max(array) > biggerSUM):
		biggerSUM = max(array)
		print(biggerSUM, max(array))
	
	#for all the posible lenghts (I know, sorry)
	for sumLenght in range(2, arrayLength):
		smallerIndex = 0
		queu = deque()
		
		#fills with the starting array with the given length
		while len(queu) < sumLenght:
			queu.append(array[smallerIndex])
			smallerIndex+=1
				
		#while i still have elements
		while smallerIndex < arrayLength:
			#if the sum is bigger, I update my possible output
			if sum(queu) > biggerSUM:
				biggerSUM = sum(queu)
				print(biggerSUM, queu, sumLenght) #debug
			
			#if i'm not done yet, I try with the next array of this size
			if smallerIndex < arrayLength:
				queu.popleft()
				queu.append(array[smallerIndex])
			
			smallerIndex+=1
				
	return biggerSUM
			
			
			