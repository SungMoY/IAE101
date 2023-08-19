# Sung Mo Yang
# 112801117
# sungyang
#
# IAE 101 (Fall 2022)
# HW 2, Problem 1

def divisible(n):
    divisibleArray = [1,2,3,4,5,6,7,8,9]
    for num in divisibleArray:
        if (n % num == 0):
            divisibleArray[num-1] = True
        else:
            divisibleArray[num-1] = False
    return divisibleArray


# DO NOT DELETE THE FOLLOWING LINES OF CODE! YOU MAY
# CHANGE THE FUNCTION CALLS TO TEST YOUR WORK WITH
# DIFFERENT INPUT VALUES.
if __name__ == "__main__":
    test1 = divisible(126)
    print("divisible(126) is:", test1)
    print()
    test2 = divisible(20)
    print("divisible(20) is:", test2)
    print()
    test3 = divisible(1024)
    print("divisible(1024) is:", test3)
    print()
    test4 = divisible(17)
    print("divisible(17) is:", test4)
    print()
    test5 = divisible(539)
    print("divisible(539) is:", test5)
    print()