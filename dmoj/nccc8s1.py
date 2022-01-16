alphabet, string, res = [char for char in input().strip()], [char for char in input().strip()], []
for i in range(len(string)):
    res.append("".join(string[:i] + string[i + 1:]))
for i in range(len(string)):
    for j in range(len(alphabet)):
        res.append("".join(string[:i] + [alphabet[j]] + string[i + 1:]))
for i in range(len(string) + 1):
    for j in range(len(alphabet)):
        res.append("".join(string[:i] + [alphabet[j]] + string[i:]))

res = set(res)
res.remove("".join(string))
for result in sorted(list(res)):
    print(result)