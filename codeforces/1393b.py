import sys

input = sys.stdin.readline

n, vals, q = int(input()), [int(i) for i in input().split()], int(input())
cnt, cnt2, cnt4 = [0 for _ in range(10 ** 5 + 1)], 0, 0
for i in range(n):
    cnt2 -= cnt[vals[i]] // 2
    cnt4 -= cnt[vals[i]] // 4
    cnt[vals[i]] += 1
    cnt2 += cnt[vals[i]] // 2
    cnt4 += cnt[vals[i]] // 4

for i in range(q):
    t, x = input().strip().split()
    x = int(x)
    cnt2 -= cnt[x] // 2
    cnt4 -= cnt[x] // 4
    if t == "+":
        cnt[x] += 1
    else:
        cnt[x] -= 1
    cnt2 += cnt[x] // 2
    cnt4 += cnt[x] // 4
    if cnt2 >= 4 and cnt4 >= 1:
        print("YES")
    else:
        print("NO")
