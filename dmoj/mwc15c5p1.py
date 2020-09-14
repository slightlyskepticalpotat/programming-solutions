import statistics

n = int(input())
m = [float(i) for i in input().strip().split()]
print(statistics.mean(m))
print(statistics.median(m))
print(*sorted(statistics.multimode(m)))