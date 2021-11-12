import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, values, counts, ans = int(input()), [int(i) for i in input().split()], {}, 0
    for i in range(n):
        check = values[i] - i
        counts[check] = counts.get(check, 0) + 1
    for same in counts:
        ans += (counts[same] * (counts[same] - 1)) // 2
    print(ans)
