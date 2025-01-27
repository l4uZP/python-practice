import sys
import random

print("ROCK SCISSORS PAPER")

wins = 0
looses = 0
ties = 0

options = {
    "r": ("rock", 0, "s"),
    "s": ("scissors", 1, "p"),
    "p": ("paper", 2, "r")
}


while True:
    print(str(wins) + " Wins - " + str(looses) + " Looses - " + str(ties) +" Ties \n")
    
    print("Enter your move:(r)ock - (p)aper - (s)cissors")
    print("Press (q) if you want to quit the game.")
    
    userInput = input()
    
    if userInput == "q":
        print("Bye! ;)")
        sys.exit()

    try:
        userOption = options[userInput]
    except:
        print("Thats not an option!")
        continue

    print(userOption[0].upper() + " versus...")

    computerNumber = random.randint(0, 2)
    computerOption = ""

    for option in options:
        if options[option][1] == computerNumber:
            print(options[option][0].upper())    
            computerOption =  option

    
    if userOption == options[computerOption]:
        print("Is a tie! :O")
        ties = ties + 1
    elif userOption[2] == computerOption:
        print("You win! :)")
        wins = wins + 1
    else:
        print("You loose! :(")
        looses = looses + 1

