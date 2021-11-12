n, k = map(int, input().split())
fence = [int(i) for i in input().split()]
psa = [fence[0]]
for i in range(n):
    psa.append(psa[i] + fence[i])

best, best_index = float("inf"), -1
for i in range(k, n + 1):
    if psa[i] - psa[i - k] < best:
        best = psa[i] - psa[i - k]
        best_index = i
print(best_index - k + 1)
