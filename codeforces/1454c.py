for _ in range(int(input())):
    n, values = int(input()), [int(i) for i in input().split()]
    reals, counts, tries = [values[0]], {}, []
    for i in range(1, n):
        if values[i] != values[i - 1]:
            reals.append(values[i])
    for i in range(len(reals)):
        if reals[i] in counts:
            counts[reals[i]] += 1
        else:
            counts[reals[i]] = 1
    counts[reals[-1]] -= 1
    counts[reals[0]] -= 1
    for i in range(len(reals)):
        tries.append(counts[reals[i]] + 1)
    print(min(tries))
