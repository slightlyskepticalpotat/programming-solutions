import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, mapping = int(input()), {"L": "L", "R": "R", "U": "D", "D": "U"}
    print("".join([mapping[i] for i in input().strip()]))