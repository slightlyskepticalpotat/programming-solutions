import sys

input = sys.stdin.readline

for _ in range(int(input())): # set each digit to 0 in one of the numbers
    n, k = map(int, input().split())
    print(pow(n, k, 10 ** 9 + 7))
