import sys

input = sys.stdin.readline

n, best, rectangles = int(input()), 0, set()
for _ in range(n):
    rectangles.add(tuple(int(i) for i in input().split()))
for point1 in rectangles:
    for point2 in rectangles:
        if (point1[0], point2[1]) in rectangles and (point2[0], point1[1]) in rectangles: # check if it forms a diagonal
            best = max(best, abs(point1[0] - point2[0]) * abs(point1[1] - point2[1]))
print(best)