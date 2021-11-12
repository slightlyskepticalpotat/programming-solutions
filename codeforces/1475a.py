for _ in range(int(input())):
    n = int(input())
    while not n % 2:
        n /= 2
    if n == 1:
        print("NO")
    else:
        print("YES")
