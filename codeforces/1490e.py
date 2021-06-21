import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, values = int(input()), [int(i) for i in input().split()]
    values = list(sorted([[values[i]] + [i] for i in range(n)]))
    winner, psa, ans = [False for i in range(n - 1)] + [True], [0], [values[-1][1] + 1] # largest always wins
    for i in range(n):
        psa.append(psa[i] + values[i][0])
    psa.pop(0)
    for i in range(n - 2, -1, -1):
        if psa[i] >= values[i + 1][0] and winner[i + 1]:
            winner[i] = True
            ans.append(values[i][1] + 1)
    print(len(ans))
    print(*list(sorted(ans)))
