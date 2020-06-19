grid = [[1, 2], [3, 4]]
instructions = [char for char in input().strip()]
for thing in instructions:
    if thing == "H":
        grid.reverse()
    if thing == "V":
        grid[0].reverse()
        grid[1].reverse()

print(grid[0][0], end = " ")
print(grid[0][1])
print(grid[1][0], end = " ")
print(grid[1][1])