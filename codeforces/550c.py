n, works = input(), -1
for i in range(len(n)):
    if not int(n[i]) % 8:
        works = int(n[i])
for i in range(len(n)):
    for j in range(i + 1, len(n)):
        if not int(n[i] + n[j]) % 8:
            works = int(n[i] + n[j])
for i in range(len(n)):
    for j in range(i + 1, len(n)):
        for k in range(j + 1, len(n)):
            if not int(n[i] + n[j] + n[k]) % 8:
                works = int(n[i] + n[j] + n[k])
if works != -1:
    print("YES")
    print(works)
else:
    print("NO")
