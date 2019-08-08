class Node:
	
	def __init__(self, val = None):
		self.value = val
		self.next = None
		self.previous = None

class Queue:

	def __init__():
		self.first = None
		self.last = None
		self.length = 0
	
	#returns the first element of the queue
	def peek(self):
		return self.first
	
	#adds an element to the end of the queue
	def enqueue(self, value):
		newNode = Node(value)
		if self.last is not None:
			self.last.next = newNode
			self.last = newNode
		else:
			self.first = newNode
			self.last = newNode
		self.length +=1
	
	#removes and return the first element od the queueu
	def dequeue(self, value):
		firstNode = self.first
		if self.first is not None:
			self.first = self.first.next
		elif self.first == self.last:
			self.first = None
			self.last = None
		else:
			self.first = None
		self.length -=1
		return firstNode
	
	
	def isEmpty(self):
		return self.length==0
		
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