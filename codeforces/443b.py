def equal(a, b):
    for i in range(len(a)):
        if a[i] != b[i] and a[i] != "*" and b[i] != "*":
            return False
    return True

string, k, best = input().strip(), int(input()), 0
string += "*" * k
for i in range(len(string) + 1):
    for j in range(i + 1, len(string) + 1):
        if not (j - i) % 2:
            if equal(string[i:(i + j) // 2], string[(i + j) // 2: j]):
                best = max(best, j - i)
print(best)
