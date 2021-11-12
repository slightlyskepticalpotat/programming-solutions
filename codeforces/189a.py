n, a, b, c = map(int, input().split())
possible = []
for i in range(n // a + 1):
    for j in range(n // b + 1):
        if (n - (i * a) - (j * b)) >= 0 and (n - (i * a) - (j * b)) % c == 0:
            possible.append(i + j + (n - (i * a) - (j * b)) // c)
print(max(possible))
