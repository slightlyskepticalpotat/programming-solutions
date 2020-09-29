import statistics

medians = []
for i in range(int(input())):
    medians.append(statistics.median([int(i) for i in input().split()]))
print(statistics.median(medians))