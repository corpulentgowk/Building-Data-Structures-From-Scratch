class test(object):
	def __init__(self, dataStruct):
		self.dataStruct = dataStruct
		self.passed = True
		self.failedCases = []

	def validateResult(self, expectedResult, testCase):
		if str(self.dataStruct) == expectedResult:
			self.passed = self.passed and True
		else:
			self.failedCases.append(testCase)
			self.passed = False

	def executeCommands(self, func, inputs, expectedResult):
		method = getattr(self.dataStruct, func)
		for inpt in inputs:
			method(inpt)
		self.validateResult(expectedResult, [func, inputs])