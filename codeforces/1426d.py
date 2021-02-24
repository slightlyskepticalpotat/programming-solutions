n, values, seen, tot, ans = int(input()), [int(i) for i in input().split()], set([0]), 0, 0
for i in range(n):
    tot += values[i]
    if tot in seen: # psa[a] - psa[b] = 0, reset psa
        ans, seen, tot = ans + 1, set([0]), values[i]
    seen.add(tot)
print(ans)
