import math

n = int(input())
m = math.floor((1 + math.sqrt(1 + 8 * n)) / 2) # mth row from the top
low, high = ((m - 1) * m) / 2 + 1, ((m + 1) * m) / 2 # range of numbers to add
if n == 1: # special case
    print(n)
else:
    print(int((high - low + 1) * (high + low) / 2))