import random
import os
import time
import sys

WIDTH = 20
HEIGH = 15


def createMap():
    rows = []
    for x in range(WIDTH):
        column = []
        for y in range(HEIGH):
            if random.randint(0, 1) == 0:
                column.append("#")
            else:
                column.append(" ")
        rows.append(column)
    return rows


def printCurrentMap():
    os.system("clear") #This will only work on linux.
    for row in randMap:
        print(row)


def toggleLife(cell):
    if cell == "#":
        return " "
    else:
        return "#"


def nextStep():
    time.sleep(1)
    for x in range(len(randMap)):
        for y in range(len(randMap[x])):
            if randMap[x][y] == "#" and (countLivingNeighbors(x,y) < 2 or countLivingNeighbors(x,y) > 3):
                randMap[x][y] = toggleLife(randMap[x][y])
            elif randMap [x][y] == " " and countLivingNeighbors(x,y) == 3:
                randMap[x][y] = toggleLife(randMap[x][y])
            else:
                randMap[x][y] = randMap[x][y]
                

def countLivingNeighbors(x, y):
    ln = 0

    #maybe I should find a better or cleaner way to handle this
    col = y+1    
    if col >= HEIGH:
        col = 0
    row = x+1
    if row >= WIDTH:
        row = 0

    if randMap[x-1][y-1] == "#":
        ln+=1
    if randMap[x-1][y] == "#":
        ln+=1
    if randMap[x-1][col] == "#":
        ln+=1
    if randMap[x][y-1] == "#":
        ln+=1
    if randMap[x][col] == "#":
        ln+=1
    if randMap[row][y-1] == "#":
        ln+=1
    if randMap[row][y] == "#":
        ln+=1
    if randMap[row][col] == "#":
        ln+=1

    return ln


randMap = createMap()

try:
    while True:
        printCurrentMap()
        nextStep()
except:
    sys.exit()