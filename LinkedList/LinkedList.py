class Node:
	
	def __init__(self, val = None):
		self.value = val
		self.next = None

class LinkedList:
	def __init__(self, val = None):
		self.head = Node(val)
		self.tail = self.head
		self.length = 1
		
	#adds element at the end
	def append(self, val):
		newNode = Node(val)
		self.tail.next = newNode
		self.tail = newNode
		self.length +=1
		
	#adds element at the beginning
	def prepend(self, value):
		newHead = Node(value)
		newHead.next = self.head
		self.head = newHead
		self.length +=1
		
	#returns the node at a given index
	def findNodeOnIndex(self, index):
		currentNode = self.head
		currentIndex = 0
		while currentIndex != index:
			currentNode = currentNode.next
			currentIndex +=1
		return currentNode
		
	#inserts node at a certain index
	def insert(self, index, val):
		if index > self.length -1 or index < 0: #if it's out of bouds, we return an error
			return false
		#if we want to insert at 0, we just use prepend
		elif index == 0:
			return prepend(val)
		#if we want to insert at the end, we just use append
		elif index == self.length -1 :
			return append(val)
			
		#otherwise find the node before we want to insert
		currentNode = self.findNodeOnIndex(index-1)
		newNode = Node(val)
		#change index accordingly
		newNode.next = currentNode.next
		currentNode.next = newNode
		self.length +=1 
		
	#removes an node at a certain index
	def remove(self, index):
		#if it's out of bouds, we return an error
		if index > self.length -1 or index < 0:
			return false
		#if it's 0 we just change the head and te correspondent index
		elif index == 0:
			newHead = self.head.next
			oldHead = self.head
			self.head = newHead
			self.length -=1 
			return oldHead #added this, useful for reverse
			
		#otherwise we find the note before and update indexes
		currentNode = self.findNodeOnIndex(index-1)
		deletedNode = currentNode.next
		currentNode.next = currentNode.next.next
		self.length -=1 
		return deletedNode #added this, useful for reverse
		
	#reverses the linked list
	def reverse(self):
		if self.length == 1:
			return self
		reverseLinkedList = LinkedList(self.tail.value) #creates a new list with the value of the other one's tail
		self.remove(self.length-1) #removes the tail
		while self.head != None: #while the current linkedList is not empty
			reverseLinkedList.append(self.remove(self.length-1).value) #we keep appending the last element to the reversed one
		self.head = reverseLinkedList.head #we make the new linkedList as the new one
		self.tail = reverseLinkedList.tail
		self.length = reverseLinkedList.length
		return self
		
	def reverseNoExtraSpace(self):
		if self.length == 1:
			return self
		first = self.head
		self.tail = self.head
		second = first.next
		while(second is not None):
			temp = second.next
			second.next = first
			first = second
			second = temp
		self.head.next = None
		self.head = first
		
	#prints the linked list in order
	def show(self):
		currentNode = self.head
		print(currentNode.value, "-->")
		while currentNode.next != None:
			currentNode = currentNode.next
			print(currentNode.value, "-->")
		print("length: " + str(self.length))
			
#test		
myLinkedList = LinkedList(10)
myLinkedList.append(5)
myLinkedList.append(16)
myLinkedList.show()
myLinkedList.prepend(1)
myLinkedList.show()
myLinkedList.insert(2,4)
myLinkedList.show()
#myLinkedList.remove(2)
#myLinkedList.show()
#myLinkedList.remove(3)
#myLinkedList.show()
#myLinkedList.remove(0)
#myLinkedList.show()
myLinkedList.reverse()
myLinkedList.show()
myLinkedList.reverseNoExtraSpace()
myLinkedList.show()