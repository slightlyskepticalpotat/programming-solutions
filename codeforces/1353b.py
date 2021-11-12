import collections, sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    a, b, i = collections.deque(sorted([int(i) for i in input().split()])), collections.deque(sorted([int(i) for i in input().split()])), 0
    while i < k and a[0] < b[-1]:
        a.append(b.pop())
        b.appendleft(a.popleft())
        i += 1
    print(sum(a))