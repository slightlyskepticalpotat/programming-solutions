for _ in range(int(input())):
    n, k = map(int, input().split())
    values = sorted([int(i) for i in input().split()])
    top = max(values)
    values.remove(top)
    for i in range(k):
        top += values.pop()
    print(top)
