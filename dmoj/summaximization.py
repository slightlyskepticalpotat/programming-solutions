# https://www.geeksforgeeks.org/biggest-integer-maximum-digit-sum-range-1-n

import sys
input = sys.stdin.readline

def digit_sum(x): # sum of digits of a number
    digit = 0
    while x != 0:
        digit += x % 10
        x //= 10
    return digit

def max_sum(x, y): # y > x
    potential = [] # potential greatest numbers
    digit = 1
    while y != 0: # iterate through the digits, runtime O(digits)
        current = (y - 1) * digit + (digit - 1) # reduce by 1, rest is 9s
        potential.append([current, digit_sum(current)]) # add everything [number, sum]
        y //= 10 # decrement number and digit
        digit *= 10
    potential = [char for char in potential if char[0] >= x] # must be within x, y range
    potential = sorted(potential, key = lambda x: x[1], reverse=True) # highest number out of potentials
    return potential[0][1]

for i in range(int(input())):
    a, b = sorted(map(int, input().split()))
    print(max_sum(a, b)) # have to be in ascending order for some reason