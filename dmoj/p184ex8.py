import sys

input = sys.stdin.readline

a, b, c, d, e, f, spoiled = 0, 0, 0, 0, 0, 0, 0
for i in range(int(input())):
    vote = input().strip()
    if vote == "A":
        a += 1
    elif vote == "B":
        b += 1
    elif vote == "C":
        c += 1
    elif vote == "D":
        d += 1
    elif vote == "E":
        e += 1
    elif vote == "F":
        f += 1
    else:
        spoiled += 1
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(spoiled)