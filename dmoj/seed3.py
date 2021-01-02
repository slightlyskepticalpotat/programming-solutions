# range update with difference array

import sys

input = sys.stdin.readline

stations, n, j = [0 for _ in range(int(input()) + 1)], int(input()), int(input())
for i in range(j):
    xi, xf, k = map(int, input().split())
    stations[xi - 1] += k
    stations[xf] -= k

original = [stations[0]]
for i in range(1, len(stations) - 1):
    original.append(original[i - 1] + stations[i])
print(sum([station < n for station in original]))