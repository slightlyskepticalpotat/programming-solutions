import sys

input = sys.stdin.readline

for _ in range(int(input())):
    oa, ob = map(int, input().split())
    n, s = oa + ob, [char for char in input().strip()]
    for i in range(n // 2):
        if s[i] == "?" and s[n - i - 1] != "?":
            s[i] = s[n - i - 1]
        elif s[i] != "?" and s[n - i - 1] == "?":
            s[n - i - 1] = s[i]
    a, b, q = oa - s.count("0"), ob - s.count("1"), s.count("?")

    if a < 0 or b < 0:
        print(-1)
    elif q % 2:
        if a % 2:
            r = 0
            for i in range(n // 2):
                if r == b:
                    break
                if s[i] == "?" and s[n - i - 1] == "?":
                    s[i] = "1"
                    s[n - i - 1] = "1"
                    r += 2
            for i in range(n):
                if s[i] == "?":
                    s[i] = "0"
        else:
            r = 0
            for i in range(n // 2):
                if r == a:
                    break
                if s[i] == "?" and s[n - i - 1] == "?":
                    s[i] = "0"
                    s[n - i - 1] = "0"
                    r += 2
            for i in range(n):
                if s[i] == "?":
                    s[i] = "1"
        if s.count("0") == oa and s.count("1") == ob and s == s[::-1]:
            print("".join(s))
        else:
            print(-1)
    else:
        if a % 2 or b % 2:
            print(-1)
        else:
            r = 0
            for i in range(n // 2):
                if r == a:
                    break
                if s[i] == "?" and s[n - i - 1] == "?":
                    s[i] = "0"
                    s[n - i - 1] = "0"
                    r += 2
            for i in range(n):
                if s[i] == "?":
                    s[i] = "1"
            if s.count("0") == oa and s.count("1") == ob and s == s[::-1]:
                print("".join(s))
            else:
                print(-1)
