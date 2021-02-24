for _ in range(int(input())):
    n, k = map(int, input().split())
    values, tries = [int(i) for i in input().split()], []
    for i in set(values):
        new_values = [int(i) for i in values]
        paint = 0
        for j in range(n):
            if new_values[j] != i:
                for l in range(j, min(j + k, n)):
                    new_values[l] = i
                paint += 1
        tries.append(paint)
    print(min(tries))
