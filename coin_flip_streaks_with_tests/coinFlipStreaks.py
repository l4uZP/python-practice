import random

def GetSixRandomFlips():
    flips = []
    for x in range(6):
        flip = GetRandomCoinSide()
        flips.append(flip)
    return flips

def GetRandomCoinSide():
    throw = random.randint(0,1)
    if throw == 0:
        return "H"
    elif throw == 1:
        return "T"
    
def CountTsAndHs(flips):
    h = 0
    t = 0
    for side in flips:
        if side == "T":
            t +=1
        elif side == "H":
            h +=1
    return t, h

def CalculatePercentage(flipTimes, streaks):
    percentage = streaks / flipTimes
    return percentage

def PrintReadablePercentage(percentage):
    res = percentage * 100
    return str(res) + "%"

def main():
    flips = GetSixRandomFlips()
    print("Flips: " + str(flips))


# main()