import sys

input = sys.stdin.readline

laptops, flag = [[int(i) for i in input().split()] for _ in range(int(input()))], False
laptops.sort()

for i in range(1, len(laptops)):
    if laptops[i][1] < laptops[i - 1][1]:
        print("Happy Alex")
        sys.exit(0)
print("Poor Alex")
