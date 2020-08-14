score, letter = 0, ""
stuff = list("abcdefghijklmnopqrstuvwxyz")

lengths = []
string = input().strip()
for i in range(len(stuff)):
    for j in range(i + 1, len(stuff)):
        ree = string[::]
        ree = ree.replace(stuff[i], "")
        ree = ree.replace(stuff[j], "")
        lengths.append(len(ree))
print(min(lengths))