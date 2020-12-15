import sys

input = sys.stdin.readline

for _ in range(5):
    capacity, items = int(input()), int(input())
    backpack = [[0] * (capacity + 1) for _ in range(2)] # initialize dp array, actually only need 2 rows
    weight, value = [], []
    for i in range(items):
        a, b = map(int, input().split())
        weight.append(a)
        value.append(b)
    
    for i in range(items):
        if i % 2 == 0:
            for j in range(capacity + 1):
                if weight[i] <= j:
                    backpack[1][j] = max(value[i] + backpack[0][j-weight[i]], backpack[0][j])
                else:
                    backpack[1][j] = backpack[0][j] # carry previous maximum forward
        else:
            for j in range(capacity + 1):
                if weight[i] <= j:
                    backpack[0][j] = max(value[i] + backpack[1][j-weight[i]], backpack[1][j])
                else:
                    backpack[0][j] = backpack[1][j] # this basically cycles the two rows to reduce memory usage
    if items % 2 == 0: # prints 1 or 2nd row
        print(backpack[0][capacity])
    else:
        print(backpack[1][capacity])
    placeholder = input()