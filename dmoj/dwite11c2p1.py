i, steps = 1, ""
while len(steps) < 100000:
    if i % 2 == 1:
        steps += "R" * i
    else:
        steps += "D" * i
    i += 1

for i in range(5):
    x, y = 0, 0
    for j in range(int(input())):
        if steps[j] == "R":
            x += 1
        else:
            y -= 1
    print(x, y)