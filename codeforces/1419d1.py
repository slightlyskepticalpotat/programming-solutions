import sys

input = sys.stdin.readline

n, prices = int(input()), list(sorted([int(i) for i in input().split()]))
smaller, bigger, ans = prices[:n // 2], prices[n // 2:], 0
final = [smaller.pop() if i % 2 else bigger.pop() for i in range(n)]
ans = sum(final[i - 1] > final[i] and final[i + 1] > final[i] for i in range(1, n - 1))
print(ans)
print(*final) # so we just split the list and alternate
