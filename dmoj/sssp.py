import sys

input = sys.stdin.readline

def dijkstra(graph, start):
    costs[1] = 0
    previous, node = {i: None for i in graph}, minimum(costs)
    while node != None:
        cost, peers = costs[node], graph[node]
        for peer in peers:
            updated_cost = cost + peers[peer]
            if updated_cost < costs[peer]:
                costs[peer], previous[peer] = updated_cost, node
        searched.append(node)
        node = minimum(costs)
    return 0

def minimum(graph):
    cheapest_cost, cheapest_node = float("inf"), None
    for node in costs:
        cost = costs[node]
        if cost < cheapest_cost and node not in searched:
            cheapest_cost, cheapest_node = cost, node
    return cheapest_node

n, m = map(int, input().split())
graph = {i + 1: {} for i in range(n)}
for i in range(m):
    u, v, w = map(int, input().split())
    try: # parallel edges
        graph[u][v] = min(graph[u][v], w)
    except:
        graph[u][v] = w
    try:
        graph[v][u] = min(graph[v][u], w)
    except:
        graph[v][u] = w

costs, searched = {i: float("inf") for i in graph}, []
dijkstra(graph, 1)
for thing in costs:
    if costs[thing] == float("inf"):
        print(-1)
    else:
        print(costs[thing])