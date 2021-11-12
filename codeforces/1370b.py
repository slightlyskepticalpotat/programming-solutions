import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, vals = int(input()), [int(i) for i in input().split()]
    odds, evens = [[vals[i], i + 1] for i in range(2 * n) if vals[i] % 2], [[vals[i], i + 1] for i in range(2 * n) if not vals[i] % 2] 
    if len(evens) == 0: # leave two
        while len(odds) > 3:
            print(odds.pop()[1], odds.pop()[1])
    else:
        while len(odds) > 1:
            print(odds.pop()[1], odds.pop()[1])

    if len(odds) == 0: # leave two
        while len(evens) > 3:
            print(evens.pop()[1], evens.pop()[1])
    else:
        while len(evens) > 1:
            print(evens.pop()[1], evens.pop()[1])