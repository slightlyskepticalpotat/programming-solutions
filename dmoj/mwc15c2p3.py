import sys

input = sys.stdin.readline

n, x, y, visited = int(input()), 0, 0, [(0, 0)]
steps = [i for i in input().strip().split()]

for i in range(len(steps)):
    if steps[i] == "U":
        y += 1
    elif steps[i] == "R":
        x += 1
    elif steps[i] == "D":
        y -= 1
    else:
        x -= 1
    if (x, y) in visited:
        print(f"Fell at {i + 1}")
        raise SystemExit
    else:
        visited.append((x, y))
print("Safe!")