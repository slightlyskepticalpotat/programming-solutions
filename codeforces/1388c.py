import sys

input = sys.stdin.readline
sys.setrecursionlimit(2 ** 16)

def dfs(x, last = float("inf")):
    global ans
    current_happy = 0
    for peer in graph[x]:
        if peer != last:
            dfs(peer, x)
            current_happy, visits[x] = current_happy + happy_visits[peer], visits[x] + visits[peer]
    happy_visits[x] = (visits[x] + happy[x]) / 2
    ans &= happy_visits[x] == happy_visits[x] // 1 # must be int
    ans &= 0 <= happy_visits[x] <= visits[x] # must be in bounds
    ans &= current_happy <= happy_visits[x] # cannot increase

for _ in range(int(input())):
    n, m = map(int, input().split())
    residents, happy, ans = [int(i) for i in input().split()], [int(i) for i in input().split()], True
    visits, happy_visits, graph = [i for i in residents], [0 for i in range(n)], {i: [] for i in range(n)}
    for i in range(n - 1):
        x, y = map(int, input().split())
        graph[x - 1].append(y - 1)
        graph[y - 1].append(x - 1)
    dfs(0)
    if ans:
        print("YES")
    else:
        print("NO")
