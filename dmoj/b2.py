for i in range(int(input())):
    a, b = input().strip().split()
    a, b = int(a[::-1]), int(b[::-1])
    print(str(int(str(a + b)[::-1])))