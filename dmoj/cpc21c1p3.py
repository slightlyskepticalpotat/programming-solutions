import sys

input = sys.stdin.readline

for _ in range(int(input())):
    r1, r2, r3 = map(int, input().split()) # math.pi omitted
    total, focus = (r2 - r3) ** 2, 0
    if r2 - r1 >= 2 * r3: # between c1 and c2
        focus += (r2 - r3) ** 2
        focus -= (r1 + r3) ** 2
    if r1 >= r3: # in c1
        focus += (r1 - r3) ** 2
    else: # outside c1
        focus += min(r3 - r1, r2 - r3) ** 2
    print(focus / total)