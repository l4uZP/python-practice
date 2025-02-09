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

def main():
    TestGetSixRandomFlipsItReturnsSixItems()
    TestGetRandomCoinSideBasicExample()
    TestCountTsAndHsBasicExample()
    TestCountTsAndHsAnotherBasicExample()
    TestGetSixRandomFlipsItReturnsOnlyTsAndHsArray()

main()