import sys

input = sys.stdin.readline

for i in range(int(input())):
    n = int(input())
    scores = [int(i) for i in input().strip().split()]
    print(f"{min(scores)} {max(scores)}")