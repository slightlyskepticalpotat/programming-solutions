import sys

input = sys.stdin.readline


def lcs(x, y):
    values = [[None]*(len(y) + 1) for i in range(len(x) + 1)]
    for i in range(len(x) + 1):
        for j in range(len(y) + 1):
            if i == 0 or j == 0: # build the dp array
                values[i][j] = 0
            elif x[i-1] == y[j-1]:
                values[i][j] = values[i-1][j-1]+1
            else:
                values[i][j] = max(values[i-1][j], values[i][j-1])
    return values[-1][-1]

for i in range(5):
    line = input().strip()
    print(lcs(line, line[::-1]))