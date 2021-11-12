import sys

input = sys.stdin.readline

def check(x, y):
    for i in range(min(x[0], y[0]), max(x[0], y[0]) + 1):
        if not plan[i][x[1]] == "B":
            return False
    for i in range(min(x[1], y[1]), max(x[1], y[1]) + 1):
        if not plan[y[0]][i] == "B":
            return False
    return True

n, m = map(int, input().split())
plan = tuple(tuple(i for i in input().strip()) for j in range(n))
start = [(i, j) for i in range(n) for j in range(m) if plan[i][j] == "B"]
for i in range(len(start)):
    for j in range(i + 1, len(start)):
        if not check(start[i], start[j]) and not check(start[j], start[i]):
            print("NO")
            sys.exit()
print("YES")
