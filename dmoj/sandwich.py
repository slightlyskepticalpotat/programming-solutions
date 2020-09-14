import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
steps, sandwich = [int(i) for i in input().strip()], deque([])

for i in range(n):
    if steps[i]:
        sandwich.appendleft(i + 1)
    else:
        sandwich.append(i + 1)

while sandwich:
    print(sandwich.popleft())