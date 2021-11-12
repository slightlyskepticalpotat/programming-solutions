import sys

input = sys.stdin.readline

for _ in range(int(input())):
    a, b, q = map(int, input().split())
    psa, ans = [0], []
    for i in range(a * b):
        psa.append(psa[-1])
        if ((i + 1) % a) % b != ((i + 1) % b) % a:
            psa[-1] += 1
    for i in range(q):
        l, r = map(int, input().split())
        ans.append((r // (a * b) * psa[-1] + psa[r % (a * b)]) - (((l - 1) // (a * b) * psa[-1] + psa[(l - 1) % (a * b)])))
    print(*ans)
