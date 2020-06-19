import sys
from collections import deque
input = sys.stdin.readline

weights = []
max_weight = int(input())
cars = int(input())
for i in range(cars):
    weights.append(int(input()))
queue = deque()
counter = 0

for thing in weights:
    queue.appendleft(thing)
    if len(queue) > 4:
        queue.pop()
    if sum(queue) > max_weight:
        break
    else:
        counter+=1
print(counter)