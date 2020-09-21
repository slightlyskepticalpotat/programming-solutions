import sys

input = sys.stdin.readline

for i in range(int(input())):
    d, message, n, total = int(input()), input().replace("\n", ""), int(input()), 0
    x = [int(i) for i in input().strip().split()]
    print(d, end = " ")
    for i in range(n):
        total += x[i]
        if total < 0:
            total += len(message)
        elif total >= len(message):
            total %= len(message)
        print(message[total], end = "")
    print("")