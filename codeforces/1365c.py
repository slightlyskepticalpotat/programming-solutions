import statistics, sys

input = sys.stdin.readline

n, a, b = int(input()), [int(i) for i in input().split()], [int(i) for i in input().split()]
pos_a = [0 for _ in range(n + 1)]
for i in range(n):
    pos_a[a[i]] = i
diffs = [(i - pos_a[b[i]]) % n for i in range(n)]
print(diffs.count(statistics.mode(diffs)))