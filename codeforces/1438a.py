import statistics

n, values, diff = int(input()), sorted([int(i) for i in input().split()]), []
for i in range(n - 1):
    diff.append(values[i + 1] - values[i])
diff_len = len(set(diff))
if n == 1:
    print(-1)
elif diff_len == 1:
    if diff[0] == 0:
        works = [values[-1] + diff[0]]
        print(len(works))
        print(*sorted(works))
    else:
        works = [values[0] - diff[0], values[-1] + diff[0]]
        if n == 2:
            if not (values[0] + values[1]) % 2:
                works.append((values[0] + values[1]) // 2)
        print(len(works))
        print(*sorted(works))
elif diff_len == 2:
    common, works = min(statistics.multimode(diff)), []
    if common:
        for i in range(1, n):
            if values[i - 1] + common == values[i] - common:
                works.append(values[i - 1] + common)
    if len(works) > 1:
        works = []
    print(len(works))
    if works:
        print(*sorted(works))
else:
    print(0)
