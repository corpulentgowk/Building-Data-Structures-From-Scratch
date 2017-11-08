from linkedlist import LinkedList, ListNode

class HashBucket(object):

	def __init__(self, size=131): #131 is a prime number
		self.size = size
		self.bucket = [None] * size

	def hashFunction(self, key):
		return hash(key) % self.size

	def insert(self, key, value):
		ind = self.hashFunction(key)
		if self.bucket[ind]:
			self.addToChain(ind, key, value)
		else:
			self.createChain(ind, key, value)

	def remove(self, key):
		ind = self.hashFunction(key)
		try:
			if self.bucket[ind]:
				self.removeFromChain(ind, key)
			else:
				raise Exception()
		except:
			print "KeyError: '" + str(key) + "'"
			return 

		if not self.bucket[ind].root: #Checks if Removal was off the root node in Linked List
			self.bucket[ind] = None #If so reset the bucket to None

	def createChain(self, ind, key, value):
		chain = LinkedList()

		chain.insertVal(key,value)
		self.bucket[ind] = chain

	def addToChain(self, ind, key, value):
		chain = self.bucket[ind]     #Have to search through the nodes manually
		curr = chain.root			 #Ensure that that the key does not already exist
		
		while curr:
			currKey = curr.key
			if currKey == key:
				curr.val = value #Replace the value with the same key with the new value
				break

			if not curr.next:
				curr.next = ListNode(key,value)
				break
			curr = curr.next

	def removeFromChain(self, ind, key):
		chain = self.bucket[ind].removeOne(key)


'''
Hash = HashBucket()

Hash.insert(1,"wrecked")
Hash.insert(132,"wrecked")
Hash.insert(132,"Change of Heart")
Hash.insert(133, "hey")
Hash.insert(2, "hi")

for l in Hash.bucket:
	if l:
		print str(l)
'''