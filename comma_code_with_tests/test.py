import commaCode as cc

def isTrue(expected, result):
    if result == expected:
        print("Test passed")
        return
    else:
        print("Test failed")
        print("Expected: " + expected + "  Result: " + result)
        return
    
def TestCreateStringListBasicExample():
    a = ['a','b','c']
    expected = "a, b and c"
    result = cc.CreateStringList(a)
    isTrue(expected, result)

def TestCreateStringListAnotherBasicExample():
    a = ['c', 'd', 'e', 'f']
    expected = "c, d, e and f"
    result = cc.CreateStringList(a)
    isTrue(expected, result)

def TestCreateStringListWithOneNumber():
    a = ['c', 'd', 'e', 1]
    expected = "c, d, e and 1"
    result = cc.CreateStringList(a)
    isTrue(expected, result)

def TestCreateStringEmptyArray():
    a = []
    expected = ""
    result = cc.CreateStringList(a)
    isTrue(expected, result)

def TestCreateStringListWithBoolean():
    a = ['c', True, 'e', 1]
    expected = "c, True, e and 1"
    result = cc.CreateStringList(a)
    isTrue(expected, result)

def main():
    TestCreateStringListBasicExample()
    TestCreateStringListAnotherBasicExample()
    TestCreateStringListWithOneNumber()
    TestCreateStringEmptyArray()
    TestCreateStringListWithBoolean()

main()



# Say you have a list value like this: 
# spam = ['apples', 'bananas', 'tofu', 'cats'] 

# Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, with and inserted before the last item. For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'. But your function should be able to work with any list value passed to it. Be sure to test the case where an empty list [] is passed to your function.