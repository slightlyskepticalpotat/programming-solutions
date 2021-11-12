import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    total, last = 0, 0
    friends = list(sorted([int(i) for i in input().split()], reverse = True))
    presents = [int(i) for i in input().split()]
    for i in range(n):
        if last <= friends[i] - 1:
            total += min(presents[friends[i] - 1], presents[last])
            last += 1
        else:
            total += presents[friends[i] - 1]
    print(total)
