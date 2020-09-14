import math, sys

input = sys.stdin.readline

n = input().strip() # converting big strings to ints is slow
if n in ["1", "2", "6", "24", "120"]: # smaller values need adjusting
    print(["1", "2", "6", "24", "120"].index(n) + 1)
    raise SystemExit

length, result, i = len(n), 0, 0

while i < length: # get n from the number of digits in n!
    result += 1
    i += math.log10(result)
print(result - 1)