import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
best_id, best_score = [-1 for _ in range(n)], [-1 for _ in range(n)]
for i in range(k):
    a, b, c = map(int, input().split())
    if c > best_score[b - 1]:
        best_score[b - 1] = c
        best_id[b - 1] = a
print(*best_id)
