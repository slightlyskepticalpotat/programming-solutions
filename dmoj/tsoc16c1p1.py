for i in range (int(input())):
    l, a, b, f = map(int, input().strip().split())
    if a <= l-f <= b:
        print("Yes")
    else:
        print("No")