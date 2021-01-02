import heapq, sys

input = sys.stdin.readline

def heap_dijkstra(graph, start):
    queue = [(0, start)] # cost, node
    heapq.heapify(queue)
    while queue:
        searching = heapq.heappop(queue)
        for peer, cost in enumerate(adj_graph[searching[1]]):
            if cost: # we haven't visited it before
                new_cost = searching[0] + cost
                if new_cost < costs[peer]:
                    costs[peer] = new_cost
                    heapq.heappush(queue, (new_cost, peer))

n, t = int(input()), int(input())
adj_graph, costs = [[0 for i in range(n + 1)] for j in range(n + 1)], {i + 1: float("inf") for i in range(n)}
costs[1] = 0
for i in range(t):
    u, v, w = map(int, input().split())
    adj_graph[u][v] = w
    adj_graph[v][u] = w
k, pencils = int(input()), {}
for i in range(k):
    z, p = map(int, input().split())
    pencils[z] = p
d = int(input())
heap_dijkstra(adj_graph, d)

best_price = float("inf")
for city in pencils:
    best_price = min(best_price, costs[city] + pencils[city])
print(best_price)