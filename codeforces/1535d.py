import sys

input = sys.stdin.readline

def update(x):
    if s[x] == "0": # higher indexed wins
        cnt[x] = cnt[2 * x + 2]
    elif s[x] == "1": # lower indexed wins
        cnt[x] = cnt[2 * x + 1]
    else: # either of them can win
        cnt[x] = cnt[2 * x + 2] + cnt[2 * x + 1]

k, s = int(input()), [char for char in input().strip()][::-1]
n = (2 ** k) - 1 # size of pseudo-segtree
cnt = [1 for _ in range(n * 2 + 1)] # high and low for each

for i in range(n - 1, -1, -1): # initialise the pseudo-segtree
    update(i)

for _ in range(int(input())):
    p, c = input().strip().split()
    p = n - int(p) # reverse the index
    s[p] = c
    while p:
        update(p)
        p = (p - 1) // 2
    update(0)
    print(cnt[0])
