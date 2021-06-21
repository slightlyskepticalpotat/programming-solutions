def is_cube_root(x):
    return x and int(round((x ** (1 / 3)))) ** 3 == x

for _ in range(int(input())):
    x, flag = int(input()), False
    for i in range(1, int(x ** (1 / 3)) + 1):
        if is_cube_root(x - i ** 3):
            flag = True
    if flag:
        print("YES")
    else:
        print("NO")
