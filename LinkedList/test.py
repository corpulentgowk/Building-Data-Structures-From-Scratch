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
if not testA.passed:
	failedTestCases += testA.failedCases

#Testing Bulk Insertion
testList = LinkedList()
testB = test(testList)
expectedResult = [1,2,1,4,5,8,4,7,8]
testB.executeCommands("insertVal", [1,2,1,4,5,8,4,7,8], str(expectedResult))

# Singleton Removal
expectedResult = [2,1,4,5,8,4,7,8]
testB.executeCommands("removeOne", [1], str(expectedResult))
allTestPassed = allTestPassed and testB.passed

# Remove Many
expectedResult = [2,1,4,5,4,7]
testB.executeCommands("removeAll", [8], str(expectedResult))

allTestPassed = allTestPassed and testB.passed
if not testB.passed:
	failedTestCases += testB.failedCases

#Testing Is Palindrome
testList = LinkedList()
testC = test(testList)
expectedResult = [1,1,2,2,1,1]
testC.executeCommands("insertVal", [1,1,2,2,1,1], str(expectedResult))
expectedResult = True
testC.executeCommands("isPalindrome", [], expectedResult, True) #This is a truthy test

testC.dataStruct = LinkedList() #Reinitialzie the List in the same test
expectedResult = [1,1,2,2,1]
testC.executeCommands("insertVal", [1,1,2,2,1], str(expectedResult))
expectedResult = False
testC.executeCommands("isPalindrome", [], expectedResult, True)

testC.dataStruct = LinkedList()
expectedResult = ["a", "b", "c", "d", "c", "b", "a"]
testC.executeCommands("insertVal",  ["a", "b", "c", "d", "c", "b", "a"], str(expectedResult))
expectedResult = True
testC.executeCommands("isPalindrome", [], expectedResult, True)

testC.dataStruct = LinkedList()
expectedResult = ["a", "b", "b", "a"]
testC.executeCommands("insertVal",  ["a", "b", "b", "a"], str(expectedResult))
expectedResult = True
testC.executeCommands("isPalindrome", [], expectedResult, True)

testC.dataStruct = LinkedList()
expectedResult = ["a", "b", "b", "d"]
testC.executeCommands("insertVal",  ["a", "b", "b", "d"], str(expectedResult))
expectedResult = False
testC.executeCommands("isPalindrome", [], expectedResult, True)

testC.dataStruct = LinkedList()
expectedResult = ["a", "b", "c", "d", "c", "b"]
testC.executeCommands("insertVal",  ["a", "b", "c", "d", "c", "b"], str(expectedResult))
expectedResult = False
testC.executeCommands("isPalindrome", [], expectedResult, True)

testC.dataStruct = LinkedList()
expectedResult = ["a"]
testC.executeCommands("insertVal",  ["a"], str(expectedResult))
expectedResult = True
testC.executeCommands("isPalindrome", [], expectedResult, True)

allTestPassed = allTestPassed and testC.passed
if not testC.passed:
	failedTestCases += testC.failedCases

if allTestPassed:
	print "All Test Cases Passed!"
else:
	print "The Following Test Cases Failed:"
	print failedTestCases

