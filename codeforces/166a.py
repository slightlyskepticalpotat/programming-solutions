n, k = map(int, input().split())
teams, freqs = [tuple(int(i) for i in input().split()) for _ in range(n)], {}
teams.sort(key = lambda x: (-x[0], x[1]))
for team in teams:
    freqs[team] = freqs.get(team, 0) + 1
print(freqs[teams[k - 1]])
