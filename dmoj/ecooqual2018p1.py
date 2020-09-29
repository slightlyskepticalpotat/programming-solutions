import sys

input = sys.stdin.readline

for i in range(int(input())):
    n = int(input())
    costs = [int(i) for i in input().split()]
    produced = [int(i) for i in input().split()]
    total = sum([costs[i] * produced[i] for i in range(n)])
    print(total)