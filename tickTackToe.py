import random

board = {"topL":" ", "topM":" ", "topR":" ", "midL":" ", "midM":" ", "midR":" ", "lowL":" ", "lowM":" ", "lowR":" "}
keepPlaying = True
turn = "user"

def printBoard():
    print(board["topL"] + " | " + board["topM"] + " | " + board["topR"])
    print("---------")
    print(board["midL"] + " | " + board["midM"] + " | " + board["midR"])
    print("---------")
    print(board["lowL"] + " | " + board["lowM"] + " | " + board["lowR"])

def printPositions():
    print("It's your turn")
    print("Choose your position: ")
    print("\ntopL, topM, topR")
    print("midL, midM, midR")
    print("lowL, lowM, lowR\n")

def switchTurn():
    global turn
    if turn == "user":
        turn = "computer"
    else:
        turn = "user"

def isAvailable(move):
    if move not in board.keys():
        return False
    
    if board[move] == " ":
        return True
    else:
        return False
    
def computerPlay():
    while True:
        positions = list(board.keys())
        computerMove = positions[random.randint(0,len(positions)-1)]
        if isAvailable(computerMove):
            board[computerMove] = "o"
            break

# def userPlay():

def main():
    print("Start Game")
    printBoard()

    while keepPlaying:
        global turn
        if turn == "user":
            printPositions()

            userMove = input()

            if isAvailable(userMove):
                board[userMove] = "x"
            else:
                print("Space not available. Try again.")
                continue

        else:
            print("Computer turn")

            computerPlay()

        printBoard()
        switchTurn()
main()