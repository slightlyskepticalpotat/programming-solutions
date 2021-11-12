import sys

input = sys.stdin.readline

def check(cost, start):
    ans = 0
    for i in range(n):
        ans += int(ans % 2 == start or vals[i] <= cost) # skip if possible
    return ans >= k 

n, k = map(int, input().split())
vals, l, r = [int(i) for i in input().split()], 1, 10 ** 9

while l < r:
    m = (l + r) // 2
    if check(m, 0) or check(m, 1):
        r = m 
    else:
        l = m + 1
print(l)