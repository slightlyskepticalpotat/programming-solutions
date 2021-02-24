for _ in range(int(input())):
    n, values = int(input()), input().strip()
    l, r = values.index("1"), values.rindex("1")
    print(values[l:r + 1].count("0"))
