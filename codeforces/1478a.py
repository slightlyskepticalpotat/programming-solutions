import statistics

for _ in range(int(input())):
    n, values = int(input()), [int(i) for i in input().split()]
    print(values.count(statistics.mode(values)))
