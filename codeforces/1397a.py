import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, count = int(input()), {i: 0 for i in "abcdefghijklmnopqrstuvwxyz"}
    s, ans = "".join([input().strip() for i in range(n)]), True
    for char in s:
        count[char] += 1
    for char in count:
        if count[char] % n:
            ans = False
    if ans:
        print("YES")
    else:
        print("NO")
