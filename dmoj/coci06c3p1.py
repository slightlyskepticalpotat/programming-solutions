dwarves = [int(input()) for _ in range(9)]
total = sum(dwarves)
for i in range(9):
    for j in range(i + 1, 9):
        if total - dwarves[i] - dwarves[j] == 100:
            print("\n".join([str(dwarves[k]) for k in range(len(dwarves)) if k not in [i, j]]))
            raise SystemExit