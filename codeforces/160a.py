n = int(input())
values = list(sorted([int(i) for i in input().split()], reverse = True) + [0])
for i in range(n + 1):
    if sum(values[:i]) > sum(values[i:]):
        print(i)
        break
