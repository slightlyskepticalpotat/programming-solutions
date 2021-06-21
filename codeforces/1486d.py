import sys

input = sys.stdin.readline

def query(l, r):
    if l == r:
        return -1
    print(f"? {l} {r}", flush=True)
    return int(input())

n = int(input())
pivot = query(1, n)
if pivot == 1 or query(1, pivot) != pivot: # max element to right
    l, r = pivot, n
    while r > l + 1:
        m = (l + r) // 2
        if query(pivot, m) == pivot:
            r = m
        else:
            l = m
    print(f"! {r}", flush=True)
else:
    l, r = 1, pivot
    while r > l + 1:
        m = (l + r) // 2
        if query(m, pivot) == pivot:
            l = m
        else:
            r = m
    print(f"! {l}", flush=True)
