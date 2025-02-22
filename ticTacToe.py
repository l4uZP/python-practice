import random
import time

board = {"topL":" ", "topM":" ", "topR":" ", "midL":" ", "midM":" ", "midR":" ", "lowL":" ", "lowM":" ", "lowR":" "}
keepPlaying = True
turn = "user"

def printBoard():
    print(board["topL"] + " | " + board["topM"] + " | " + board["topR"])
    print("---------")
    print(board["midL"] + " | " + board["midM"] + " | " + board["midR"])
    print("---------")
    print(board["lowL"] + " | " + board["lowM"] + " | " + board["lowR"])

def printInstructions():
    print("\nIt's your turn")
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
    
def computerPlaying():
    print("\nComputer turn")
    time.sleep(0.5)
    print("\n...\n")
    time.sleep(1)
    
    while True:
        positions = list(board.keys())
        computerMove = positions[random.randint(0,len(positions)-1)]

        if isAvailable(computerMove):
            board[computerMove] = "o"
            break

        if noMovesLeft():
            finishGame()
            break

def noMovesLeft():
    if " " not in board.values():
        print("Draw!")
        return True
    return False

def userPlaying():
    while True:
        userMove = input()

        if isAvailable(userMove):
            board[userMove] = "x"
            break
        else:
            print("Space not available. Try again.")

def checkLine(pos1, pos2, pos3):
    if board[pos1] == board[pos2] == board[pos3] != " ":
        finishGame()
        print(turn + " wins")


def checkBoard():
    checkLine("topL","topM","topR")    
    checkLine("midL","midM","midR")
    checkLine("lowL","lowM","lowR")
    checkLine("topL","midL","lowL")
    checkLine("topM","midM","lowM")
    checkLine("topR","midR","lowR")
    checkLine("topL","midM","lowR")
    checkLine("topR","midM","lowL")
        

def finishGame():
    global keepPlaying
    keepPlaying = False
    print("Game Over")

def main():
    print("Start Game")
    printBoard()

    while keepPlaying:
        global turn
        if turn == "user":
            printInstructions()
            userPlaying()
        else:
            computerPlaying()

        printBoard()
        checkBoard()
        switchTurn()

main()