class Node:
	
	def __init__(self, val = None):
		self.value = val
		self.next = None
		self.previous = None
		
class Stack:
	#constructor
	def __init__(self):
		self.top = None
		self.bottom = None
		self.length = 0
	
	#returns the element at the top
	def peek(self):
		return self.top
	
	#Adds element to the queue
	def push(self, value):
		newTop = Node(value)
		newTop.next = self.top
		self.top = newTop
		
		if self.length == 0:
			self.bottom = newTop
			
		self.length += 1
	
	#removes element from the queue
	def pop(self):
		if self.top is not None:
			if self.top == self.bottom:
				self.bottom = None
			poppedElemnt = self.top
			self.top = self.top.next
			self.length -=1
			return poppedElemnt
		return None
	
	#checks if the queue is empty
	def isEmpty(self):
		if self.length == 0:
			return True
		return False
		
#debug		
def test():
	myStack = Stack()
	myStack.push("Google")
	myStack.push("Udemy")
	myStack.push("Youtube")
	print(myStack.peek().value)
	print(myStack.isEmpty())
	print(myStack.pop().value)
	print(myStack.isEmpty())
	print(myStack.peek().value)
	print(myStack.pop().value)
	print(myStack.pop().value)
	print(myStack.isEmpty())
	