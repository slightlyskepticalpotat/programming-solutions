for _ in range(int(input())):
    n, m = map(int, input().split())
    bottom, left, res = [int(i) for i in input().split()], [int(i) for i in input().split()], 0
    for train in bottom:
        if train in left:
            res += 1
    print(res)
