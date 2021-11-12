import statistics, sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    graph = [[int(i) for i in input().split()] for j in range(n)]
    dist, ans = [[0 for i in range(m)] for j in range(n)], 0
    for i in range(n):
        for j in range(m):
            dist[i][j] = i + j + 1
    last = dist[n - 1][m - 1]
    freqs = [[] for i in range(last // 2)]
    for i in range(n):
        for j in range(m):
            try:
                freqs[min(i + j, last - (i + j + 1))].append(graph[i][j])
            except: # middle
                pass
    for i in range(last // 2):
        ans += len(freqs[i]) - freqs[i].count(statistics.mode(freqs[i]))
    print(ans)