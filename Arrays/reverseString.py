from collections import deque
def reverseString(stringToReverse):
	if not isinstance(stringToReverse, str) or len(stringToReverse) < 2:
		return False
	reversedString = deque()
	for letter in stringToReverse:
		reversedString.appendleft(letter)
	print (reversedString)
	return ''.join(reversedString)
	
def reverseString2(stringToReverse):
	reversedString = deque()
	for index in range(len(stringToReverse)-1, -1, -1):
		reversedString.append(stringToReverse[index])
	print (reversedString)
	return ''.join(reversedString)
	
def reverseString3(stringToReverse):
	return stringToReverse[::-1] 