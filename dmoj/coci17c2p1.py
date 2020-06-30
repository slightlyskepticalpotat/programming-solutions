import sys
input = sys.stdin.readline

for i in range(int(input())):
    rows, columns = map(int, input().split())
    print((min(rows, columns) - 1)*2)