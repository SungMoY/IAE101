# Sung Mo Yang
# 112801117
# sungyang
#
# IAE 101 (Fall 2022)
# HW 2, Problem 3

def reverse1(s):
    #reverse string s using a for loop
    returnString = ""
    for char in s:
        returnString = char + returnString
    return returnString

def reverse2(s):
    #reverse string using splice
    return s[::-1]


# DO NOT DELETE THE FOLLOWING LINES OF CODE! YOU MAY
# CHANGE THE FUNCTION CALLS TO TEST YOUR WORK WITH
# DIFFERENT INPUT VALUES.
if __name__ == "__main__":
    print("reverse1(\"Mississippi\") is:", reverse1("Mississippi"))
    print()
    print("reverse2(\"Mississippi\") is:", reverse2("Mississippi"))
    print()
    print("reverse1(\"Connetquot\") is:", reverse1("Connetquot"))
    print()
    print("reverse2(\"Connetquot\") is:", reverse2("Connetquot"))
    print()
    print("reverse1(\"Wyandanch\") is:", reverse1("Wyandanch"))
    print()
    print("reverse2(\"Wyandanch\") is:", reverse2("Wyandanch"))
    print()
    print("reverse1(\"Ronkonkoma\") is:", reverse1("Ronkonkoma"))
    print()
    print("reverse2(\"Ronkonkoma\") is:", reverse2("Ronkonkoma"))
    print()
