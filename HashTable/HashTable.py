
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

	def insert(self, key, value): 

		if self.numElements >= self.size:
			raise Exception("HashMap Full")

		ind = self.hashFunction(key)

		while self.buckets[ind]:

			if self.buckets[ind].key == key:
				self.numElements += 1
				self.buckets[ind].value = value #Update exisisting bucket key with new value.
				return #Insert complete/Could have alternatively breaked here and just made a new bucket. 

			ind += 1 #Increment the index until an empy bucket is found.
			ind = ind % self.size #Wraps back around to the beggining if the collision adjustment index out of bounds of array.
		
		self.buckets[ind] = Bucket(key, value)
		self.numElements += 1

	def remove(self, key):

		ind = self.hashFunction(key)
		startInd = ind

		while self.buckets[ind]:

			if self.buckets[ind].key != key:
				ind += 1

			else:
				self.numElements -= 1
				self.buckets[ind] = None #Free the location where the key already exists
				return

			if ind > self.size - 1: #Reached the end of the list of buckets
				ind = 0 #Continue searching from beggining. 

			if ind == startInd: #Back to where the probe started.
				raise Exception("The Hashtable does not contain the specified key")

		raise Exception("The Hashtable does not contain the specified key") #Encounter a NoneType in the Array
																			#Key Not found



h = HashMap()

for l in h.buckets:
	if l:
		print l.key, l.value

