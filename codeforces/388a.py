n, required, searched = int(input()), 0, []
boxes = list(sorted([int(i) for i in input().split()]))
while True:
    stack = 0
    for i in range(n):
        if i not in searched and boxes[i] >= stack:
                searched.append(i)
                stack += 1
    if stack:
        required += 1
    else:
        break
print(required)
