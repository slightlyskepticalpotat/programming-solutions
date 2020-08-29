import sys

input = sys.stdin.readline

drilled = [[200, 0], [200, 1], [200, 2], [201, 2], [202, 2], [203, 2], [203, 3], [203, 4], [204, 4], [205, 4], [205, 3], [205, 2], [206, 2], [207, 2], [207, 3], [207, 4], [207, 5], [207, 6], [206, 6], [205, 6], [204, 6], [203, 6], [202, 6], [201, 6], [200, 6], [199, 6], [199, 5], [199, 4]]
plan = [[False] * 401 for i in range(201)] # extra safety margin
x, y = 199, 4 # to convert x subtract 200, for y add 1 and negate

for x, y in drilled:
    plan[y][x] = True

while True:
    direction, distance = input().strip().split()
    distance = int(distance)
    flag = False
    if direction == "q":
        break
    elif direction == "d":
        for _ in range(distance):
            y += 1
            if plan[y][x] == True:
                flag = True
            plan[y][x] = True
    elif direction == "u":
        for _ in range(distance):
            y -= 1
            if plan[y][x] == True:
                flag = True
            plan[y][x] = True
    elif direction == "l":
        for _ in range(distance):
            x -= 1
            if plan[y][x] == True:
                flag = True
            plan[y][x] = True
    elif direction == "r":
        for _ in range(distance):
            x += 1
            if plan[y][x] == True:
                flag = True
            plan[y][x] = True
    if not flag:
        print(f"{x - 200} {-(y + 1)} safe")
    else:
        print(f"{x - 200} {-(y + 1)} DANGER")