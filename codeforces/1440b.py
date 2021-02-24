for _ in range(int(input())):
    n, k = map(int, input().split())
    values, sum = [int(i) for i in input().split()], 0
    for i in range(k * ((n - 1) // 2), n * k, n // 2 + 1):
        sum += values[i]
    print(sum)
