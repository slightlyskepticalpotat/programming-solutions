# https://www.geeksforgeeks.org/count-pairs-array-whose-sum-less-x/

import sys
input = sys.stdin.readline

integers, target = map(int, input().split())
numbers = sorted([int(i) for i in input().split()])
count = 0
l = 0
r = integers - 1

while l < r:
    if numbers[l] + numbers[r] <= target: # if x + y < z and a, b < y, x + a, x + b < y
        count += (r - l)
        l += 1
    else:
        r -= 1
print(count % 1000000007)