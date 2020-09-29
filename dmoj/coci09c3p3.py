import sys

input = sys.stdin.readline 

n, c = map(int, input().split())
integers = [int(i) for i in input().split()]
print(*list(sorted(integers, key = lambda x: (integers.count(x), -integers.index(x)), reverse = True)))