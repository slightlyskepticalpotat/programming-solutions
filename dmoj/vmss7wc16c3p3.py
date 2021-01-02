import heapq, sys

input = sys.stdin.readline

def heap_dijkstra(graph, start, costs):
    queue, searched = [(0, start)], set() # cost, node
    heapq.heapify(queue)
    while queue:
        searching = heapq.heappop(queue)
        for peer in graph[searching[1]]:
            if peer not in searched:
                updated_cost = searching[0] + graph[searching[1]][peer]
                if updated_cost < costs[peer]:
                    costs[peer] = updated_cost
                    heapq.heappush(queue, (costs[peer], peer))
        searched.add(searching)

n, m, b, q = map(int, input().split())
graph, costs = {i + 1: {} for i in range(n)}, {i + 1: float("inf") for i in range(n)}
costs[b] = 0
for i in range(m):
    x, y, z = map(int, input().split())
    graph[x][y] = z
    graph[y][x] = z
    
heap_dijkstra(graph, b, costs)
for _ in range(q):
    a = int(input())
    if costs[a] == float("inf"):
        print(-1)
    else:
        print(costs[a])