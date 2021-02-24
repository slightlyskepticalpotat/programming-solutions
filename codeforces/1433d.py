for _ in range(int(input())):
    n, values = int(input()), [int(i) for i in input().split()]
    if len(set(values)) == 1:
        print("NO")
    else:
        print("YES")
        first = 0
        for i in range(n):
            if values[i] != values[0]:
                second = i
                break
        print(first + 1, second + 1)
        for i in range(n):
            if i != first and i != second:
                if values[i] != values[0]:
                    print(first + 1, i + 1)
                else:
                    print(second + 1, i + 1)
