import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, x = map(int, input().split())
    vals = [int(i) for i in input().split()]
    for i in range(1, 1024):
        if i not in vals:
            if x > 0:
                x -= 1
            else:
                print(i - 1)
                break