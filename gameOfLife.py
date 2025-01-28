import random

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
    for row in randMap:
        print(row)


randMap = createMap()
printCurrentMap()