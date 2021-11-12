for _ in range(int(input())):
    n, m = map(int, input().split())
    values = [int(i) for i in input().split()]
    if sum(values) == m:
        print("YES")
    else:
        print("NO")
