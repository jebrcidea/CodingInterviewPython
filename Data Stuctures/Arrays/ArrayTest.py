def arrayTest(array):
	print(array)
	array.append('j')
	print(array)
	array.pop()
	print(array)
	array = ['0'] + array
	print(array)

from collections import deque
#faster for pop and append (both left and right, so queues and stacks. But slower for inserting at the middle
def tryDequeue():
	dequeVar = deque('abc')
	print(dequeVar)
	dequeVar.append('j')
	print(dequeVar)
	dequeVar.pop()
	print(dequeVar)
	dequeVar.appendleft('0')
	print(dequeVar)
	dequeVar.popleft()
	print(dequeVar)
	
arrayTest(['a', 'b', 'c'])
tryDequeue()