import collections, math, sys

input = sys.stdin.readline

def bfs(start):
    searched, queue = set(start), collections.deque(start)
    for participant in start:
        dist[participant] = 0
    while queue:
        searching = queue.popleft()
        for peer in graph[searching]:
            if peer not in searched:
                searched.add(peer)
                queue.append(peer)
                dist[peer] = min(dist[searching] + 1, dist[peer])

n, m, q, k = map(int, input().split())
participants, answers = [int(i) for i in input().split()], []
dist, graph = {i + 1: float("inf") for i in range(n)}, {i + 1: [] for i in range(n)}
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
bfs(participants)
for i in range(n):
    answers.append(math.ceil((1/2 + math.sqrt(1/4 - 4 * 1/2 * - dist[i + 1] / k))) - 1) # good old quadratic formula
print(*answers)