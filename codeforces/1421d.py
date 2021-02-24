for _ in range(int(input())):
    repl = True
    x, y = map(int, input().split())
    c1, c2, c3, c4, c5, c6 = map(int, input().split())
    while repl: # we try to replace edges
        repl = False
        if c1 + c3 < c2:
            c2 = c1 + c3
            repl = True
        if c2 + c4 < c3:
            c3 = c2 + c4
            repl = True
        if c3 + c5 < c4:
            c4 = c3 + c5
            repl = True
        if c4 + c6 < c5:
            c5 = c4 + c6
            repl = True
        if c5 + c1 < c6:
            c6 = c5 + c1
            repl = True
        if c6 + c2 < c1:
            c1 = c6 + c2
            repl = True
    if x >= 0 and y >= 0:
        pivot = min(x, y)
        print(c1 * pivot + c2 * (y - pivot) + c6 * (x - pivot))
    elif x <= 0 and y <= 0:
        pivot = min(-x, -y)
        print(c4 * pivot + c5 * (-y - pivot) + c3 * (-x - pivot))
    elif x >= 0 and y <= 0:
        print(c6 * x + c5 * (-y))
    elif x <= 0 and y >= 0:
        print(c3 * (-x) + c2 * y)
