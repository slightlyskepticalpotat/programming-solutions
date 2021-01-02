import sys

input = sys.stdin.readline

def check(a, b, c):
    try:
        if (a[1] - b[1]) / (a[0] - b[0]) == (a[1] - c[1]) / (a[0] - c[0]):
            return True
    except:
        if a[0] == b[0] == c[0] or a[1] == b[1] == c[1]:
            return True
    return False

n, pairs, triplets = int(input()), [], 0
grid = [[char for char in input()] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if grid[i][j].isalpha():
            pairs.append((i, j))

for i in range(len(pairs)):
    for j in range(i + 1, len(pairs)):
        for k in range(j + 1, len(pairs)):
            if check(pairs[i], pairs[j], pairs[k]):
                triplets += 1
print(triplets)