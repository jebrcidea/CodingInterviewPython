from collections import deque
def reverseString(stringToReverse):
	if not isinstance(stringToReverse, str) or len(stringToReverse) < 2:
		return False
	reversedString = deque()
	for letter in stringToReverse:
		reversedString.appendleft(letter)
	print (reversedString)
	return ''.join(reversedString)
	
def reverseString2(stringToReverse):  #solution with deque, makes code smaller
	reversedString = deque()
	for index in range(len(stringToReverse)-1, -1, -1):
		reversedString.append(stringToReverse[index])
	print (reversedString)
	return ''.join(reversedString)
	
def reverseString3(stringToReverse): #less lines solution, hard to understand f you dont know python
	return stringToReverse[::-1] 