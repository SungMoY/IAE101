# Sung Mo Yang
# 112801117
# sungyang
#
# IAE 101 (Fall 2022)
# HW 1, Problem 5

from time import time


def how_long(distance, fraction, scale):
    c = 186000
    # ADD YOUR CODE HERE
    #check if distance and fraction are positive?
    timeInSeconds = distance / (fraction * c)
    match scale:
        case "M":
            return timeInSeconds/60
        case "H":
            return timeInSeconds/3600
        case "D":
            return timeInSeconds/(3600 * 24)
        case "Y":
            return timeInSeconds/(3600 * 24 * 365)
    return -1


# DO NOT DELETE THE FOLLOWING LINES OF CODE! YOU MAY
# CHANGE THE FUNCTION CALLS TO TEST YOUR WORK WITH
# DIFFERENT INPUT VALUES.
if __name__ == "__main__":
    test1 = how_long(238900, 0.01, "M") # approximate distance to Moon
    print("how_long(238900, 0.01, 'M') is:", test1)
    print()
    test2 = how_long(45594000, 0.01, "H") # approximate distance to Mars
    print("how_long(45594000, , 0.01, 'H') is:", test2)
    print()
    test3 = how_long(93000000, 1.0, "M") # approximate distance to Sun
    print("how_long(93000000, 1.0, 'M') is:", test3)
    print()
    test4 = how_long(9000000000, 0.01, "D") # approximate distance to edge of Solar System
    print("how_long(9000000000, 0.01, 'D') is:", test4)
    print()
    test5 = how_long(25000000000000, 0.01, "Y") # approximate distance to closest system Alpha Centauri
    print("how_long(25000000000000, 0.01, 'Y') is:", test5)
    print()

