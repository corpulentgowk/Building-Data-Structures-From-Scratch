class trieTree(object):
	def __init__(self, root={}):
		self.root = root
	
	def insert(self, word):
		curr_node = self.root

		for char in word:
			if char in curr_node:
				curr_node = curr_node[char] #If the char is already present proceed to that node
			else:
				curr_node[char] = {} #Create the child in the node
				curr_node = curr_node[char] #Proceed down the next child
		curr_node["End"] = None #Marks that the current letter marks the end of a word

	def isWord(self, word):

		curr_node = self.root

		for char in word:
			if char in curr_node:
				curr_node = curr_node[char] 
			else:
				return False

		if "End" in curr_node:
			return True
		else:
			return False

	def isPrefix(self, word):
		curr_node =self.root

		for char in word:
			if char in curr_node:
				curr_node = curr_node[char]
			else:
				return False
				
		if "End" in curr_node:
			return len(curr_node) >= 2 #Must contain at least 2 keys. One for "End" and another for at least on char child.
		else:
			return len(curr_node) >= 1 #Not the end of the word so it must contain at 

