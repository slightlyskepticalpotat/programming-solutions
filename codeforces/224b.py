# minimal by inclusion means that any subset cannot satisfy the same requirements (essentially no duplicates at either end)

n, k = map(int, input().split())
values, single, l, r = [int(i) for i in input().split()], set(), -1, -1
for i in range(n):
    single.add(values[i])
    if len(single) == k:
        l, r = 1, i + 1
        break
single = set()
for i in range(r - 1, max(-1, l - 2), -1):
    single.add(values[i])
    if len(single) == k:
        l = i + 1
        break
        
if len(single) < k:
    print(-1, -1)
else:
    print(l, r)
