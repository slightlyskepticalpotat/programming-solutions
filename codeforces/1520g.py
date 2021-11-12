import collections, sys

input = sys.stdin.readline

def bfs_mod(start):
    queue, dist[start], best = collections.deque([start]), 0, float("inf")
    while queue:
        searching = queue.popleft()
        if graph[searching[0]][searching[1]] > 0 and graph[searching[0]][searching[1]] + dist[searching] < best:
            best = graph[searching[0]][searching[1]] + dist[searching]
        for peer in ((searching[0] + 1, searching[1]), (searching[0] - 1, searching[1]), (searching[0], searching[1] + 1), (searching[0], searching[1] - 1)):
            if 0 <= peer[0] < n and 0 <= peer[1] < m and not peer in dist and graph[peer[0]][peer[1]] != -1:
                queue.append(peer)
                dist[peer] = dist[searching] + w
    return best

n, m, w = map(int, input().split())
graph, dist, ans = tuple(tuple(int(i) for i in input().split()) for j in range(n)), {}, float("inf")
best_start = bfs_mod((0, 0))
ans = min(ans, dist.get((n - 1, m - 1), float("inf")))
dist = {}
best_end = bfs_mod((n - 1, m - 1))
ans = min(ans, best_start + best_end)
if ans < float("inf"):
    print(ans)
else:
    print(-1)
