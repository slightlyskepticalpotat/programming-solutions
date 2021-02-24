import sys

input = sys.stdin.readline

n, m = map(int, input().split())
colours, best, best_car = [int(i) for i in input().split()], float("inf"), 0
colours_set = set(colours)
colours_graph = {colour: set() for colour in colours_set}
for i in range(m):
    a, b = map(int, input().split())
    if colours[a - 1] in colours_set and colours[b - 1] in colours_set and colours[a - 1] != colours[b - 1]:
        colours_graph[colours[a - 1]].add(colours[b - 1])
        colours_graph[colours[b - 1]].add(colours[a - 1])
for colour in colours_graph:
    if len(colours_graph[colour]) > best_car or len(colours_graph[colour]) == best_car and colour < best:
        best = colour
        best_car = len(colours_graph[colour])
print(best)
