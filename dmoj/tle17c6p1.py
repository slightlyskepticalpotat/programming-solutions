number = int(input())
molecules = sorted(list(input()))
maximum = molecules.count(max(set(molecules), key = molecules.count))
if number % 2 == 1 or maximum > number / 2:
    print("No")
else:
    print("Yes")