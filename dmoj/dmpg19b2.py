molecules = [int(i) for i in input().split()]
max1, max2 = list(sorted(molecules, reverse = True))[0], list(sorted(molecules, reverse = True))[1]
if abs(molecules.index(max1) - molecules.index(max2)) == 2:
    print("trans")
else:
    print("cis")