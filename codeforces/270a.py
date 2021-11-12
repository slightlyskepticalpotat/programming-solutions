for _ in range(int(input())):
    d = 180 - int(input())
    if 360 % d == 0:
        print("YES")
    else:
        print("NO")
