for _ in range(int(input())):
    n, values = int(input()), [int(i) for i in input().split()]
    if len(set(values)) == n and values == list(sorted(values, reverse = True)):
        print("NO")
    else:
        print("YES")
