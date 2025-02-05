import random
import os
import time

WIDTH = 3
HEIGH = 3


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
    os.system("clear")
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
            randMap[x][y] = toggleLife(randMap[x][y])



def countLivingNeighbors(x, y):
    ln = 0
    if randMap[x-1][y-1] == "#":
        ln+=1
    if randMap[x-1][y] == "#":
        ln+=1
    if randMap[x-1][y+1] == "#":
        ln+=1
    if randMap[x][y-1] == "#":
        ln+=1
    if randMap[x][y+1] == "#":
        ln+=1
    if randMap[x+1][y-1] == "#":
        ln+=1
    if randMap[x+1][y] == "#":
        ln+=1
    if randMap[x+1][y+1] == "#":
        ln+=1

    return ln


randMap = createMap()

printCurrentMap()
print(countLivingNeighbors(1,1))

# while True:
#     printCurrentMap()
#     nextStep()

