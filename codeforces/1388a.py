import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    if n > 30: # 6 + 10 + 14
        print("YES")
        if n - 30 in [6, 10, 14]:
            print(f"6 10 15 {n - 31}")
        else:
            print(f"6 10 14 {n - 30}")
    else:
        print("NO")
