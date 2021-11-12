for _ in range(int(input())):
    n, values = int(input()), [int(i) for i in input().split()]
    if len(set(values)) < len(values):
        print("YES")
    else:
        print("NO")
