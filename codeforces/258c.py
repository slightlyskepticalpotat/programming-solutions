n, values, total = int(input()), list(sorted([int(i) for i in input().split()])), 0
for i in range(n):
    total += abs((i + 1) - values[i])
print(total)
