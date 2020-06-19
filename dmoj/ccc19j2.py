import sys
input = sys.stdin.readline

for i in range(int(input())):
    num, char = input().strip().split()
    num = int(num)
    print(num * char)