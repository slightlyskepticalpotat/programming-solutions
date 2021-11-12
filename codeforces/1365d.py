import collections, copy, sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    maze, ans = [[i for i in input().strip()] for j in range(n)], "Yes"
    for i in range(n): # blocks around bad people
        for j in range(m):
            if maze[i][j] == "B":
                for d in [-1, 1]:
                    if 0 <= i + d < n and 0 <= j < m:
                        if maze[i + d][j] == ".":
                            maze[i + d][j] = "#"
                    if 0 <= i < n and 0 <= j + d < m:
                        if maze[i][j + d] == ".":
                            maze[i][j + d] = "#"
    queue, searched = collections.deque([(n - 1, m - 1)]), set([(n - 1, m - 1)])
    old_maze = copy.deepcopy(maze)

    if maze[n - 1][m - 1] != "#":
        while queue: # bfs
            searching = queue.popleft()
            maze[searching[0]][searching[1]] = "S"
            for d in [-1, 1]:
                if 0 <= searching[0] + d < n and 0 <= searching[1] < m:
                    if maze[searching[0] + d][searching[1]] != "#" and (searching[0] + d, searching[1]) not in searched:
                            queue.append((searching[0] + d, searching[1]))
                            searched.add((searching[0] + d, searching[1]))
                if 0 <= searching[0] < n and 0 <= searching[1] + d < m:
                    if maze[searching[0]][searching[1] + d] != "#" and (searching[0], searching[1] + d) not in searched:
                        queue.append((searching[0], searching[1] + d))
                        searched.add((searching[0], searching[1] + d))
    for i in range(n):
        for j in range(m):
            if (old_maze[i][j] == "G" and maze[i][j] != "S") or (old_maze[i][j] == "B" and maze[i][j] == "S"):
                ans = "No"
    print(ans)