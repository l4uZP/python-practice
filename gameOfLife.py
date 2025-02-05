import random
import os
import time

WIDTH = 10
HEIGH = 10


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



randMap = createMap()
while True:
    printCurrentMap()
    nextStep()