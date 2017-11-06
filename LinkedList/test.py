import sys 
sys.path.append('..')
import random
from test_tool import test
from linkedlist import LinkedList


allTestPassed = True
failedTestCases = []

testList = LinkedList()
testA = test(testList)

#Testing Bulk Insertion
expectedResult = [1,2,3,4,5]
testA.executeCommands("insertVal", [1,2,3,4,5], str(expectedResult))
allTestPassed = allTestPassed and testA.passed
failedTestCases.append(testA.failedCases)

#Testing Bulk Insertion
testList = LinkedList()
testB = test(testList)
expectedResult = [1,2,1,4,5,8,4,7,8]
testB.executeCommands("insertVal", [1,2,1,4,5,8,4,7,8], str(expectedResult))

# Singleton Removal
expectedResult = [2,1,4,5,8,4,7,8]
testB.executeCommands("removeOne", [1], str(expectedResult))
allTestPassed = allTestPassed and testB.passed
failedTestCases.append(testB.failedCases)

# Remove Many
expectedResult = [2,1,4,5,4,7]
testB.executeCommands("removeAll", [8], str(expectedResult))
allTestPassed = allTestPassed and testB.passed
failedTestCases.append(testB.failedCases)


if allTestPassed:
	print "All Test Cases Passed!"
else:
	print "The Following Test Cases Failed:"
	print failedTestCases

