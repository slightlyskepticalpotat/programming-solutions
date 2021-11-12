import sys

input = sys.stdin.readline

for _ in range(int(input())):
    t = [i for i in input().strip()]
    if len(set(t)) == 1:
        print(t[0] * len(t))
    else:
        print("01" * len(t))