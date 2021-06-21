import itertools, string, sys

input = sys.stdin.readline

cand = list(map("".join, itertools.product(string.ascii_lowercase, repeat = 3))) + list(map("".join, itertools.product(string.ascii_lowercase, repeat = 2))) + list(map("".join, itertools.product(string.ascii_lowercase, repeat = 1)))
cand.sort(key = len)

for _ in range(int(input())):
    n, s, ans = int(input()), input().strip(), []
    for i in cand:
        if i not in s:
            print(i)
            break
