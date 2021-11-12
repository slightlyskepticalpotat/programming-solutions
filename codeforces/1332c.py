import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    s, counts, ans = input().strip(), [[0 for i in range(26)] for j in range((k + 1) // 2)], 0
    for i in range(n):
        counts[min(i % k, k - (i % k + 1))][ord(s[i]) - 97] += 1
    for i in range(k // 2): # for each half of a block
        ans += 2 * n // k - max(counts[i])
    if k % 2: # original middle letter
        ans += n // k - max(counts[k // 2])
    print(ans)