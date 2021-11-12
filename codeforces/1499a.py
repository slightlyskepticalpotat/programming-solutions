import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k1, k2 = map(int, input().split())
    w, b = map(int, input().split())
    if w * 2 <= min(k1, k2) * 2 + (abs(k1 - k2) // 2) * 2:
        k1, k2 = n - k1, n - k2
        if b * 2 <= min(k1, k2) * 2 + (abs(k1 - k2) // 2) * 2:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
