import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, vals, psa, cnt, ans = int(input()), [int(i) for i in input().strip()], [0], {}, 0
    for i in range(n):
        psa.append(psa[i] + vals[i])
    for i in range(n + 1):
        cnt[psa[i] - i] = cnt.get(psa[i] - i, 0) + 1
    ans = sum([cnt[val] * (cnt[val] - 1) // 2 for val in cnt])
    print(ans)
