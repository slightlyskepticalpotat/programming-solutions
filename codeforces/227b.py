import sys

input = sys.stdin.readline

n, values, index = int(input()), [int(i) for i in input().split()], {}
for i in range(n):
    index[values[i]] = i + 1
v, s, q, queries = 0, 0, int(input()), [int(i) for i in input().split()]
for i in range(q):
    v += index[queries[i]]
    s += n - index[queries[i]] + 1
print(v, s)
