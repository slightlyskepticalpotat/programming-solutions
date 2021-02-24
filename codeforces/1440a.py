for _ in range(int(input())):
    n, c0, c1, h = map(int, input().split())
    string = input().strip()
    zeros, ones = string.count("0"), string.count("1")
    print(min(min(n * c0 + (n - zeros) * h, n * c1 + (n - ones) * h), zeros * c0 + ones * c1))
