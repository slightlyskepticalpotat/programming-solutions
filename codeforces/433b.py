n, stones = int(input()), [int(i) for i in input().split()]
sorted_stones = list(sorted(stones))
psa, sorted_psa = [stones[0]], [sorted_stones[0]]
for i in range(n):
    psa.append(psa[i] + stones[i])
    sorted_psa.append(sorted_psa[i] + sorted_stones[i])
for i in range(int(input())):
    t, l, r = map(int, input().split())
    if t == 1:
        print(psa[r] - psa[l - 1])
    elif t == 2:
        print(sorted_psa[r] - sorted_psa[l - 1])
