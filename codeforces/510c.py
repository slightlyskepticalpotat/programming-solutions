import sys

input = sys.stdin.readline

def toposort(graph):
    searched, stack = set(), []
    for node in graph:
        if node not in searched:
            toposort_recurse(graph, node, searched, stack)
    return stack[::-1]

def toposort_recurse(graph, node, searched, stack):
    searched.add(node)
    for peer in graph[node]:
        if peer not in searched:
            toposort_recurse(graph, peer, searched, stack)
    stack.append(node)

def toposort_check(graph, path):
    for node in graph:
        for peer in graph[node]:
            if path.index(peer) < path.index(node):
                return False
    return True

graph, n, prev, curr = {char: [] for char in "abcdefghijklmnopqrstuvwxyz"}, int(input()), input().strip(), ""
for i in range(n - 1):
    old_curr = curr = input().strip()
    while len(prev) > 0 and len(curr) > 0 and curr[0] == prev[0]:
        curr, prev = curr[1:], prev[1:]
    if curr and prev:
        graph[prev[0]].append(curr[0])
    elif prev and not curr:
        print("Impossible")
        sys.exit(0)
    prev = old_curr

path = toposort(graph)
if toposort_check(graph, path):
    print("".join(path))
else:
    print("Impossible")
