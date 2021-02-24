for _ in range(int(input())):
    n = int(input())
    if n in [1, 2, 3]:
        print(n - 1)
    elif not n % 2:
        print(2)
    else:
        print(3)
