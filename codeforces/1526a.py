import collections, sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, values = int(input()), collections.deque(sorted([int(i) for i in input().split()]))
    result = [values.popleft() if i % 2 else values.pop() for i in range(2 * n)]
    print(*result)
