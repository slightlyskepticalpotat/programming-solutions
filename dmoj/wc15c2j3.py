import math, sys

input = sys.stdin.readline

def dist(x1, y1, x2, y2):
    return math.sqrt(abs(x2-x1)**2 + abs(y2-y1)**2)

s, e, r = map(int, input().split())
stormtroopers = [[int(i) for i in input().split()] for j in range(s)]
ewoks = [[int(i) for i in input().split()] for j in range(e)]
in_danger = 0

for ewok in ewoks:
    in_range = set()
    for stormtrooper in stormtroopers:
        if dist(ewok[0], ewok[1], stormtrooper[1], stormtrooper[2]) <= r:
            in_range.add(stormtrooper[0])
    if len(in_range) >= 2:
        in_danger += 1
print(in_danger)