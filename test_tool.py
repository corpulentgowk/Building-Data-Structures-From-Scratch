class test(object):
	def __init__(self, dataStruct):
		self.dataStruct = dataStruct
		self.passed = True
		self.failedCases = []

	def validateResult(self, expectedResult, testCase):
		if str(self.dataStruct) == expectedResult:
			self.passed = self.passed and True
		else:
			testCase += [str(self.dataStruct), "Expected: '" + str(expectedResult) + "' Got: '" + str(self.dataStruct) + "'. "]
			self.failedCases.append(testCase)
			self.passed = False

	def validateTruth(self, expectedResult, truthness, testCase):
		if truthness == expectedResult:
			self.passed = self.passed and True
		else:
			testCase += [str(self.dataStruct), "Expected: '" + str(expectedResult) + "' Got: '" + str(truthness) + "'. "]
			self.failedCases.append(testCase)
			self.passed = False

	def executeCommands(self, func, inputs, expectedResult, ret=False, skipValidation = False):
		method = getattr(self.dataStruct, func)
		
		if not ret: #If no return is expected
			if inputs:
				for inpt in inputs:
					if type(inpt) is list: #If there are more than one argument to each method
						self.funcMap(method, inpt)
					else:
						method(inpt)
			else:
				method()
			if not skipValidation:
				self.validateResult(expectedResult, [func, inputs])
		else:
			if inputs:
				truthness = True #Here if the return type is true or false. True and "Somestring" yeilds "Somestring"
				for inpt in inputs:
					if type(inpt) is list: #If there are more than one argument to each method
						truthness = truthness and self.funcMap(method, inpt)
					else:
						truthness = truthness and method(inpt)
			else:
				truthness = method()
			if not skipValidation:
				self.validateTruth(expectedResult, truthness, [func])
	
	def funcMap(self, func, args): 
		return func(*args)