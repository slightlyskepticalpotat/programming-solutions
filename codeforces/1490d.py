import sys

input = sys.stdin.readline

def build_binary_tree(l, r, d):
    if l > r:
        return
    if l == r:
        depths[l] = d
        return
    pivot = values[l:r + 1].index(max(values[l:r + 1])) + l
    depths[pivot] = d
    build_binary_tree(l, pivot - 1, d + 1)
    build_binary_tree(pivot + 1, r, d + 1)

for _ in range(int(input())):
    n, values, depths = int(input()), [int(i) for i in input().split()], [-1 for _ in range(101)]
    build_binary_tree(0, n - 1, 0)
    print(*depths[:n])
