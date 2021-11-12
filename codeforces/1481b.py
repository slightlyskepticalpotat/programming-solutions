import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    mountains, best = [int(i) for i in input().split()], -1
    for i in range(k):
        flag = False
        for j in range(n - 1):
            if mountains[j] < mountains[j + 1]:
                mountains[j], flag, best = mountains[j] + 1, True, j + 1 # it rolled somewhere good
                break
        if not flag:
            best = -1
            break
    print(best)
