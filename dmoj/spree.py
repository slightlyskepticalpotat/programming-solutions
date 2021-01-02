import sys

input = sys.stdin.readline

def knapsack(items, capacity, utility, cost):
    backpack = [[0] * (capacity + 1) for _ in range(2)]
    for i in range(items):
        if i % 2 == 0:
            for j in range(capacity + 1):
                if cost[i] <= j:
                    backpack[1][j] = max(utility[i] + backpack[0][j - cost[i]], backpack[0][j])
                else:
                    backpack[1][j] = backpack[0][j]
        else:
            for j in range(capacity + 1):
                if cost[i] <= j:
                    backpack[0][j] = max(utility[i] + backpack[1][j - cost[i]], backpack[1][j])
                else:
                    backpack[0][j] = backpack[1][j]
    if not items % 2:
        return backpack[0][capacity]
    else:
        return backpack[1][capacity]

utility, cost = [], []
items, capacity = map(int, input().split())
for _ in range(items):
    u, c = map(int, input().split())
    utility.append(u)
    cost.append(c)
    
print(knapsack(items, capacity, utility, cost))