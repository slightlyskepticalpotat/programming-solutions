import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, values, ans = int(input()), [int(i) for i in input().split()], float("inf")
    mins, left, total = [float("inf"), float("inf")], [n, n], 0
    for i in range(n): # iterate over number of turns
        mins[i % 2] = min(mins[i % 2], values[i])
        left[i % 2] -= 1
        total += values[i]
        if i != 0:
            ans = min(ans, total + mins[0] * left[0] + mins[1] * left[1]) # maximise length of cheapest segment
    print(ans)
