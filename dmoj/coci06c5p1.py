import sys
input = sys.stdin.readline

cups = ["ball", "none", "none"]

for thing in [char for char in input().strip()]:
    if thing == "A":
        cups[0], cups[1] = cups[1], cups[0]
    elif thing == "B":
        cups[1], cups[2] = cups[2], cups[1]
    elif thing == "C":
        cups[0], cups[2] = cups[2], cups[0]
print(cups.index("ball") + 1)