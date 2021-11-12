import sys 

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    a, w, i, ans = sorted([int(i) for i in input().split()]), sorted([int(i) for i in input().split()], reverse = True), 0, 0
    while w and w[-1] == 1: # handle ones separately
        ans += a.pop() * 2
        w.pop()
    for j in range(len(w)):
        ans += a[i] + a.pop()
        i += w[j] - 1
    print(ans)