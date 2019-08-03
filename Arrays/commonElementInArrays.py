def isThereCommonElement(array1,array2): #O(n+m)
	hashTable = { i:True for i in array1 } #O(n)
	for item in array2: #O(m)
		if item in hashTable:
			return True
	return False
			