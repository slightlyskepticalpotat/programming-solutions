level = int(input())
collisions = 0
plushies = []
for i in range(int(input())):
    plushies.append(int(input()))

for thing in plushies:
    if level <= thing:
        collisions += 1
print(collisions)