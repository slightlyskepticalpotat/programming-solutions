import sys

input = sys.stdin.readline

n, m = map(int, input().split())
x, best, best_i, ans, zero = input().strip(), 0, 0, "", 0
a = [int(i) for i in input().split()]
for i in range(m):
    if a[i] >= best:
        best = a[i]
        best_i = i
for i in range(n):
    if x[i] == "0":
        if zero == best_i:
            ans = x[i + 1:] + x[:i]
            break
        else:
            zero += 1
print(ans.replace("0", ""))