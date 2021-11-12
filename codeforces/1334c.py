import sys

input = sys.stdin.buffer.readline

for _ in range(int(input())):
    n, best, best_i = int(input()), float("inf"), -1
    vals = [[int(i) for i in input().split()] for j in range(n)]
    vals.append(vals[0])
    for i in range(n):
        if vals[i + 1][0] - max(0, vals[i + 1][0] - vals[i][1]) < best:
            best = vals[i + 1][0] - max(0, vals[i + 1][0] - vals[i][1])
            best_i = i + 1
    new_vals, ans = [vals[(best_i + i) % n] for i in range(n)], 0
    for i in range(n - 1):
        ans += max(new_vals[i][0], 0)
        new_vals[i + 1][0] -= new_vals[i][1]
    ans += max(new_vals[-1][0], 0)
    print(ans)