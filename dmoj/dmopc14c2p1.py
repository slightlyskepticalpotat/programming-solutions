trees = []
for i in range(int(input())):
    x = 0
    for i in range(int(input())):
        x+=int(input())
    trees.append(x)
for i in range(1, len(trees)+1):
    if trees[i-1] == 0:
        print("Weekend")
    else:
        print("Day {day}: {mass}".format(day=i, mass=trees[i-1]))