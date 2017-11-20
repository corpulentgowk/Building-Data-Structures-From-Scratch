import sys 
sys.path.append('..')
from test_tool import test
from HashTable import HashMap

h = HashMap()


allTestPassed = True
failedTestCases = []

#Testing Insertion and Lookups
testA = test(HashMap())
expectedResult = []
testA.executeCommands("insert", [[1,"one"],[2,"two"],[3,"three"],[4,"four"],[5, "five"]], str(expectedResult),False, True) #Not a Truth Assertion/Skip Validation

expectedResult = True
testA.executeCommands("isIn", [5], expectedResult, True)

expectedResult = "five"
testA.executeCommands("lookup",[5], expectedResult, True)

expectedResult = "one"
testA.executeCommands("lookup",[1], expectedResult, True)

#Validating Removals
expectedResult = True
testA.executeCommands("remove", [5], expectedResult, False, True) #Skip Validation of removal

expectedResult = False
testA.executeCommands("isIn", [5], expectedResult, True)

#Validating Reinsertions
expectedResult = "newFive"
testA.executeCommands("insert", [[5, "newFive"]], expectedResult, False, True) #Skip Validation of insert

expectedResult = True
testA.executeCommands("isIn", [5], expectedResult, True)

expectedResult = "newFive"
testA.executeCommands("lookup",[5], expectedResult, True)


allTestPassed = allTestPassed and testA.passed
if not testA.passed:
	failedTestCases += testA.failedCases



if allTestPassed:
	print "All Test Cases Passed!"
else:
	print "The Following Test Cases Failed:"
	print failedTestCases
