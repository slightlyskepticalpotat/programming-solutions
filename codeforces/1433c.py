for _ in range(int(input())):
    n, values = int(input()), [int(i) for i in input().split()]
    if len(set(values)) == 1:
        print(-1)
    else:
        dominant = max(values)
        for i in range(n):
            if values[i] == dominant:
                if i == 0 and values[i] > values[i + 1]:
                    print(i + 1)
                    break
                elif i == n - 1 and values[i] > values[i - 1]:
                    print(i + 1)
                    break
                elif i != 0 and i != n - 1 and values[i] > values[i - 1] or values[i] > values[i + 1]:
                    print(i + 1)
                    break
