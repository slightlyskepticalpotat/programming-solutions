n, m = map(int, input().split())
names, ans = [set() for _ in range(m)], 1
for _ in range(n):
    name = input().strip()
    for i in range(m):
        names[i].add(name[i])
for i in range(m): # basic permutations
    ans = ans * len(names[i])
    ans %= 1000000007
print(ans)
