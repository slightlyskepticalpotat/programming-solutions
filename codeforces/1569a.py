import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, s = int(input()), input().strip()
    if "ab" in s:
        print(s.index("ab") + 1, s.index("ab") + 2)
    elif "ba" in s:
        print(s.index("ba") + 1, s.index("ba") + 2)
    else:
        print(-1, -1)
