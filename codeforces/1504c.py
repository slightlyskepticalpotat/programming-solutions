import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, s, f, a, b  = int(input()), input().strip(), False, [], []
    c, z, j = s.count("1"), s.count("0"), 0
    if s[0] != "1" or s[-1] != "1":
        print("NO")
    elif z % 2 or c % 2:
        print("NO")
    else:
        for i in range(n):
            if s[i] == "1":
                if j < c / 2:
                    a.append("(")
                    b.append("(")
                else:
                    a.append(")")
                    b.append(")")
                j += 1
            else:
                if f:
                    a.append("(")
                    b.append(")")
                else:
                    a.append(")")
                    b.append("(")
                f = not f
        print("YES")
        print("".join(a))
        print("".join(b))
