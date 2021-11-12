import math

def indulge(x, y):
    if not x % y or not y % x or math.gcd(x, y) == 1:
        return True
    else:
        return False

for _ in range(int(input())):
    n, chairs = int(input()), []
    for i in range(4 * n, 0, -1):
        if not chairs or not sum([indulge(i, chair) for chair in chairs]):
            chairs.append(i)
        if len(chairs) == n:
            break
    print(*chairs)
