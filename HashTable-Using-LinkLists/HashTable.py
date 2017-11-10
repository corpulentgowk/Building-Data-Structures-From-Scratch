from linkedlist import LinkedList, ListNode

class HashBucket(object):

	def __init__(self, size=131): #131 is a prime number
		self.size = size
		self.bucket = [None] * size
		self.numElements = 0

	def hashFunction(self, key):
		return hash(key) % self.size

	def rehash(self, newSize):
		self.size = newSize
		oldBucket = self.bucket

		self.bucket = [None] * newSize
		self.numElements = 0

		for chain in oldBucket:
			if chain:
				curr = chain.root
				while curr:
					self.insert(curr.key, curr.val)
					curr = curr.next

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


	def createChain(self, ind, key, value):
		chain = LinkedList()
		chain.insertVal(key,value)
		self.bucket[ind] = chain

		self.numElements += 1

		if (float(self.numElements)/float(self.size)) > .75:
			self.rehash(self.size << 1) #Double Size of Hash Table and Rehash the elements

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
				self.numElements += 1

				if (float(self.numElements)/float(self.size)) > .75:
					self.rehash(self.size << 1) #Double Size of Hash Table and Rehash the elements

				break
			curr = curr.next

	def removeFromChain(self, ind, key):
		chain = self.bucket[ind]

		chain.removeOne(key)

		if not self.bucket[ind].root: #Checks if Removal was off the root node in Linked List
			self.bucket[ind] = None #If so reset the bucket to None

		self.numElements -= 1
		if (float(self.numElements)/float(self.size)) < .25:
			self.rehash(self.size >> 1) #Halve the Size of Hash Table and Rehash the elements


'''
Hash = HashBucket(4) #Init HashMap of size 4

Hash.insert(1,"one")
Hash.insert(2,"two")
Hash.insert(3, "three")
Hash.insert(4, "four")

Hash.remove(2)
Hash.remove(1)
Hash.remove(3)

Hash.insert(6, "six")


print Hash.bucket

for l in Hash.bucket:
	if l:
		print str(l)
'''