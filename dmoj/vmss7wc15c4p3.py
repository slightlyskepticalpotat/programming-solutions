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
        
n, m = map(int, input().split())
graph, costs = {i: {} for i in range(n)}, {i: float("inf") for i in range(n)}
costs[0] = 0
for i in range(m):
    a, b, t = map(int, input().split())
    graph[a][b] = t
    graph[b][a] = t
heap_dijkstra(graph, 0, costs)

costs_2 = {i: float("inf") for i in range(n)}
costs_2[n - 1] = 0
heap_dijkstra(graph, n - 1, costs_2)
print(max([costs[i] + costs_2[i] for i in range(n)]))