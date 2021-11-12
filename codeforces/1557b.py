import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    vals, order = [int(i) for i in input().split()], {}
    sorted_vals, arrays = sorted(vals), 1
    order = {sorted_vals[i - 1]: sorted_vals[i] for i in range(1, n)}
    for i in range(1, n): # check if we match the sorted order
        arrays += int(order.get(vals[i - 1], float("inf")) != vals[i])
    if arrays <= k:
        print("Yes")
    else:
        print("No")