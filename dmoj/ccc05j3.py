import sys
input = sys.stdin.readline
directions = []

while True:
    directions.append(input().strip())
    if directions[-1] == "SCHOOL":
        break
directions.reverse()

for i in range(1, len(directions)-1, 2):
    if directions[i] == "L":
        l_r = "RIGHT"
    elif directions[i] == "R":
        l_r = "LEFT"
    print("Turn " + l_r + " onto " + directions[i+1] + " street.")
    
if directions[-1] == "R":
    print("Turn LEFT into your HOME.")
else:
    print("Turn RIGHT into your HOME.")