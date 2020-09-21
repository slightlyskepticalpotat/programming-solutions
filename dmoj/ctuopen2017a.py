import sys

input = sys.stdin.readline

while True:
    try:
        n = int(input())
        x, answer = [int(i) for i in input().strip().split()], 1
        for i in range(n - 1, 1, -1):
            if x[i] - x[i - 1] != x[i - 1] - x[i - 2]:
                answer = i
                break
        print(answer)
    except:
        break