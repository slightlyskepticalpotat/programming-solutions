for _ in range(int(input())):
    n, m = map(int, input().split())
    dist, order = {}, []
    for i in range(n):
        row = [int(i) for i in input().split()]
        dist[row[0]] = row
    for i in range(m):
        column = [int(i) for i in input().split()]
        if column[0] in dist:
            order = column
    for row in order:
        print(*dist[row])
