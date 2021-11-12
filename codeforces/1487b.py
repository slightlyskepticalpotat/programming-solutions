for _ in range(int(input())):
    n, k = map(int, input().split())
    k -= 1
    print((k + (n % 2) * k // (n // 2)) % n + 1)
