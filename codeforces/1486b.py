import sys

input = sys.stdin.readline

def find_middle(x):
    if len(x) % 2:
        return 1
    return abs(x[len(x) // 2 - 1] - x[len(x) // 2]) + 1

for _ in range(int(input())):
    n = int(input())
    houses = [[int(i) for i in input().split()] for j in range(n)]
    x, y = [houses[i][0] for i in range(n)], [houses[i][1] for i in range(n)]
    x.sort()
    y.sort()
    print(find_middle(x) * find_middle(y))
