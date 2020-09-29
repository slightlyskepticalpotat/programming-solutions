import collections, itertools, sys

input = sys.stdin.readline

def slope(x1, y1, x2, y2):
    if x1 == x2:
        return 256
    return (y2 - y1) / (x2 - x1)

i = 0
while True:
    i += 1
    n, global_max = int(input()), 0
    if not n:
        break
    points = tuple(tuple(int(i) for i in input().split()) for _ in range(n))
    for j, (x1, y1) in itertools.islice(enumerate(points), 1, n):
        global_max = max(collections.Counter(slope(x1, y1, x2, y2) for x2, y2 in itertools.islice(points, j)).most_common(1)[0][1], global_max)
    global_max += 1
    if global_max < 4:
        global_max = 0
    print(f"Photo {i}: {global_max} points eliminated")