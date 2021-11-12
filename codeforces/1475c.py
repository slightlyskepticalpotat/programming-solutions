import sys

input = sys.stdin.readline

for _ in range(int(input())):
    a, b, k = map(int, input().split())
    boys, girls, ways = [int(i) for i in input().split()], [int(i) for i in input().split()], 0
    boys_ready, girls_ready = [0 for i in range(a)], [0 for i in range(b)]
    for i in range(k):
        boys_ready[boys[i] - 1] += 1
        girls_ready[girls[i] - 1] += 1
    for i in range(k):
        ways += k - boys_ready[boys[i] - 1] - girls_ready[girls[i] - 1] + 1 # subtract intersections
    print(ways // 2)
