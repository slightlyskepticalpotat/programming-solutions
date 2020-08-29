# python rounding always rounds to even digits for some reason

import sys, math
input = sys.stdin.readline

def round(x):
    if x - math.floor(x) < 0.5:
        return math.floor(x)
    return math.ceil(x)

numbers = []
for i in range(int(input())):
    numbers.append(int(input()))

numbers.sort()
if len(numbers) % 2 == 1:
    print(numbers[len(numbers) // 2])
else:
    print(round((numbers[len(numbers) // 2 - 1] + numbers[len(numbers) // 2]) / 2))