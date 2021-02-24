n = int(input())
for i in range(n):
    line = [str(j) for j in range(i)] + [str(j) for j in range(i, -1, -1)]
    print(" ".join(line).center((n * 2 + 1) * 2 - 1).rstrip())
line = [str(j) for j in range(n)] + [str(j) for j in range(n, -1, -1)]
print(" ".join(line).center((n * 2 + 1) * 2 - 1).rstrip())
for i in range(n - 1, -1, -1):
    line = [str(j) for j in range(i)] + [str(j) for j in range(i, -1, -1)]
    print(" ".join(line).center((n * 2 + 1) * 2 - 1).rstrip())
