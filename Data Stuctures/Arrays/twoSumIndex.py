'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

'''
def twoSumIndex(numbersArray, target):
	dictionary = dict()
	
	if type(target) != int or type(numbersArray)!= list or len(numbersArray) < 2:
		return []
	#add validation for each item of the array
	
	for index, number in enumerate(numbersArray):
		#validating that the element is a number
		if type(number) != int:
			return []
			
		complement = target - number
		if complement in dictionary:
			return [dictionary[complement], index]
			
		if not number in dictionary:
			dictionary[number] = index
	return []