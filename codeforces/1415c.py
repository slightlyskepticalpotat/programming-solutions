for _ in range(int(input())):
    n, p, k = map(int, input().split())
    level = input().strip()
    x, y = map(int, input().split())
    costs, total = [-1 for i in range(k)], float("inf") # cost of starting at different cells
    for i in range(k):
        l = 0
        for j in range(i, n, k):
            if j >= p - 1 and level[j] == "0": # screen out last cells
                l += 1
        costs[i] = l
    for i in range(p - 1, n):
        total = min(total, x * costs[i % k] + y * (i + 1 - p))
        if level[i] == "0": # to update the rest of the cells
            costs[i % k] -= 1
    print(total)
