import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    heights, flag = [int(i) for i in input().split()], True
    for i in range(n):
        if i == 0:
            minh = heights[0]
            maxh = heights[0]
        elif i == (n - 1):
            if heights[-1] + (k - 1) < minh:
                flag = False
            if heights[-1] > maxh + (k - 1):
                flag = False
        else:
            minh = max(minh - (k - 1), heights[i])
            maxh = min(maxh + (k - 1), heights[i] + (k - 1))
            if minh > maxh:
                flag = False
                break
    if flag:
        print("yes")
    else:
        print("no")
