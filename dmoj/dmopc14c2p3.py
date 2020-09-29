import sys

input = sys.stdin.readline

n = int(input())
rates = list(sorted([int(i) for i in input().split()], reverse = True))
logs = list(sorted([int(i) for i in input().split()]))

print(sum([rates[i] * logs[i] for i in range(n)]))