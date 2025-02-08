import random

print("Let's play a game :)")
print("I'm thinking of a number between 1 and 20.")

number = random.randint(1,20)
win = False

print("Take a guess...")
print("But remember, you only have 6 chances.")

for tryNumber in range(6):
    print("Try "+ str(tryNumber+1))
    guess = input()
    
    if int(number) != int(guess):
        print("Wrong!")
        continue
    else:
        print("You guessed the number in "+ str(tryNumber+1) +" guesses. Congratulations.")
        win = True
        break
    
if not win:
    print("You loose. The number was: " + str(number))

print("Game over.")