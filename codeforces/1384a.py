import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, vals = int(input()), [int(i) for i in input().split()]
    ans = [["a" for i in range(max(vals) + 1)] for j in range(n + 1)]
    for i in range(n):
        if ans[i][vals[i]] == "a":
            new = "b"
        else:
            new = "a"
        ans[i + 1] = ans[i][:vals[i]] + [new] + ans[i][vals[i] + 1:]
    print("\n".join(["".join(row) for row in ans]))
