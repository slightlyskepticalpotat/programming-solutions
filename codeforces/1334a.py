import sys

input = sys.stdin.readline

for _ in range(int(input())):
    data, ans = [[int(i) for i in input().split()] for j in range(int(input()))], True
    for i in range(len(data)):
        if data[i][0] < data[i][1]:
            ans = False
        if i > 0:
            if data[i][0] < data[i - 1][0] or data[i][1] < data[i - 1][1]:
                ans = False
            if data[i][0] - data[i - 1][0] < data[i][1] - data[i - 1][1]:
                ans = False
    if ans:
        print("YES")
    else:
        print("NO")