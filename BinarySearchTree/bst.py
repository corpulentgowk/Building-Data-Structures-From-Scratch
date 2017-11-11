class node(object):
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = left

class BST(object):

	def __init__(self):
		self.root = None

	def insert(self, val):
		if not self.root:
			self.root = node(val)
			return

		curr = self.root

		while curr:
			if val < curr.val:
				if curr.left:
					curr = curr.left
					continue
				curr.left = node(val)
				break

			elif val > curr.val:
				if curr.right:
					curr = curr.right
					continue
				curr.right = node(val)
				break
			else:
				raise Exception("Duplicate Key") #This BST Does not Allow for Duplicates. 
	def remove(self, val):
		self.delete(val, self.root)
	def delete(self, val, currNode):
		'''
		Replacing has three cases. 

		Case 1: The node to replace is a leaf node. Then you set the pointer referenecing it in the parent to None. 

		Case 2: The node has one child. Redirect the parent pointer to its single child. 

		Case 3: The node has two children. Replace the node with the smallest node in its right subtree
		or replace the node with the largest value in its left subtree so the BST properties hold true. 
		'''
		
		if not currNode: #Null Node
			return None

		if val == currNode.val:
			if not currNode.left and not currNode.right: #Case 1
				return None
			if not currNode.left: #Case 2
				return currNode.right
			if not currNode.right: #Case 2
				return currNode.left

			#Case 3
			smallest = self.fetchSmallestNode(currNode.right)
			currNode.val = smallest.val

			currNode.right = self.delete(smallest.val, currNode.right)
			return currNode

		elif val < currNode.val:
			currNode.left = self.delete(val, currNode.left)
			return currNode
		else:
			currNode.right = self.delete(val, currNode.right)
			return currNode

	def fetchSmallestNode(self, subTreeRoot):
		curr = subTreeRoot
		while curr.left:
			curr = curr.left
		return curr
	def lookup(self, val, currNode = False):

		if currNode == False: #Defaults to False for Ease of Use
			currNode = self.root

		if not currNode: #Null Node
			return False 

		if currNode.val == val:
			return True 

		if val < currNode.val:
			return self.lookup(val, currNode.left)
		else:
			return self.lookup(val, currNode.right)




a = BST()

a.insert(2)
a.insert(1)
a.insert(10)
a.insert(7)
a.insert(8)
a.insert(9)
a.insert(11)
a.insert(14)

a.insert(12)

print a.lookup(2)
a.remove(2)
a.remove(1)

print a.lookup(1)


