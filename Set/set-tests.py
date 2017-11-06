import random
import set as SET
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


allTestPassed = True
failedTestCases = []

testSet = SET.custom_set()
testA = test(testSet)

#Testing Bulk Insertion
expectedResult = [{1: 0, 2: 1, 3: 2, 4: 3, 5: 4}, [1, 2, 3, 4, 5]]
testA.executeCommands("insert", [1,2,3,4,5], str(expectedResult))
allTestPassed = allTestPassed & testA.passed
failedTestCases.append(testA.failedCases)

#Testing Removal
expectedResult = [{5: 0, 2: 1, 3: 2, 4: 3}, [5, 2, 3, 4]]
testA.executeCommands("remove", [1], str(expectedResult))
allTestPassed = allTestPassed & testA.passed
failedTestCases.append(testA.failedCases)


#Testing Inserting Duplicate Element
expectedResult = [{5: 0, 2: 1, 3: 2, 4: 3}, [5, 2, 3, 4]]
testA.executeCommands("insert", [5], str(expectedResult))
allTestPassed = allTestPassed & testA.passed
failedTestCases.append(testA.failedCases)

if allTestPassed:
	print "All Test Cases Passed!"
else:
	print "The Following Test Cases Failed:"
	print failedTestCases






