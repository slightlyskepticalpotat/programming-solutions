for _ in range(int(input())):
    n, jumps = int(input()), 0
    while jumps * (jumps + 1) / 2 < n:
        jumps += 1
    if jumps * (jumps + 1) / 2 == n + 1:
        jumps += 1
    print(jumps)
