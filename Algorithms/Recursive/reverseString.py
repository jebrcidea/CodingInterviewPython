import math

def reverseString(stringToReverse):
	stringLenght = len(stringToReverse)
	if stringLenght == 1:
		return stringToReverse
	if stringLenght == 2:
		return stringToReverse[::-1]
	return reverseString(stringToReverse[math.floor(stringLenght/2):stringLenght]) + reverseString(stringToReverse[0:math.floor(stringLenght/2)])
	
print(reverseString('yoyo master'))
#should return: 'yretsam oyoy'