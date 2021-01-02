warnings, counts = 0, {}

for i in range(int(input())):
    name = input().strip()
    if counts.get(name, 0) > sum([counts[key] for key in counts]) - counts.get(name, 0):
        warnings += 1
    counts[name] = counts.get(name, 0) + 1
print(warnings)