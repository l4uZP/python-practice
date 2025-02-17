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

def TestReadablePercentageWorksWithSomeBasicExamples():
    p1 = 0.1
    p2 = 0.01
    p3 = 0.0001
    p4 = 1
    r1 = cfs.ReadablePercentage(p1)
    r2 = cfs.ReadablePercentage(p2)
    r3 = cfs.ReadablePercentage(p3)
    r4 = cfs.ReadablePercentage(p4)
    test.Equals(r1, "10.0%")
    test.Equals(r2, "1.0%")
    test.Equals(r3, "0.01%")
    test.Equals(r4, "100%")

def TestIsAStreakReturnsTrueWhenSixConsecutiveFlipsAreTheSame():
    hs = ["H","H","H","H","H","H"]
    ts = ["T","T","T","T","T","T"]

    r1 = cfs.IsAStreak(hs)
    r2 = cfs.IsAStreak(ts)

    test.Equals(r1, True)
    test.Equals(r2, True)

def TestIsAStreakReturnsFalseWhenSixConsecutiveFlipsAreNotTheSame():
    f1 = ["H","H","H","T","H","H"]
    f2 = ["T","T","H","T","T","T"]

    r1 = cfs.IsAStreak(f1)
    r2 = cfs.IsAStreak(f2)

    test.Equals(r1, False)
    test.Equals(r2, False)


def main():
    TestGetSixRandomFlipsItReturnsSixItems()
    TestGetRandomCoinSideBasicExample()
    TestCountTsAndHsBasicExample()
    TestCountTsAndHsAnotherBasicExample()
    TestGetSixRandomFlipsItReturnsOnlyTsAndHsArray()
    TestCalculatePercentageWorksWithBasicExample()
    TestCalculatePercentageWorksWithAnotherBasicExample()
    TestReadablePercentageWorksWithSomeBasicExamples()
    TestIsAStreakReturnsTrueWhenSixConsecutiveFlipsAreTheSame()
    TestIsAStreakReturnsFalseWhenSixConsecutiveFlipsAreNotTheSame()


main()