x, y = map(int, input().split())
print(x * y // 2, end = "")
if (x * y) % 2 == 0:
    print(".0")
else:
    print(".5")