# Sung Mo Yang
# 112801117
# sungyang
#
# IAE 101 (Fall 2022)
# HW 2, Problem 4

# DO NOT CHANGE OR REMOVE THIS
from time import time


gravity = -9.8 # downward acceleration due to gravity is -9.8 meters per second^2

# v is the initial horizontal velocity of the ball in meters per second
# h is the initial height of the ball in meters
def how_far(v, h):
    timeInSeconds = 0
    currentDistance = h

    while (currentDistance > 0):
        timeInSeconds+=1
        currentDistance = h  + (0.5 * gravity * timeInSeconds**2)

    return v *timeInSeconds


# DO NOT DELETE THE FOLLOWING LINES OF CODE! YOU MAY
# CHANGE THE FUNCTION CALLS TO TEST YOUR WORK WITH
# DIFFERENT INPUT VALUES.
if __name__ == "__main__":
    test1 = how_far(10.0, 100.0)
    print("how_far(10.0, 100.0) is:", test1)
    print()
    test2 = how_far(45.0, 2.0)
    print("how_far(45.0, 2.0) is:", test2)
    print()
    test3 = how_far(20.0, 100.0)
    print("how_far(20.0, 100.0) is:", test3)
    print()
    test4 = how_far(30.0, 100.0)
    print("how_far(30.0, 100.0) is:", test4)
    print()
    test5 = how_far(20.0, 10000.0)
    print("how_far(20.0, 10000.0) is:", test5)
    print()
