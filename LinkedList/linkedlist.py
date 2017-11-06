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
