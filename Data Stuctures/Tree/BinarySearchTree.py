class BinaryTreeNode:
	def __init__(self, value = None):
		self.value = value
		self.left = None
		self.right = None
		
class BinarySearchTree:
	def __init__(self):
		 self.root = None
		 
		 
	def insert(self, value):
		newBinaryTreeNode = BinaryTreeNode(value)
		if self.root == None:
			self.root = newBinaryTreeNode
			return
		else:
			currentNode = self.root
			while currentNode != None:
				if newBinaryTreeNode.value > currentNode.value:
					if currentNode.right is None:
						currentNode.right = newBinaryTreeNode
						return
					else:
						currentNode = currentNode.right
				else:
					if(currentNode.left is None):
						currentNode.left = newBinaryTreeNode
						return
					else:
						currentNode = currentNode.left
	
	
	
	def lookup(self, value):
		currentNode = self.root
		while currentNode != None:
			if value > currentNode.value:
				currentNode = currentNode.right
			elif value < currentNode.value:
				currentNode = currentNode.left
			elif value == currentNode.value:
				return currentNode
		return False
		
	# def delete(self, value):
		# if self.root is None:
			# return False
		# currentNode = self.root
		# parrentNode = None
		# while currentNode is not None:
			# if value < currentNode.value:
				# parentNode = currentNode
				# currentNode = currentNode.left
			# elif value > currentNode.value:
				# arentNode = currentNode
				# currentNode = currentNode.right
			# else:
				# if currentNode.right == None:
					# if parentNode is None:
						# self.root = currentNode.left
					# else:
						# if currentNode.value < parentNode.value:
							# parentNode.left = currentNode.left
						# elif currentNode.value > parentNode.value:
							# parentNode.right = currentNode.left
					
				# elif currentNode.left == None:
					# if parentNode is None:
						# self.root = currentNode.right
					# else:
						# if currentNode.value < parentNode.value:
							# parentNode.left = currentNode.right
						# elif currentNode.value > parentNode.value:
							# parentNode.right = currentNode.right
				# else:
					# leftmost = currentNode.right.left
					# letmostParent = currentNode.right
					# while leftmost.left is not None:
						# letmostParent = leftmost
						# leftmost = leftmost.left
						
					# leftmostParen.left = leftmost.right
					# leftmost.left = currentNode.left
					# leftmost.right = currentNode.right
					
					# if parentNode is None:
						# self.root = leftmost
					# else:
						# if currentNode.value < parentNode.value:
							# parentNode.left = leftmost
						# elif currentNode.value > parentNode.value:
							# parentNode.right = leftmost
					
				

	
	def trasverse(self, Node = None):
		if Node is None:
			Node = self.root
		print(Node.value)
		if Node.left is not None:
			self.trasverse(Node.left)
		if Node.right is not None:
			self.trasverse(Node.right)
		return Node
	
	
	
	
	# 		9
	#	4		20
	#1	6	15	170
	
	
def test():
	myTree = BinarySearchTree()
	myTree.insert(9)
	myTree.insert(4)
	myTree.insert(6)
	myTree.insert(20)
	myTree.insert(170)
	myTree.insert(15)
	myTree.insert(1)
	myTree.trasverse()
	myTree.delete(4)
	myTree.trasverse()