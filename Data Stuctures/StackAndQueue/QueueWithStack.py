'''
 Implement Queue using Stacks
 
 Implement the following operations of a queue using stacks.

    push(x) -- Push element x to the back of queue.
    pop() -- Removes the element from in front of queue.
    peek() -- Get the front element.
    empty() -- Return whether the queue is empty.

Example:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);  
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false


Notes:

    You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
    Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
    You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).

'''

class QueueWithStack:
	def __init__(self):
		self.stack = list()

	def push(self, value):
		self.stack.append(value)
	
	def pop(self):
		newQueue = list()
		while len(self.stack) != 1:
			newQueue.append(self.stack.pop())
		response = self.stack.pop()
		self.stack = newQueue
		#for index in range(0, len(newQueue)):
		#	self.stack.append(newQueue[index])
			
		return response
	
	def peek(self):
		return self.stack[0]
	
	def isEmpty(self):
		return len(self.stack) == 0
		
		
def test():
	myStack = QueueWithStack()
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