# Sung Mo Yang
# 112801117
# sungyang
#
# IAE 101 (Fall 2022)
# HW 1, Problem 2

def tip_amount(bill, good_service):
    # ADD YOUR CODE HERE
    if bill < 25.00:
        return 6.0
    else:
        if good_service:
            return bill * .27
        else:
            return bill * .13


# DO NOT DELETE THE FOLLOWING LINES OF CODE! YOU MAY
# CHANGE THE FUNCTION CALLS TO TEST YOUR WORK WITH
# DIFFERENT INPUT VALUES.
if __name__ == "__main__":
    print("tip_amount(23.37,True) is", tip_amount(23.37, True))
    print()
    print("tip_amount(23.37,False) is", tip_amount(23.37, False))
    print()
    print("tip_amount(81.75,True) is", tip_amount(81.75, True))
    print()
    print("tip_amount(63.59,True) is", tip_amount(63.59, True))
    print()
    print("tip_amount(63.59,False) is", tip_amount(63.59, False))
    print()
