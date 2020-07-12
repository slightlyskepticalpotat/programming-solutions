import itertools

numbers = int(input())
integers = sorted([int(i) for i in input().split()])
print(*integers) # oof