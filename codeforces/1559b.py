import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, s = int(input()), input().strip()
    if s.count("?") == n:
        print(("BR" * (n // 2 + 1))[:n])
    else:
        while "?" in s:
            s = s.replace("?R", "BR").replace("R?", "RB").replace("?B", "RB").replace("B?", "BR")
        print(s)