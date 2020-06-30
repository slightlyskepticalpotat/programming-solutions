# https://stackoverflow.com/questions/39588554/minimum-number-of-steps-to-reduce-number-to-1
# https://wiki.python.org/moin/BitwiseOperators

import sys, math
input = sys.stdin.readline

for i in range(int(input())):
    number = int(input())
    tries = 0
    while number:
        if number & 1:
            if number & 2 and number ^ 3:
                number+=1
            else:
                number-=1
        else:
            number = number >> 1
        tries+=1
    print(tries)