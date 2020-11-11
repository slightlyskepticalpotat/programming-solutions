import sys

input = sys.stdin.readline

def dijkstra(graph, start):
    costs[0] = 0
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

t, n, m, g = map(int, input().split())
food_basics, graph = [int(input()) for i in range(g)], {i: {} for i in range(n + 1)}
for i in range(m):
    a, b, l = map(int, input().split())
    graph[a][b] = l

costs, searched, possible = {i: float("inf") for i in graph}, [], 0
dijkstra(graph, 0)
for node in costs:
    if node and costs[node] < t and node in food_basics:
        possible += 1
print(possible)