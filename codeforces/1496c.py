import math, sys

input = sys.stdin.readline

def dist(x, y):
    return math.sqrt(abs(x[0] - y[0]) ** 2 + abs(x[1] - y[1]) ** 2)

for _ in range(int(input())):
    n, miners, mines = int(input()), [], []
    for _ in range(2 * n): # intersections can be fixed
        x, y = map(int, input().split())
        if not x:
            miners.append([0, abs(y)])
        elif not y:
            mines.append([abs(x), 0])
    miners.sort(key = lambda x: x[1], reverse = True)
    mines.sort(key = lambda x: x[0], reverse = True)
    print(sum([dist(miners.pop(), mines.pop()) for _ in range(n)]))
