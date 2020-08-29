a, b = map(int, input().split())
c, d = map(int, input().split())
e, f = map(int, input().split())
x, y = 0, 0
if a == c:
    x = e
elif a == e:
    x = c
elif c == e:
    x = a
if b == d:
    y = f
elif b == f:
    y = d
elif d == f:
    y = b
print(x, y)