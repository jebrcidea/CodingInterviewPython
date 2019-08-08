class Node:
	
	def __init__(self, val = None):
		self.value = val
		self.next = None
		self.previous = None

class DoublyLinkedList:
	def __init__(self, val = None):
		self.head = Node(val)
		self.tail = self.head
		self.length = 1
		
	#adds element at the end
	def append(self, val):
		newNode = Node(val)
		self.tail.next = newNode
		newNode.previous = self.tail
		self.tail = newNode
		self.length +=1
		
	#adds element at the beginning
	def prepend(self, value):
		newHead = Node(value)
		newHead.next = self.head
		self.head.previous = newHead
		self.head = newHead
		self.length +=1
		
	#returns the node at a given index. Optimized so we can start at the beginning or the end accordingly
	def findNodeOnIndex(self, index):
		if index > self.length -1 or index < 0:
			return False
		
		#if it's smaller or equal to the first half, we start at the beginning
		if index <= self.length / 2 :
			currentNode = self.head
			currentIndex = 0
			while currentIndex != index:
				currentNode = currentNode.next
				currentIndex +=1
		#if it's at the end, we start by the end. 
		else:
			currentNode = self.tail
			currentIndex = self.length-1
			while currentIndex != index:
				currentNode = currentNode.previous
				currentIndex -=1
		return currentNode
		
	#inserts node at a certain index
	def insert(self, index, val):
		if index > self.length -1 or index < 0:  #if it's out of bouds, we return an error
			return False
		elif index == 0: #if we want to insert at 0, we just use prepend
			return prepend(val)
		elif index == self.length -1 : #if we want to insert at the end, we just use append
			return append(val)
			
		#otherwise find the node before we want to insert
		currentNode = self.findNodeOnIndex(index-1)
		newNode = Node(val)
		#change indexes accordingly
		newNode.next = currentNode.next
		newNode.previous = currentNode
		currentNode.next.previous = newNode
		currentNode.next = newNode
		self.length +=1 
		
	#removes an node at a certain index
	def remove(self, index):
		if index > self.length -1 or index < 0: #if it's out of bouds, we return an error
			return False
		#if it's 0 we just change the head and te correspondent index
		elif index == 0:  
			newHead = self.head.next
			newHead.previous = None
			self.head = newHead
			self.length -=1 
			return
			
		#otherwise we find the note before and update indexes
		currentNode = self.findNodeOnIndex(index-1)
		currentNode.next = currentNode.next.next
		#be careful, this could be the last node so it might not have a next.previous
		if currentNode.next is not None:
			currentNode.next.previous = currentNode
		self.length -=1 
	
	#prints the linked list in order
	def show(self):
		currentNode = self.head
		print(currentNode.value, "-->")
		while currentNode.next != None:
			currentNode = currentNode.next
			print(currentNode.value, "-->")
		print("length: " + str(self.length))
			
#test			
myLinkedList = DoublyLinkedList(10)
myLinkedList.append(5)
myLinkedList.append(16)
myLinkedList.show()
myLinkedList.prepend(1)
myLinkedList.show()
myLinkedList.insert(2,4)
myLinkedList.show()
myLinkedList.remove(2)
myLinkedList.show()
myLinkedList.remove(3)
myLinkedList.show()
myLinkedList.remove(0)
myLinkedList.show()