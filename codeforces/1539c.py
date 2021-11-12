import sys

input = sys.stdin.buffer.readline # buffer sometimes faster

n, k, x = map(int, input().split())
vals, ans = sorted([int(i) for i in input().split()]), 1
diffs = sorted([vals[i] - vals[i - 1] for i in range(1, n)])
for diff in diffs:
    if diff > x:
        p = (diff - 1) // x
        if k >= p:
            k -= p
        else:
            ans += 1
print(ans)
