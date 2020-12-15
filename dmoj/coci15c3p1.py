n = 0
for i in range(int(input())):
    p = input().strip()
    n += int(p[:-1]) ** int(p[-1])
print(n)