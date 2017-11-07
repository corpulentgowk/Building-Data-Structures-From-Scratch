class ListNode(object):
	def __init__(self, val):
		self.val = val
		self.next = None

class LinkedList(object):
	def __init__(self):
		self.root = None
	def __str__(self):
		curr = self.root
		collect = []
		while curr:
			collect.append(curr.val)
			curr = curr.next

		return str(collect)

	def insertVal(self, val):
		node = ListNode(val)
		if not self.root:
			self.root = node
		else:
			self.addToList(node)

	def addToList(self, node):
		curr = self.root
		while curr:
			if not curr.next:
				curr.next = node
				return
			curr = curr.next

	def removeOne(self, val):
		curr = self.root
		prev = None
		while curr:
			if curr.val == val:
				if curr.next: #Clone the next node into the current ndoe
					curr.val = curr.next.val
					curr.next = curr.next.next
				else: #Nothing Follows so sett curr to be None
					if prev:
						prev.next = None
					else:
						self.root = None #Reset Root
				return #Return after removing the first instance. 
			
			prev = curr
			curr = curr.next

	def removeAll(self, val):
		curr = self.root
		prev = None
		while curr:
			if curr.val == val:
				if curr.next: #Clone the next node into the current ndoe
					curr.val = curr.next.val
					curr.next = curr.next.next
					continue #Go to the next iteration without advancing the curr node point as the inherited value may be next in line
				else: 
					if prev: #Not at Root
						prev.next = None
					else:
						self.root = None #Reset Root.
			prev = curr
			curr = curr.next

	def isPalindrome(self):
		head = self.root
		return self.palindrome(head, head)[1]

	def palindrome(self, head, curr): 
		"""
		Recurs down to the last node(n-th node) and compares the head to the last node. 
		Returns the node that follows the head so that when the recursion pops back to the n-1th node its comparing to the 2nd node
		
		Area for improvement. This scans comparing the n == 0 | (n-1) == 1 | (n-2) == 2 | (n-3) == 3 | ....
		Once the compared nodes cross each other at the midpoint we know wether or not its a palindrome. No need to compare further.
		But it does not affect the time complexity as the recursive tree has to be back tracked regardless. Comparisons are O(1) and so
		would checking to see if you reached the midpoint. 

		Would also need an O(n) operation to determine the length. Alternatively I could 
		Reformat this data structure to keep track of the current length of the linked list. Dec/Inc as nodes are added or removed but I wanted to make
		A palindrome function that can be generalized to any standard Linked List. 
		"""
		if not curr.next:
			#print head.val, curr.val
			if curr.val == head.val:
				return [head.next, True]
			else:
				return [head.next, False]
		localCurr = curr
		res = self.palindrome(head, curr.next)
		#print res[0].val, curr.val

		if res[1] == False:
			return [res[0].next, False] #Short Circuit after the first mismatch. No need to continue comparisons
		else:
			if res[0].val == curr.val:
				return [res[0].next, True]
			else:
				return [res[0].next, False]




