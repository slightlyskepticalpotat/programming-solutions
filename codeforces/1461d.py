import bisect, sys

input = sys.stdin.readline

def process(l, r):
    possible.add(sum(values[l: r + 1]))
    mid, pivot = (values[l] + values[r]) // 2, -1
    for i in range(l, r + 1):
        if values[i] <= mid:
            pivot = i
        else:
            break
    if pivot in [-1, r]:
        return
    process(l, pivot)
    process(pivot + 1, r)

for _ in range(int(input())):
    n, q = map(int, input().split())
    values, possible = list(sorted([int(i) for i in input().split()])), set()
    process(0, n - 1)
    for i in range(q):
        if int(input()) in possible:
            print("Yes")
        else:
            print("No")
