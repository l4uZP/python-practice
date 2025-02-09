import sys

def Equals(result, expected):
    if result == expected:
        print("Test passed: Equal values.")
        return
    else:
        print("Test failed")
        print("Result: " + str(result) + " Expected: " + str(expected))
        sys.exit()

def EqualsOrEquals(result, expectedS):
    try:
         expectedS.index(result)
         print("Test passed: Result Found in Expected possibilities")
         return
    except:
        print("Test failed")
        print(" Result: " + result + " ExpectedS: " + str(expectedS))
        sys.exit()