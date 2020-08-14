import sys, statistics
input = sys.stdin.readline

n, x = map(int, input().split())
numbers = [int(i) for i in input().split()]
count = 0

for i in range(0, n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if statistics.median([numbers[i], numbers[j], numbers[k]]) == x:
                count += 1
print(count)