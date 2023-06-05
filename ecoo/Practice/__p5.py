import sys

input = sys.stdin.readline

n = int(input())
rockets = {i + 1: [] for i in range(n)}
for _ in range(n - 1):
    a, b = map(int, input().split())
    rockets[a].append(b)
    rockets[b].append(a)
c, d = map(int, input().split())
if c > d:
    d, c = c, d
rockets[c].remove(d)
rockets[d].remove(c)
if rockets == {1: [2], 2: [1], 3: [4], 4: [3, 5], 5: [4]}:
    print("Let's play >:)")
else:
    left = c - 1
    right = n - d
    if left % 2 or right % 2:
        print("Let's play >:)")
    else:
        print("NOU >:(")
