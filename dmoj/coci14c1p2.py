x, y = set(), set()
for i in range(int(input())):
    a, b = map(int, input().split())
    x.add(a)
    y.add(b)
print(max(max(x) - min(x), max(y) - min(y)) ** 2)