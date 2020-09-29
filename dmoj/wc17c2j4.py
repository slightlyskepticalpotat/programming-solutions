def consonant(x):
    if x in ["-", "a", "e", "i", "o", "u"]:
        return False
    return True

old, new = input().strip(), ""
for i in range(len(old)):
    if i == 0 or not consonant(old[i]) or not consonant(new[-1]):
        new += old[i]

if "-" in new:
    new, final = [char for char in new.split("-")], []
else:
    new, final = [new], []

for i in range(len(new)):
    if i == 0 or new[i] != new[i - 1]:
        final.append(new[i])
print("-".join(final))