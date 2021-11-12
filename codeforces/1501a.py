import math, sys

input = sys.stdin.readline

for _ in range(int(input())):
    arr_dep = [[int(i) for i in input().split()] for j in range(int(input()))] + [[0, 0]] # add start
    travel = [int(i) for i in input().split()]
    time = arr_dep[0][0] + travel[0]
    for i in range(len(travel) - 1):
        time = max(time + math.ceil((arr_dep[i][1] - arr_dep[i][0]) / 2), arr_dep[i][1])
        time += arr_dep[i + 1][0] - arr_dep[i][1] + travel[i + 1]
    print(time)
