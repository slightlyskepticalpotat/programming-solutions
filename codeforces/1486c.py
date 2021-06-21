import sys

input = sys.stdin.readline

def query(l, r):
    if l == r:
        return -1
    print(f"? {l} {r}", flush=True)
    return int(input())

l, r = 1, int(input()) + 1
while r > l + 1:
    m = (l + r) // 2
    pre = query(l, r - 1)
    if pre < m:
        if query(l, m - 1) == pre:
            r = m
        else:
            l = m
    else:
        if query(m, r - 1) == pre:
            l = m
        else:
            r = m
print(f"! {l}", flush=True)
