import bisect, sys

input = sys.stdin.readline

n, k, q = map(int, input().split())
sequence, frequency = [int(i) for i in input().split()], [[] for _ in range(2001)]

psa = [0]
for i in range(n):
    psa.append(psa[i] + sequence[i]) # prefix sum array
    frequency[sequence[i] + 1000].append(i) # save the indices

for i in range(q):
    a, b, x, y = map(int, input().split())
    if psa[y] - psa[x - 1] > k:
        a_pos, b_pos = bisect.bisect_left(frequency[a + 1000], x - 1), bisect.bisect_left(frequency[b + 1000], x - 1)
        if a_pos != len(frequency[a + 1000]) and frequency[a + 1000][a_pos] <= y - 1 and b_pos != len(frequency[b + 1000]) and frequency[b + 1000][b_pos] <= y - 1: # work backwards
            print("Yes")
        else:
            print("No")
    else:
        print("No")