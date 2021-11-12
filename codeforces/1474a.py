for _ in range(int(input())):
    n, b = int(input()), [int(char) for char in input().strip()]
    a = [1] + [0 for i in range(n - 1)]
    for i in range(1, n):
        if 1 + b[i] != a[i - 1] + b[i - 1]:
            a[i] = 1
        else:
            a[i] = 0
    print("".join([str(char) for char in a]))
