import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, vals, psa, ans = int(input()), [int(i) - 1 for i in input().split()], [[0] for j in range(26)], [1]
    for i in range(26):
        for j in range(n):
            psa[i].append(psa[i][-1] + int(vals[j] == i))
    for i in range(n):
        for j in range(i, n):
            outer, inner = 0, 0
            for k in range(26):
                outer, inner = max(outer, min(psa[k][i], psa[k][-1] - psa[k][j])), max(inner, psa[k][j] - psa[k][i])
            ans.append(outer * 2 + inner)
    print(max(ans))