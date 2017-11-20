import sys 
sys.path.append('..')
from test_tool import test
from trie import trieTree

allTestPassed = True
failedTestCases = []


#Bulk Insertion
testA = test(trieTree())
expectedResult = []
testA.executeCommands("insert", ["hello","hellbent", "healthy", "hell", "pears", "pear", "race", "racecar"], str(expectedResult),False, True) #Not a Truth Assertion/Skip Validation

expectedResult = True
testA.executeCommands("isWord", ["hell"], expectedResult, True)

expectedResult = True
testA.executeCommands("isWord", ["race"], expectedResult, True)

expectedResult = False
testA.executeCommands("isWord", ["raceca"], expectedResult, True)

expectedResult = True
testA.executeCommands("isWord", ["racecar"], expectedResult, True)

expectedResult = True
testA.executeCommands("isWord", ["pear"], expectedResult, True)

expectedResult = False
testA.executeCommands("isWord", ["pea"], expectedResult, True)

expectedResult = False
testA.executeCommands("isWord", ["hel"], expectedResult, True)

expectedResult = True
testA.executeCommands("isPrefix", ["hell"], expectedResult, True)

#Edge case for isPrefix
expectedResult = False
testA.executeCommands("isPrefix", ["hellbent"], expectedResult, True)

expectedResult = True
testA.executeCommands("isPrefix", ["raceca"], expectedResult, True)
expectedResult = True
testA.executeCommands("isPrefix", ["pea"], expectedResult, True)
expectedResult = True
testA.executeCommands("isPrefix", ["hel"], expectedResult, True)


allTestPassed = allTestPassed and testA.passed
if not testA.passed:
	failedTestCases += testA.failedCases

if allTestPassed:
	print "All Test Cases Passed!"
else:
	print "The Following Test Cases Failed:"
	print failedTestCases


