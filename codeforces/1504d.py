import sys

input = sys.stdin.readline

n, black, white = int(input()), [], []
for i in range(n):
    for j in range(n):
        if (i + j) % 2:
            black.append([i + 1, j + 1])
        else:
            white.append([i + 1, j + 1])
for i in range(n ** 2): # 1 on white 2 on black
    a = int(input())
    if a == 1:
        if len(black):
            new = black.pop()
            print(2, *new)
        else:
            new = white.pop()
            print(3, *new)
    elif a == 2:
        if len(white):
            new = white.pop()
            print(1, *new)
        else:
            new = black.pop()
            print(3, *new)
    elif a == 3:
        if len(white):
            new = white.pop()
            print(1, *new)
        else:
            new = black.pop()
            print(2, *new)
    sys.stdout.flush()
