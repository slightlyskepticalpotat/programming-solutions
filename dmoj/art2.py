import sys

input = sys.stdin.readline

mod = 244002641 # pow(2654435761, -1, 2 ** 32) modinv
n, m = map(int, input().split())
paintings = [int(input()) * mod % (2 ** 32) for i in range(n)]
print(sum(list(sorted(paintings, reverse = True))[:m]))