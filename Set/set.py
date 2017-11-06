import random
class custom_set(object):
	def __init__(self):
		self.set = {}
		self.values = []
	def __str__(self):
		return str([self.set, self.values])

	def isIn(self, val):
		if val in self.set:
			return True
		return False
	def insert(self, val):
		if not val in self.set:
			self.values.append(val)
			self.set[val] = len(self.values) - 1
		return
	def remove(self, val):
		if val in self.set:
			ind = self.set[val]
			del self.set[val]
			self.values[ind] = self.values[len(self.values) - 1]
			self.set[self.values[ind]] = ind
			self.values = self.values[:-1]
			return

		raise Exception("Element not in set")

	def random(self):
		ind = random.randrange(len(self.set.keys()))
		return self.set[ind]


