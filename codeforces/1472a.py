for _ in range(int(input())):
    w, h, n = map(int, input().split())
    sheets = 1
    while not w % 2:
        sheets *= 2
        w /= 2
    while not h % 2:
        sheets *= 2
        h /= 2
    if sheets >= n:
        print("YES")
    else:
        print("NO")
