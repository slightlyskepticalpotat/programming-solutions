contestants = [sum([int(i) for i in input().split()]) for j in range(5)]
print(contestants.index(max(contestants)) + 1, max(contestants))