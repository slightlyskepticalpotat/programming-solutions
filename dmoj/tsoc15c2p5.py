import functools, sys

input = sys.stdin.readline

def compare(x, y): # speed, distance, sharpness, id
    if x[0] == y[0]: # speed is the same
        if x[0] >= s: # faster than runners
            if x[2] == y[2]: # tie
                if x[3] > y[3]:  # larger id
                    return 1
                else:
                    return -1
            else: # no tie
                if x[2] < y[2]: # sharper claw
                    return 1
                else:
                    return -1
        else:
            if x[1] == y[1]: # tie
                if x[3] > y[3]: # larger id
                    return 1
                else:
                    return -1
            else: # no tie
                if x[1] < y[1]: # stronger venom
                    return 1
                return -1
    else: # different speeds
        if x[0] < y[0]: # larger speed
            return 1
        else:
            return -1

s = int(input())
bebiliths = [[int(i) for i in input().split()] + [j + 1] for j in range(int(input()))]
bebiliths.sort(key = functools.cmp_to_key(compare))
for i in range(int(input())):
    print(bebiliths[int(input()) - 1][3])