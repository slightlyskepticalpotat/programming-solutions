import sys

input = sys.stdin.readline

triangles = [tuple([int(i) for i in input().split()] + [j + 1]) for j in range(int(input()))]
triangles.sort(key = lambda x: x[0])

for i in range(len(triangles) - 2):
    if len(set([triangles[i][2], triangles[i + 1][2], triangles[i + 2][2]])) == 2:
        print(triangles[i][3], triangles[i + 1][3], triangles[i + 2][3])
        sys.exit()
print(-1)