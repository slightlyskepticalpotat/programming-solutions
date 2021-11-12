for _ in range(int(input())):
    n, ans = int(input()), []
    ans = [i + 1 for i in range(n)]
    print(len(ans))
    print(*ans)
