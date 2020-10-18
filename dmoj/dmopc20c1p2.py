import sys

input = sys.stdin.readline

n, d = map(int, input().split())
trolley = [int(i) for i in input().split()]

for i in range(d):
    n = int(input())
    f, s = trolley[:n], trolley[n:]
    s_f, s_s = sum(f), sum(s)
    if s_f >= s_s:
        trolley = s
        print(s_f)
    else:
        trolley = f
        print(s_s)