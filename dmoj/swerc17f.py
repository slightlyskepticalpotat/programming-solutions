import sys

input = sys.stdin.readline

w, a = int(input()), 0
for i in range(int(input())):
    w_i, l_i = map(int, input().split())
    a += w_i * l_i
print(a // w)