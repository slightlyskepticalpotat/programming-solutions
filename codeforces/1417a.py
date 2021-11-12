import math

for _ in range(int(input())):
    n, k = map(int, input().split())
    values = [int(i) for i in input().split()]
    copy, copy_index, ans = min(values), values.index(min(values)), 0
    for i in range(n):
        if i != copy_index:
            ans += math.floor((k - values[i]) / copy)
    print(ans)
