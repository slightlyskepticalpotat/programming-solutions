import functools, math, sys

input = sys.stdin.readline

def knapsack(capacity, utility, weight):
    backpack = [[0 for i in range(capacity + 1)] for j in range(2)]
    for i in range(len(weight)):
        for j in range(capacity + 1):
            if weight[i] <= j: # 0 if i odd, 1 if even
                backpack[(i + 1) % 2][j] = max(utility[i] + backpack[i % 2][j - weight[i]], backpack[i % 2][j])
            else:
                backpack[(i + 1) % 2][j] = backpack[i % 2][j]
    return backpack[len(weight) % 2][capacity]

n, values = int(input()), [int(i) for i in input().split()]
if sum(values) % 2 or knapsack(sum(values) // 2, values, values) != sum(values) // 2:
    print(0)
else:
    gcd = functools.reduce(math.gcd, values)
    values = [values[i] // gcd for i in range(n)]
    for i in range(n): # remove the odd one out
        if values[i] % 2:
            print(1)
            print(i + 1)
            sys.exit()
