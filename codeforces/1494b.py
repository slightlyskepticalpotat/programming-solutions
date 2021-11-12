import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, u, r, b, l = map(int, input().split())
    ans = False
    
    for i in range(16):
        mask = bin(i)[2:].zfill(4)
        ul, ur, br, bl = int(mask[0]), int(mask[1]), int(mask[2]), int(mask[3])
        if not 0 <= u - (ul + ur) <= n - 2 or not 0 <= l - (ul + bl) <= n - 2:
            continue
        if not 0 <= r - (ur + br) <= n - 2 or not 0 <= b - (br + bl) <= n - 2:
            continue
        ans = True
    if ans:
        print("YES")
    else:
        print("NO")
