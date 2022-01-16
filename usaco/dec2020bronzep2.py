import statistics

n, ans = int(input()), 0
petals = [int(i) for i in input().split()]
for i in range(n):
    for j in range(i + 1, n + 1):
        if statistics.mean(petals[i:j]) in petals[i:j]:
            ans += 1
print(ans)
