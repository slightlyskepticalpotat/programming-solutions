import sys

input = sys.stdin.readline

n, k = map(int, input().split())
values, used, last, res = [int(input()) for _ in range(n)], {i + 1: False for i in range(k)}, {i + 1: -1 for i in range(k)}, []
for i in range(n):
    last[values[i]] = i
for i in range(n):
    if not used[values[i]]:
        while res and res[-1] > values[i] and i < last[res[-1]]: # check that the array has elements and we can swap in a smaller element and the bigger element exists later in the array
            used[res.pop()] = False
        res.append(values[i])
        used[values[i]] = True
print(*res)