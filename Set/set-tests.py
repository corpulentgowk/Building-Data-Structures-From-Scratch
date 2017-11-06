import sys 
sys.path.append('..')
import random
import test_tool as TEST
import set as SET

allTestPassed = True
failedTestCases = []

testSet = SET.custom_set()
testA = TEST.test(testSet)

#Testing Bulk Insertion
expectedResult = [{1: 0, 2: 1, 3: 2, 4: 3, 5: 4}, [1, 2, 3, 4, 5]]
testA.executeCommands("insert", [1,2,3,4,5], str(expectedResult))
allTestPassed = allTestPassed & testA.passed
failedTestCases.append(testA.failedCases)

#Testing Removal
expectedResult = [{5: 0, 2: 1, 3: 2, 4: 3}, [5, 2, 3, 4]]
testA.executeCommands("remove", [1], str(expectedResult))
allTestPassed = allTestPassed and testA.passed
failedTestCases.append(testA.failedCases)


#Testing Inserting Duplicate Element
expectedResult = [{5: 0, 2: 1, 3: 2, 4: 3}, [5, 2, 3, 4]]
testA.executeCommands("insert", [5], str(expectedResult))
allTestPassed = allTestPassed and testA.passed
failedTestCases.append(testA.failedCases)

if allTestPassed:
	print "All Test Cases Passed!"
else:
	print "The Following Test Cases Failed:"
	print failedTestCases






