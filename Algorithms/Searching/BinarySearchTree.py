from collections import deque	

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
					
				

	
	def DFS(self, Node = None):
		if Node is None:
			Node = self.root
		print(Node.value)
		if Node.left is not None:
			self.DFS(Node.left)
		if Node.right is not None:
			self.DFS(Node.right)
		return Node
		
	def DFSInOrder(self, list, Node = None):
		if Node is None:
			Node = self.root
		if Node.left is not None:
			self.DFSInOrder(list, Node.left)
			
		list.append(Node.value)
		
		if Node.right is not None:
			self.DFSInOrder(list, Node.right)
		return list
		
	def DFSPreOrder(self, list, Node = None):
		if Node is None:
			Node = self.root
			
		list.append(Node.value)
		
		if Node.left is not None:
			self.DFSPreOrder(list, Node.left)
		if Node.right is not None:
			self.DFSPreOrder(list, Node.right)
		return list
		
	def DFSPostOrder(self, list, Node = None):
		if Node is None:
			Node = self.root
		
		if Node.left is not None:
			self.DFSPostOrder(list, Node.left)
		if Node.right is not None:
			self.DFSPostOrder(list, Node.right)
		
			
		list.append(Node.value)
		
		return list
	
	
	def BFS(self):
		currentNode = self.root
		list = []
		queue = deque()
		queue.append(currentNode)
		while len(queue) > 0:
			currentNode = queue.popleft()
			list.append(currentNode.value)
			if currentNode.left is not None:
				queue.append(currentNode.left)
			if currentNode.right is not None:
				queue.append(currentNode.right)
		return list
	

	
	def BFSRecursive(self, queue, list):
		if len(queue) == 0:
			return list
		currentNode = queue.popleft()
		list.push(currentNode.value)
		if currentNode.left is not None:
			queue.append(currentNode.left)
		if currentNode.right is not None:
			queue.append(currentNode.right)
		
		return BFSRecursive(queue, list)
	
	'''
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.

 

Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true

Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
'''
	def ValidateBST(self):
		currentNode = self.root
		list = []
		queue = deque()
		queue.append(currentNode)
		while len(queue) > 0:
			currentNode = queue.popleft()
			list.append(currentNode.value)
			if currentNode.left is not None:
				if currentNode.left.value > currentNode.value:
					return False
				queue.append(currentNode.left)
			if currentNode.right is not None:
				if currentNode.right.value < currentNode.value:
					return False
				queue.append(currentNode.right)
		return True
		
	def arrayToTree(self, array):
		self.root = None
		for element in array:
			if(element is not None):
				self.insert(element)
	
	#def DFS(self):
		
	
	# 		9
	#	4		20
	#1	6	15	170
	
#inOrder -> [1,4,6,9,15,20,170]
#preOrder -> [9,4,1,6,20,15,170]
#PostOrder[1,6,4,15,170,20,9]	
def test():
	myTree = BinarySearchTree()
	myTree.insert(9)
	myTree.insert(4)
	myTree.insert(6)
	myTree.insert(20)
	myTree.insert(170)
	myTree.insert(15)
	myTree.insert(1)
	#myTree.trasverse()
	#myTree.delete(4)
	#myTree.trasverse()
	#myTree.BFS()
	print(myTree.DFSInOrder([]))
	print(myTree.DFSPreOrder([]))
	print(myTree.DFSPostOrder([]))
	
def test2():
	myTree = BinarySearchTree()
	myTree.arrayToTree([2,1,3])
	print(myTree.DFSPreOrder([]))
	print(myTree.ValidateBST())
	
	myTree = BinarySearchTree()
	#myTree.arrayToTree([5,1,4,None,None,3,6])
	node0 = BinaryTreeNode(5)
	node1 = BinaryTreeNode(1)
	node2 = BinaryTreeNode(4)
	node3 = BinaryTreeNode(3)
	node4 = BinaryTreeNode(6)
	myTree.root = node0
	node0.left = node1
	node0.right = node2
	node2.left = node3
	node3.right = node4
	print(myTree.DFSPreOrder([]))
	print(myTree.ValidateBST())
