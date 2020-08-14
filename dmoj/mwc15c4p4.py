import sys
input = sys.stdin.readline

connections, graph = int(input()), {}

for i in range(1, connections + 1):
    graph[i] = []
    
for _ in range(connections):
    x, y = input().split()
    x, y = int(x), int(y)
    graph[x].append(y)

def find_path(start_node, end_node, path=None):
    if path == None:
        path = []
    path = path + [start_node]
    if start_node == end_node:
        return True
    for vertex in graph[start_node]:
        if vertex not in path:
            extended_path = find_path(vertex, end_node, path)
            if extended_path:
                return extended_path
    return False

start, stop = input().split()
start, stop = int(start), int(stop)

if find_path(start, stop):
    print("Tangled")
else:
    print("Not Tangled")