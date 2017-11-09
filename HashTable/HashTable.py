
class Bucket(object):
	def __init__(self, key, value):
		self.key = key
		self.value = value

class HashMap(object):

	def __init__(self, size = 1 << 8): #256 / Power of 2
		self.size = size
		self.numElements = 0
		self.buckets = [None] * size

	def hashFunction(self, key):
		return hash(key) % self.size

	def rehash(self, newSize):
		self.size = newSize
		oldBuckets = self.buckets
		self.buckets = [None] * newSize
		self.numElements = 0

		for bucket in oldBuckets:
			if bucket:
				self.insert(bucket.key, bucket.value)


	def insert(self, key, value): 

		if self.numElements >= self.size:
			raise Exception("FATAL ERROR: HashMap Full")

		ind = self.hashFunction(key)

		while self.buckets[ind]:

			if self.buckets[ind].key == key:
				self.buckets[ind].value = value #Update exisisting bucket key with new value.
				return #Insert complete/Could have alternatively breaked here and just made a new bucket. 

			ind += 1 #Increment the index until an empy bucket is found.
			ind = ind % self.size #Wraps back around to the beggining if the collision adjustment index out of bounds of array.
		
		self.buckets[ind] = Bucket(key, value)
		self.numElements += 1

		if (float(self.numElements)/float(self.size)) > .75:
			self.rehash(self.size << 1) #Double Size of Hash Table and Rehash the elements

	def remove(self, key):

		ind = self.hashFunction(key)
		startInd = ind

		while self.buckets[ind]:

			if self.buckets[ind].key == key:
				self.numElements -= 1
				self.buckets[ind] = None #Free the location where the key already exists

				if (float(self.numElements)/float(self.size)) < .25:
					self.rehash(self.size >> 1) #Halve the Size of Hash Table and Rehash the elements

				return
			
			ind += 1

			if ind > self.size - 1: #Reached the end of the list of buckets.
				ind = 0 #Continue searching from beggining. 

			if ind == startInd: #Back to where the probe started.
				raise Exception("The Hashtable does not contain the specified key")

		raise Exception("The Hashtable does not contain the specified key") 
		#Encountered a NoneType in the Array which broke the While Loop However, the key was not found.
		#Does not exist

	def lookup(self, key):

		ind = self.hashFunction(key)
		startInd = ind

		while self.buckets[ind]:

			if self.buckets[ind].key == key:
				return self.buckets[ind].value
			
			ind += 1

			if ind > self.size - 1: 
				ind = 0 

			if ind == startInd: 
				raise Exception("The Hashtable does not contain the specified key")

		raise Exception("The Hashtable does not contain the specified key") 
		#Encountered a NoneType in the Array which broke the While Loop However, the key was not found.
		#Does not exist

	def isIn(self, key):

		ind = self.hashFunction(key)
		startInd = ind

		while self.buckets[ind]:

			if self.buckets[ind].key == key:
				return True
			
			ind += 1

			if ind > self.size - 1: 
				ind = 0 

			if ind == startInd: 
				return False

		return False 

