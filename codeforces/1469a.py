import sys

input = sys.stdin.readline

for _ in range(int(input())):
    sequence = [char for char in input().strip()]
    if len(sequence) % 2 != 1 and sequence[0] != ")" and sequence[-1] != "(":
        print("yes")
    else:
        print("no")
