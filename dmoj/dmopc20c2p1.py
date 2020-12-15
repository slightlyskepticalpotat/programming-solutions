import sys

input = sys.stdin.readline

graph = [["." for i in range(2003)] for j in range(2003)]
n, instructions = int(input()), [char for char in input().strip()]
x, y = 0, 1001 # 0 1000 top left corner

for i in range(n):
    if instructions[i] == "^":
        graph[y][x] = "/"
        x += 1
        y -= 1
    elif instructions[i] == "v":
        y += 1
        graph[y][x] = "\\"
        x += 1
    elif instructions[i] == ">":
        graph[y][x] = "_"
        x += 1
for row in graph:
    if len([char for char in row if char != "."]):
        print("".join(row[:n]))