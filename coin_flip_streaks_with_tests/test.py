import coinFlipStreaks as cfs
import testHelpers as test


def TestGetSixRandomFlipsItReturnsSixItems():
    flips = cfs.GetSixRandomFlips()
    test.Equals(len(flips), 6) 

def TestGetRandomCoinSideBasicExample():
    side = cfs.GetRandomCoinSide()
    test.EqualsOrEquals(side, ["T", "H"])

def TestCountTsAndHsBasicExample():
    flips = ["T","T","T","H","H","H"]
    t, h = cfs.CountTsAndHs(flips)
    test.Equals(t, 3)
    test.Equals(h, 3)

def TestCountTsAndHsAnotherBasicExample():
    flips = ["T","T","T","H","H","T"]
    t, h = cfs.CountTsAndHs(flips)
    test.Equals(t, 4)
    test.Equals(h, 2)

def TestGetSixRandomFlipsItReturnsOnlyTsAndHsArray():
    flips = cfs.GetSixRandomFlips()
    for flip in flips:
        test.EqualsOrEquals(flip, ["H","T"])

def TestCalculatePercentageWorksWithBasicExample():
    flipTimes = 100
    streaks = 10
    p = cfs.CalculatePercentage(flipTimes, streaks)
    test.Equals(p, 0.1)
    
def TestCalculatePercentageWorksWithAnotherBasicExample():
    flipTimes = 10000
    streaks = 10
    p = cfs.CalculatePercentage(flipTimes, streaks)
    test.Equals(p, 0.001)

def TestPrintReadablePercentageWorksWithSomeBasicExamples():
    p1 = 0.1
    p2 = 0.01
    p3 = 0.0001
    p4 = 1
    r1 = cfs.PrintReadablePercentage(p1)
    r2 = cfs.PrintReadablePercentage(p2)
    r3 = cfs.PrintReadablePercentage(p3)
    r4 = cfs.PrintReadablePercentage(p4)
    test.Equals(r1, "10.0%")
    test.Equals(r2, "1.0%")
    test.Equals(r3, "0.01%")
    test.Equals(r4, "100%")

def main():
    TestGetSixRandomFlipsItReturnsSixItems()
    TestGetRandomCoinSideBasicExample()
    TestCountTsAndHsBasicExample()
    TestCountTsAndHsAnotherBasicExample()
    TestGetSixRandomFlipsItReturnsOnlyTsAndHsArray()
    TestCalculatePercentageWorksWithBasicExample()
    TestCalculatePercentageWorksWithAnotherBasicExample()
    TestPrintReadablePercentageWorksWithSomeBasicExamples()

main()