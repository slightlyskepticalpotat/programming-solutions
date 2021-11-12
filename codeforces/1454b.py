for _ in range(int(input())):
    n, values = int(input()), [int(i) for i in input().split()]
    table, count, filtered = {-1: -1}, {i + 1: 0 for i in range(n)}, []
    for i in range(n):
        table[values[i]] = i + 1
        count[values[i]] += 1
    for key in count:
        if count[key] == 1:
            filtered.append(key)
    if filtered == []:
        filtered = [-1]
    print(table[min(filtered)])
