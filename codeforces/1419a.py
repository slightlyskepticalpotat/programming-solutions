import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, integer, raze, breach = int(input()), [int(i) for i in input().strip()], False, False
    if n % 2:
        for i in range(0, len(integer), 2):
            if integer[i] % 2:
                raze = True
        if not raze:
            breach = True
    else:
        for i in range(1, len(integer), 2):
            if not integer[i] % 2:
                breach = True
        if not breach:
            raze = True
    if raze:
        print(1)
    else:
        print(2)
