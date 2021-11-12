# need iterative dfs

import collections, sys, threading

input = sys.stdin.readline

def kosaraju(graph, visited, queue, n, cc, components, graph2):
    for node in graph:
        if not visited[node]:
            visit(graph, node, visited, queue)
    visited = [False for i in range(n)]
    queue = list(queue)[::-1]
    for peer in queue:
        if not visited[peer]:
            back_visit(graph, peer, visited, cc, components, graph2)
            cc += 1

def back_visit(graph, node, visited, cc, components, graph2):
    if not cc in components:
        components[cc] = [node]
    else:
        components[cc].append(node)
    visited[node] = True
    for peer in graph2[node]:
        if not visited[peer]:
            back_visit(graph, peer, visited, cc, components, graph2)

def visit(graph, node, visited, queue):
    visited[node] = True
    for peer in graph[node]:
        if not visited[peer]:
            visit(graph, peer, visited, queue)
    queue.append(node)

def main():
    n, costs, final_cost, cnt = int(input()), tuple(int(i) for i in input().split()), 0, 1
    visited, graph, graph2, queue, cc, components = [False for i in range(n)], {i: [] for i in range(n)}, {i: [] for i in range(n)}, collections.deque(), 0, {}
    for i in range(int(input())):
        u, v = map(int, input().split())
        u, v = u - 1, v - 1
        graph[u].append(v)
        graph2[v].append(u)
    kosaraju(graph, visited, queue, n, cc, components, graph2)
    for component in components:
        check = [costs[node] for node in components[component]]
        k = min(check)
        final_cost += k
        cnt = (cnt * check.count(k)) % 1000000007
    print(final_cost, cnt)

sys.setrecursionlimit(3 * 10 ** 5)
threading.stack_size(3 * 500 * 10 ** 5 )
thread = threading.Thread(target=main)
thread.start()
