import sys

input = sys.stdin.readline

k, d = map(int, input().split())
vals = sorted([int(i) for i in input().split()])
if vals == [0]:
    print(-1)
else:
    if 0 in vals:
        if k == 1:
            print(str(vals[1]))
        elif k == 2:
            print(str(vals[1]) * 2)
        else:
            print(str(vals[1]) + "0" * (k - 2) + str(vals[1]))
    else:
        print(str(vals[0]) * k)