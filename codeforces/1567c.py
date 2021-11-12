import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, a, b = [int(i) for i in input().strip()], [], [] # alice's way of adding is basically to add each digit mod 10, then add the carry multiplied by 10
    while n:
        a.append(str(n.pop()))
        if n:
            b.append(str(n.pop()))
    a, b = int("".join(a[::-1] if a else "0")), int("".join(b[::-1] if b else "0"))
    print((a + 1) * (b + 1) - 2) # exclude 0