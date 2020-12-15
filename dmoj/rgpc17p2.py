import sys

input = sys.stdin.readline

n, m, q = map(int, input().split())
cubes, psa, loc = [int(i) for i in input().split()], [0], {}
for i in range(n):
    psa.append(psa[i] + cubes[i])
    loc[cubes[i]] = i + 1
    
for _ in range(q):
    a, b = map(int, input().split())
    if (psa[loc[b]] - psa[loc[a] - 1]) >> 1 >= m: # bitshift to /2
        print("Enough")
    else:
        print("Not enough")