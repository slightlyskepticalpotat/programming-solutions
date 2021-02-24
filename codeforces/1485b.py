import sys

input = sys.stdin.readline

n, q, k = map(int, input().split())
values = [int(i) for i in input().split()]
for _ in range(q):
    l, r = map(int, input().split())
    count = values[l - 1] + k - values[r - 1] + 2 * ((values[r - 1] - values[l - 1] + 1) - (r - l + 1)) # last part is available minus taken
    print(count - 1)
