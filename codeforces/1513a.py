import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    if k > (n - 1) // 2:
        print(-1)
    else:
        numbers = [i + 1 for i in range(n)]
        for i in range(1, n - 1, 2):
            if k:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                k -= 1
        print(*numbers)
