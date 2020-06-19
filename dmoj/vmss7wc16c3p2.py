import sys
input = sys.stdin.readline
houses, roads, shahir, date = input().strip().split()
houses, roads, shahir, date = int(houses), int(roads), int(shahir), int(date)
graph = {}

for i in range(1, houses+1):
    graph[i] = []

for i in range(0, roads):
    start, end = input().strip().split()
    start, end = int(start), int(end)
    graph[start].append(end)
    graph[end].append(start)

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

if find_path(shahir, date) == True:
    print("GO SHAHIR!")
else:
    print("NO SHAHIR!")