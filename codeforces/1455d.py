import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, x = map(int, input().split())
    values, searched, swaps = [int(i) for i in input().split()], set(), 0
    while True:
        if values == list(sorted(values)):
            print(swaps)
            break
        elif swaps in searched:
            print(-1)
            break
        searched.add(swaps)
        for i in range(n):
            if values[i] > x:
                x, values[i] = values[i], x
                swaps += 1
                break
