class StackWithArray:
	def __init__(self):
		self.array = list()
		self.length = 0
	
	
	
	def peek(self):
		return self.array[self.length-1]
	
	def push(self, value):
		self.array.append(value)
		self.length +=1
	
	def pop(self):
		if self.length > 0:
			self.length -=1
		return self.array.pop()
		
		
	def isEmpty(self):
		return self.length == 0
		
#debug		
def test():
	myStack = StackWithArray()
	myStack.push("Google")
	myStack.push("Udemy")
	myStack.push("Youtube")
	print(myStack.peek())
	print(myStack.isEmpty())
	print(myStack.pop())
	print(myStack.isEmpty())
	print(myStack.peek())
	print(myStack.pop())
	print(myStack.pop())
	print(myStack.isEmpty())