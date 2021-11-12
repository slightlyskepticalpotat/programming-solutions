import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, s, ans = int(input()), input().strip(), ""
    if s.find("abacaba") == s.rfind("abacaba") != -1:
        ans = s.replace("?", "d")
    else:
        for i in range(n - 6):
            test = s[:i] + "".join([s[j] if s[j] != "?" else "abacaba"[j - i] for j in range(i, i + 7)]) + s[i + 7:]
            if test.find("abacaba") == test.rfind("abacaba") != -1:
                ans = test.replace("?", "d")
    if ans:
        print("Yes")
        print(ans)
    else:
        print("No")
