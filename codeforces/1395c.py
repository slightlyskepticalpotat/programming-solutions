import sys

input = sys.stdin.readline

n, m = map(int, input().split())
n_vals, m_vals = [int(i) for i in input().split()], [int(i) for i in input().split()]

for i in range(512): # c
    for j in range(n):
        if not any(i & (n_vals[j] & m_vals[k]) == n_vals[j] & m_vals[k] for k in range(m)): # check if & "fits" inside c
            break
        if j == n - 1:
            print(i)
            raise SystemExit
