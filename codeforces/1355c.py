import sys

input = sys.stdin.readline

a, b, c, d = map(int, input().split())
diff = [0 for i in range(2 * (10 ** 6))]
for x in range(a, b + 1):
    diff[x + b], diff[x + c + 1] = diff[x + b] + 1, diff[x + c + 1] - 1
for i in range(1, 2 * (10 ** 6)):
    diff[i] += diff[i - 1]
for i in range(1, 2 * (10 ** 6)):
    diff[i] += diff[i - 1]
print(sum([diff[-1] - diff[i] for i in range(c, d + 1)]))