import sys

input = sys.stdin.readline

for _ in range(int(input())):
    b = input().strip()
    a = b[0] + "".join([b[i] for i in range(1, len(b) - 1, 2)]) + b[-1]
    print(a)