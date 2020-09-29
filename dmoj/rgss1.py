a, b, c = map(int, input().split())
max = 0
for i in range(c // a + 1):
    check = i * a + (c - i * a) // b * b
    if max < check:
        max = check
print(max)