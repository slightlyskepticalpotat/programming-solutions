n = int(input())
if not n % 2:
    print((n // 2 + 1) ** 2)
else:
    print(2 * (n // 2 + 1) * (n // 2 + 2))
