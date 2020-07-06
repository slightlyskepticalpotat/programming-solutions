print(8128)
for i in range(100, 1000):
    if i == sum([int(n)**3 for n in list(str(i))]):
        print(i, end=" ")