import itertools

for _ in range(int(input())):
    a, b = map(int, input().split())
    mines, cost = [list(y) for x, y in itertools.groupby([int(i) for i in input().strip()])], 0
    for i in range(len(mines)):
        if mines[i][0] == 0:
            if len(mines[i]) * b < a and 0 < i < len(mines) - 1:
                cost += len(mines[i]) * b
                mines[i] = [1] * len(mines[i])
    mines = itertools.chain.from_iterable(mines)
    mines = [list(y) for x, y in itertools.groupby(mines)]
    for i in range(len(mines)):
        if mines[i][0] == 1:
            cost += a
    print(cost)
