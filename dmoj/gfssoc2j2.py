x, y = 1, 1

for i in range(int(input())):
    output = []
    if x % 91 == 0:
        output.append("Fizz Fuzz")
    elif x % 7 == 0:
        output.append("Fizz")
    elif x % 13 == 0:
        output.append("Fuzz")
    else:
        output.append(x)
    if y % 91 == 0:
        output.append("Fizz Fuzz")
    elif y % 7 == 0:
        output.append("Fizz")
    elif y % 13 == 0:
        output.append("Fuzz")
    else:
        output.append(y)
    x += 1
    y += 2
    print(*output)