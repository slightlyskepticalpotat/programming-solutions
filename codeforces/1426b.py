for _ in range(int(input())):
    n, m = map(int, input().split())
    tiles, flag = [[int(i) for i in input().split()] + [int(i) for i in input().split()] for j in range(n)], False
    if m % 2:
        print("NO")
    else:
        for tile in tiles:
            if tile[1] == tile[2]:
                flag = True
        if flag:
            print("YES")
        else:
            print("NO")
