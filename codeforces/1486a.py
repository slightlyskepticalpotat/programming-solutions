import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, flag = int(input()), True
    stacks = [int(i) for i in input().split()]
    psa = [0]
    for i in range(n):
        psa.append(psa[i] + stacks[i])
    psa.remove(0)
    for i in range(n):
        if psa[i] < i * (i + 1) / 2:
            flag = False
    if flag:
        print("YES")
    else:
        print("NO")
