import heapq, sys

input = sys.stdin.readline

def heap_dijkstra(graph, start, end, costs):
    queue, searched = [(0, start, 0)], set() # cost, node, hull
    heapq.heapify(queue)
    while queue:
        searching = heapq.heappop(queue)
        if searching[1:] in searched: # keep track of weight and node
            continue
        searched.add(searching[1:])
        for peer in graph[searching[1]]:
            updated_cost = searching[0] + graph[searching[1]][peer][0]
            updated_hull = searching[2] + graph[searching[1]][peer][1]
            if updated_hull < k and updated_cost < costs[peer][updated_hull]:
                costs[peer][updated_hull] = updated_cost
                heapq.heappush(queue, (updated_cost, peer, updated_hull))
        if searching[1] == end:
            return searching[0]
    return -1

k, n, m = map(int, input().split())
nonce = n + 1
graph, costs = {i + 1: {} for i in range(n + m // 2 + 1)}, [[float("inf") for i in range(201)] for j in range(n + m // 2 + 1)]
for i in range(m):
    ai, bi, ti, hi = map(int, input().split()) # start, stop, cost, hull
    try: # if edge already exists, add another node
        check = graph[ai][bi]
        graph[ai][nonce] = (ti, hi)
        graph[nonce][ai] = (ti, hi)
        graph[nonce][bi] = (0, 0)
        graph[bi][nonce] = (0, 0)
        nonce += 1
    except: # no previous edge
        graph[ai][bi] = (ti, hi)
        graph[bi][ai] = (ti, hi)
        
a, b = map(int, input().split())
costs[a][0] = 0
cost = heap_dijkstra(graph, a, b, costs)
print(cost)