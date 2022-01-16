import sys

input = sys.stdin.readline

n, q = map(int, input().split())
a, b = [i for i in range(n)], [i for i in range(n)] # a = i, b = a[i]
for i in range(q):
    query = [i for i in input().split()]
    x, y = int(query[1]) - 1, int(query[2]) - 1
    if query[0] == "B":
        a[b[x]], a[b[y]] = a[b[y]], a[b[x]]
        b[x], b[y] = b[y], b[x]
    elif query[0] == "E":
        a[x], a[y] = a[y], a[x]
        b[a[x]], b[a[y]] = x, y
    else:
        query, ans = [int(i) for i in query[1:]], [0 for i in range(n)]
        for i in range(n):
            ans[a[i]] = query[i]
        print(*ans)