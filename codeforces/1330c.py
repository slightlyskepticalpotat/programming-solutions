import sys

input = sys.stdin.readline

n, m = map(int, input().split())
vals, impossible, ssa = [int(i) for i in input().split()], False, [0 for i in range(m + 2)]
impossible |= sum(vals) < n # not enough ops
for i in range(m):
    impossible |= n < vals[i] + i # too many ops
for i in range(m, 0, -1):
    ssa[i] = ssa[i + 1] + vals[i - 1]
ans_ops = [max(i + 1, n - ssa[i + 1] + 1) for i in range(m)]
if impossible:
    print(-1)
else:
    print(*ans_ops)