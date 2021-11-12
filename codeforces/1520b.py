import sys

input = sys.stdin.readline

ordinary = []
for i in range(1, 11):
    for j in range(1, 10):
        ordinary.append(int(i * str(j)))

for _ in range(int(input())):
    n, ans = int(input()), 0
    for number in ordinary:
        if 1 <= number <= n:
            ans += 1
    print(ans)
