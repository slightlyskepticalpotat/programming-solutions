for _ in range(int(input())):
    n, flag = int(input()), False
    while n > 0:
        if not n % 2021 or not n % 2020:
            flag = True
        n -= 2020
    if flag:
        print("YES")
    else:
        print("NO")
