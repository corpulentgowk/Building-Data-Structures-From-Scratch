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

	def executeCommands(self, func, inputs, expectedResult, truthy=False):
		method = getattr(self.dataStruct, func)
		if not truthy:
			if inputs:
				for inpt in inputs:
					method(inpt)
			else:
				method()
			self.validateResult(expectedResult, [func, inputs])
		else:
			truthness = method()
			self.validateTruth(expectedResult, truthness, [func])
