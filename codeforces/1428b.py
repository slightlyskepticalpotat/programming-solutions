for _ in range(int(input())):
    n, belts = int(input()), input().strip()
    if not ">" in belts or not "<" in belts:
        pass
    else:
        n = 0
        for i in range(len(belts)):
            if belts[(i + 1) % len(belts)] == "-" or belts[i] == "-":
                n += 1
    print(n)
