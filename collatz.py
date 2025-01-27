import sys

def collatz(number):
    if isEven(number):
        value = number // 2
        print(value)
        return value
    
    value = 3 * number + 1
    print(value)
    return value

        
def isEven(number):
    if (number%2) == 0:
        return True
    return False

print("Collatz sequence")
print("Please write a number:")
userInput = input()

try:
    number = int(userInput)
except: 
    print("You must enter an integer number!")
    sys.exit()
    
while number != 1:
    number = collatz(number)
