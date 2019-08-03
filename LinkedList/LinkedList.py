class Node:
	
	def __init__(self, val = None):
		self.value = val
		self.next = None

class LinkedList:
	def __init__(self, val = None):
		self.head = Node(val)
		self.tail = self.head
		self.length = 1
		
	def append(self, val):
		newNode = Node(val)
		self.tail.next = newNode
		self.tail = newNode
		self.length +=1
		
	def prepend(self, value):
		newHead = Node(value)
		newHead.next = self.head
		self.head = newHead
		self.length +=1
		
	def findNodeOnIndex(self, index):
		currentNode = self.head
		currentIndex = 0
		while currentIndex != index:
			currentNode = currentNode.next
			currentIndex +=1
		return currentNode
		
	def insert(self, index, val):
		if index > self.length -1 or index < 0:
			return false
		elif index == 0:
			return prepend(val)
		elif index == self.length -1 :
			return append(val)
			
		currentNode = self.findNodeOnIndex(index-1)
		newNode = Node(val)
		newNode.next = currentNode.next
		currentNode.next = newNode
		self.length +=1 
		
	
	def show(self):
		currentNode = self.head
		print(currentNode.value, "-->")
		while currentNode.next != None:
			currentNode = currentNode.next
			print(currentNode.value, "-->")
		print("length: " + str(self.length))
			
		
myLinkedList = LinkedList(10)
myLinkedList.append(5)
myLinkedList.append(16)
myLinkedList.show()
myLinkedList.prepend(1)
myLinkedList.show()
myLinkedList.insert(2,4)
myLinkedList.show()