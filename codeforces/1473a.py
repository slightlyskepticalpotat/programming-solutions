for _ in range(int(input())):
    n, d = map(int, input().split())
    values = sorted([int(i) for i in input().split()])
    if values[0] + values[1] <= d or max(values) <= d:
        print("YES")
    else:
        print("NO")
